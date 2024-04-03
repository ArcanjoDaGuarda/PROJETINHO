from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import *

admin.site.register(Aula)
admin.site.register(Relatorio)

class CustomUserV2ChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUserV2

class CustomUserV2Admin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'projeto_proin', 'get_nome_turma', 'profile_picture')

    def get_nome_turma(self, obj):
        return obj.Nome_Turma
    get_nome_turma.short_description = 'Turma'

admin.site.register(CustomUserV2, CustomUserV2Admin)

from .models import Noticia
from .models import Turma

admin.site.register(Noticia)
admin.site.register(Turma)