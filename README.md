
# Gerenciador de empresas e CNPJs

Teste prático para a vaga de desenvolvedor na empresa Youtan

## Requisitos

Criar a aplicação das telas com Python, utilizando Django com MVT. Deve-se utilizar
Bootstrap para o CSS das telas. Como banco de dados, pode-se utilizar qualquer um
a seu critério. Como interação JS nas telas, desejável utilizar JQuery ou JS puro.

## Instalação

Foi utilizado Python 3.10 para a criação do app.

Clone o repositório:
```bash
git clone https://github.com/pabloghid/youtan_challenge.git
```

Crie um ambiente virtual (opcional, mas recomendado). Ex:
```bash
python -m venv venv
```
Ative o ambiente virtual.
No Windows:
```bash
venv\Scripts\activate
```
No Linux/macOS:
```bash
source venv/bin/activate
```

Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```
Configure o banco de dados:
- Foi utilizado o banco mySQL para essa aplicação. O arquivo settings.py está configurado para essa engine. 
- É necessário modificar o arquivo ```.env.example```, retirando o .example e colocando suas configurações do banco de dados.
Também é necessário criar a database antes de fazer as migrations. Nesse caso, vá até o banco mySQL e crie a database com o nome ```company_management```.

Após criar o banco de dados, execute as migrations:
```bash
python manage.py migrate
```

Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

## Funcionamento

É necessário estar logado para utilizar as funções do gerenciador. 

Ele é capaz de adicionar novas empresas e dentro delas, adicionar CNPJs. Também apresenta funções de edição e deleção de empresas. Conta com mensagens de erros e sucesso e paginação nas telas de empresas e CNPJs.

Foi utilizado Ajax para a criação e edição de CNPJs em um modal.

Para a criação do visual, foi utilizado apenas html e bootstrap.