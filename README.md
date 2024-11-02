# Python Crawler Project

Este é um projeto de *crawler* em Python com arquitetura MVC, que extrai e manipula dados em uma collection do MongoDB.

## Funcionalidades

- **Crawler**: Extrai dados de fontes definidas.
- **NER (Named Entity Recognition)**: Processa o conteúdo extraído para identificar e armazenar entidades relevantes no MongoDB.
- **CRUD**: Manipulação completa dos dados extraídos, incluindo criação, leitura, atualização e exclusão.
- **Arquitetura MVC**: Separação clara de responsabilidades entre Models, Views e Controllers.
- **Configuração via arquivo `.env`**: Permite definir variáveis de ambiente para configuração de banco de dados e outras credenciais.

## Tecnologias Utilizadas

- **Python**
- **Flask**: Para criação de API e interface web.
- **MongoDB**: Armazenamento dos dados extraídos e processados.
- **JavaScript**: Para interações no lado do cliente.
- **HTML e CSS**: Interface básica para visualização dos dados.

## Estrutura do Projeto

```
📂 crawler-python
 ┣ 📂 Controllers        # Contém a lógica para manipulação de dados e fluxo de controle
 ┃ ┗ 📄 EntityController.py   # Gerencia as operações CRUD para entidades
 ┣ 📂 Models             # Contém a estrutura de dados e interações com o MongoDB
 ┃ ┗ 📄 Entity.py             # Modelo que representa as entidades e suas interações com o MongoDB
 ┣ 📂 Services           # Contém scripts para coleta e processamento de dados
 ┃ ┣ 📄 crawler.py           # Script de crawler para extrair dados
 ┃ ┗ 📄 ner.py               # Script de NER para identificar entidades no conteúdo extraído
 ┣ 📂 views              # Contém arquivos estáticos para o frontend
 ┃ ┣ 📄 app.js               # JavaScript para interações no frontend
 ┃ ┣ 📄 index.html           # Página HTML principal para visualização dos dados
 ┃ ┗ 📄 style.css            # CSS para estilização da interface
 ┣ 📄 .env               # Arquivo de variáveis de ambiente para configuração
 ┣ 📄 .env.example       # Exemplo de arquivo .env
 ┣ 📄 .gitignore         # Arquivo para especificar arquivos ignorados pelo Git
 ┣ 📄 output.txt         # Exemplo de saída gerada pelo crawler
 ┣ 📄 README.md          # Documentação do projeto
 ┣ 📄 requirements.txt   # Dependências do projeto
 ┗ 📄 routes.py          # Define as rotas e mapeia para os controllers correspondentes
```

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/leoc0104/crawler.git
   ```
2. Entre no diretório do projeto:
   ```bash
   cd crawler-python
   ```
3. Instale as dependências:
   ```bash
   sudo apt install python3 python3-pip
   pip install -r requirements.txt
   ```
4. Renomeie o arquivo `.env.example` para `.env` (ou clone) e configure as variáveis de ambiente.

## Executando o Projeto

1. Execute o crawler:
   ```bash
   python3 Services/crawler.py
   ```
2. Inicie o servidor Flask:
   ```bash
   python3 routes.py
   ```
3. Inicie o servidor web:
   ```bash
   python3 -m http.server 8000
   ```

## Estrutura do Banco de Dados (MongoDB)

A coleção `entities` armazena os dados extraídos pelo *crawler* e processados pelo NER. Cada documento possui os seguintes campos:

- **_id**: Identificador único.
- **name**: Nome da entidade.
- **label**: Rótulo da entidade extraída.
