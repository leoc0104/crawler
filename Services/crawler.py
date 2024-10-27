import requests
from bs4 import BeautifulSoup

def get_text_from_uol():
    url = 'https://educacao.uol.com.br/bancoderedacoes/redacoes/o-progresso-da-tecnologia.htm'
    
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        essay_div = soup.find('div', {'class': 'text-composition'})
        if essay_div:
            essay_text = essay_div.get_text()
            return essay_text
        else:
            print("Redação não encontrada na página.")
            return None
    else:
        print(f"Falha ao vasculhar a página. Código: {response.status_code}")
        return None

if __name__ == '__main__':
    text = get_text_from_uol()
    if text:
        with open("output.txt", "w") as file:
            file.write(text)

        print("Redação salva em output.txt")
