import requests
from bs4 import BeautifulSoup

def get_noticias():
    url = 'https://oestegoiano.com.br'  # URL da página de notícias do Oeste Goiano
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    noticias = []

    post_list_boxes = soup.find_all('div', class_='uc_post_list_box')
    for post_list_box in post_list_boxes:
        titulo = post_list_box.find('div', class_='uc_post_list_title').find('a').text.strip()
        descricao = post_list_box.find('div', class_='ue-grid-item-meta-data second-cf').text.strip()

        noticias.append({'titulo': titulo, 'descricao': descricao})

    return noticias

# Teste para verificar se as notícias estão sendo puxadas corretamente
noticias = get_noticias()
for noticia in noticias:
    print('Título:', noticia['titulo'])
    print('Descrição:', noticia['descricao'])
    print('---')