from django.shortcuts import render, redirect
from videos.models import Turma, Relatorio, Aula, StatusAula, StatusRelatorio, CustomUserV2
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import *



@login_required
def index(request):
    user_name = request.user.username
    noticias = Noticia.objects.all().order_by('-data_publicacao')

    return render(request, 'index.html', {'user_name': user_name, 'noticias': noticias})

@login_required
def lista_aula(request):
    """
    Exibe a lista de aulas para o usuário.
    """
    aulas = Aula.objects.all()
    usuario = request.user

    if request.method == 'POST':
        # Lógica para marcar aulas como concluídas
        for aula in aulas:
            campo_assistida = f'aula_{aula.id}_assistida'
            if campo_assistida in request.POST:
                # Identifica a aula específica
                aula_id = int(request.POST[campo_assistida].split('_')[1])
                aula_obj = Aula.objects.get(pk=aula_id)
                # Verifica se já existe um status para esta aula e usuário
                status_aula, created = StatusAula.objects.get_or_create(aula=aula_obj, usuario=usuario)
                # Atualiza o status da aula
                status_aula.assistida = request.POST[campo_assistida] == 'True'
                status_aula.save()

                # Se todas as aulas do usuário forem concluídas, marque "concluido_por_todas" como True
                if all(a.assistida for a in usuario.aulas_concluidas.all()):
                    usuario.concluido_por_todas = True
                    usuario.save()

        # Retorne um redirecionamento para a página de lista de aulas após salvar o status
        return redirect('lista_aula')

    # Restante do código para renderização do template
    context = {
        'aulas': aulas,
        'usuario': usuario,
    }

    # Lógica para identificar aulas concluídas
    def aula_concluida(usuario, aula):
        try:
            status_aula = StatusAula.objects.filter(
                aula=aula,
                usuario=usuario,
            ).order_by('-id').first()
            if status_aula:
                return status_aula.assistida
            else:
                return False
        except StatusAula.DoesNotExist:
            return False

    # Contagem precisa de aulas concluídas
    aulas_concluidas = sum(aula_concluida(usuario, aula) for aula in aulas)

    # Cálculo ajustado da porcentagem
    total_aulas = aulas.count()
    porcentagem_aulas = 0
    if total_aulas > 0:
        porcentagem_aulas = (aulas_concluidas / total_aulas) * 100

    context.update({
        'total_aulas': total_aulas,
        'aulas_concluidas': aulas_concluidas,
        'aulas_faltando': total_aulas - aulas_concluidas,
        'porcentagem_aulas': porcentagem_aulas,
    })

    return render(request, 'ListaTemplate.html', context)

@login_required
def salvar_status_aula(request, aula_id):
    """
    Salva o status da aula para o usuário atual.
    """
    aula = get_object_or_404(Aula, pk=aula_id)
    usuario = request.user
    
    if request.method == 'POST':
        form = StatusAulaForm(request.POST)
        if form.is_valid():
            status_aula, created = StatusAula.objects.get_or_create(aula=aula, usuario=usuario)
            status_aula.assistida = form.cleaned_data['assistida']
            status_aula.save()

            # Se todas as aulas do usuário forem concluídas, marque "concluido_por_todas" como True
            if all(a.assistida for a in usuario.aulas_concluidas.all()):
                usuario.concluido_por_todas = True
                usuario.save()

            # Adiciona uma mensagem de sucesso
            messages.success(request, 'Status da aula salvo com sucesso.')
            # Retorne um redirecionamento para a página de lista de aulas após salvar o status
            return redirect('lista_aula')
    else:
        form = StatusAulaForm()

    # Renderiza o formulário com possíveis erros ou formulário vazio
    return render(request, 'ListaTemplate.html', {'form': form, 'aula_id': aula_id})


@login_required
def lista_relatorio(request):
    """
    Exibe a lista de relatórios para o usuário.
    """
    relatorios = Relatorio.objects.all()
    usuario = request.user

    if request.method == 'POST':
        # Lógica para marcar relatórios como concluídos
        for relatorio in relatorios:
            campo_concluido = f'relatorio_{relatorio.id}_concluido'
            if campo_concluido in request.POST:
                # Identifica o relatório específico
                relatorio_id = int(request.POST[campo_concluido].split('_')[1])
                relatorio_obj = Relatorio.objects.get(pk=relatorio_id)
                # Verifica se já existe um status para este relatório e usuário
                status_relatorio, created = StatusRelatorio.objects.get_or_create(relatorio=relatorio_obj, usuario=usuario)
                # Atualiza o status do relatório
                status_relatorio.concluido = request.POST[campo_concluido] == 'True'
                status_relatorio.save()

                # Se todos os relatórios do usuário forem concluídos, marque "concluido_por_todos" como True
                if all(rel.concluido for rel in usuario.relatorios_concluidos.all()):
                    usuario.concluido_por_todos = True
                    usuario.save()

        # Retorne um redirecionamento para a página de lista de relatórios após salvar o status
        return redirect('lista_relatorio')

    # Restante do código para renderização do template
    context = {
        'relatorios': relatorios,
        'usuario': usuario,
    }

    # Lógica para identificar relatórios concluídos
    def relatorio_concluido(usuario, relatorio):
        try:
            status_relatorio = StatusRelatorio.objects.filter(
            relatorio=relatorio,
            usuario=usuario,
            ).order_by('-id').first()
            if status_relatorio:
                return status_relatorio.concluido
            else:
                return False
        except StatusRelatorio.DoesNotExist:
            return False

    # Contagem precisa de relatórios concluídos
    relatorios_concluidos = sum(relatorio_concluido(usuario, relatorio) for relatorio in relatorios)

    # Cálculo ajustado da porcentagem
    total_relatorios = relatorios.count()
    porcentagem_relatorio = 0
    if total_relatorios > 0:
        porcentagem_relatorio = (relatorios_concluidos / total_relatorios) * 100

    context.update({
        'total_relatorios': total_relatorios,
        'relatorios_concluidos': relatorios_concluidos,
        'relatorios_faltando': total_relatorios - relatorios_concluidos,
        'porcentagem_relatorio': porcentagem_relatorio,
    })

    return render(request, 'relatorios.html', context)

