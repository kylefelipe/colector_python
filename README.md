# Coletor de dados

Esse coletor é para exemplificar com pegar dados de uma API e subir para um banco de dados [PostgreSQL](https://www.postgresql.org)

## Criando o ambiente

Para criar o ambiente, basta rodar no terminal:

```shell
python3 -m venv .venv
```

Logo após ative o ambiente:

```shell
source .venv/bin/activate
```

> Caso use um terminal diferente do bash, verifique a doc dele antes

Assim o seu ambiente virtual estará ativado e pronto para ser usado.
Instale as dependências:

```shell
pip install -r requirements.txt
```

Faça uma cópia do arquivo .env.example e renomeie para .env e edite lá dentro as variáveis de ambiente para receber os dados da conexão com o banco, url base que vai fazer a busca de dados e etc.

## Arquivo .env

Contém as seguintes variáveis:

* PG_HOST='host_do_banco' -> Recebe o Host do banco de dados  
* PORT=5433 -> Recebe a porta do banco  
* DATABASE='nome_do_banco' -> Recebe o nome do banco onde será armazenado os dados  
* PG_USER='nome_do_usuario_do_banco' -> Recebe usuário que será utilizado no banco  
* PG_PASSWORD='senha_do_usuario_do_banco' -> Recebe senha do usuário do banco  
* BASE_URL='https://swapi.dev/api' -> Recebe base da API a ser utilizada  

## Uso

Após configurar o ambiente, basta rodar o arquivo `main.py` que irá pegar os dados da API, criar a tabela no banco, caso não exista, e subir os dados recebidos para o banco.
