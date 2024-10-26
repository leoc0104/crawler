import requests
from bs4 import BeautifulSoup
from pprint import pprint

def get_text_from_uol():
    url = 'https://educacao.uol.com.br/bancoderedacoes/redacoes/o-progresso-da-tecnologia.htm'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        text = soup.find('div', {'class': 'text'}).get_text()

        return text
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        return None

if __name__ == '__main__':
    text = get_text_from_uol()
    if text:
        print(text)