@login_required
def salvar_status_relatorio(request, relatorio_id):
    """
    Salva o status do relatório para o usuário atual.
    """
    relatorio = get_object_or_404(Relatorio, pk=relatorio_id)
    usuario = request.user
    
    if request.method == 'POST':
        form = StatusRelatorioForm(request.POST)
        if form.is_valid():
            status_relatorio, created = StatusRelatorio.objects.get_or_create(relatorio=relatorio, usuario=usuario)
            status_relatorio.concluido = form.cleaned_data['concluido']
            status_relatorio.save()

            # Se todos os relatórios do usuário forem concluídos, marque "concluido_por_todos" como True
            if all(rel.concluido for rel in usuario.relatorios_concluidos.all()):
                usuario.concluido_por_todos = True
                usuario.save()

            # Adiciona uma mensagem de sucesso
            messages.success(request, 'Status do relatório salvo com sucesso.')
            # Retorne um redirecionamento para a página de lista de relatórios após salvar o status
            return redirect('lista_relatorio')
    else:
        form = StatusRelatorioForm()

    # Renderiza o formulário com possíveis erros ou formulário vazio
    return render(request, 'relatorios.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                # Redirecionar para uma página de sucesso
                return HttpResponseRedirect(reverse('pagina_sucesso'))
            else:
                return HttpResponse("Sua conta está desativada.")
        else:
            print(f"Tentativa de login falhou para o usuário: {username}")
            return HttpResponse("Credenciais inválidas.")
    else:
        return render(request, 'login.html', {})

@login_required
def pagina_sucesso(request):
    return redirect('/home/')

@login_required
def pesquisar_por_nome(request):
    # Inicialmente, obtém todas as aulas
    aulas = Aula.objects.all()

    if request.method == 'POST':
        # Se a solicitação é um POST, obtém o nome pesquisado e filtra as aulas
        nome_pesquisa = request.POST.get('nome')
        if nome_pesquisa:
            aulas = Aula.objects.filter(nome_da_aula__icontains=nome_pesquisa)

    elif request.method == 'GET':
        # Se a solicitação é um GET, obtém o nome pesquisado e filtra as aulas
        nome_pesquisa = request.GET.get('nome')
        if nome_pesquisa:
            aulas = Aula.objects.filter(nome_da_aula__icontains=nome_pesquisa)

    # Retorna a resposta renderizada com o formulário de pesquisa e os resultados (se houver)
    return render(request, 'ListaTemplate.html', {'aulas': aulas})


@login_required
def pesquisar_relatorio_por_nome(request):
    if request.method == 'GET':
        nome_pesquisa = request.GET.get('nome')
        relatorios = Relatorio.objects.filter(nome_do_relatorio__icontains=nome_pesquisa)
        return render(request, 'relatorios.html', {'relatorios': relatorios})


@login_required
def sair(request):
    logout(request)
    return redirect('user_login')

@login_required
def sua_visualizacao_protegida(request):
    return render(request, 'login.html')


from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from videos.models import CustomUserV2

from django.core.files.storage import default_storage

def registro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        projeto_proin = request.POST.get('projeto_proin')

        profile_picture = request.FILES.get('profile_picture')

        try:
            # Salvar a imagem no sistema de arquivos
            if profile_picture:
                file_path = default_storage.save(f'profile_pics/{profile_picture.name}', profile_picture)
            else:
                file_path = None

            # Criar um novo usuário
            user = CustomUserV2.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                projeto_proin=projeto_proin,
                profile_picture=file_path
            )
            
            # Autenticar o usuário após o registro
            authenticated_user = authenticate(username=username, password=password)
            login(request, authenticated_user)

            # Redirecionar para a página desejada após o registro
            return redirect('user_login') 

        except Exception as e:
            # Se houver um erro ao criar o usuário, você pode imprimir para depuração
            print(f"Erro ao criar usuário: {e}")

            # Adicione uma mensagem de erro para ser exibida na página de registro
            error_message = "Erro ao criar usuário. Por favor, tente novamente."
            return render(request, 'registro.html', {'error_message': error_message})

    return render(request, 'registro.html')


def lista_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'lista_noticias.html', {'noticias': noticias})