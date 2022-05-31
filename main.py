import psycopg2
from os import environ as ENV # Pega as variáveis de ambiente
from dotenv import load_dotenv
from api_handler.get_data import getData
from db_handler import database_handler as db, people_table as pt

load_dotenv() # Configurando as variáveis de ambiente

# pegando os dados da API
raw_data = getData()
data_header = [colName for colName in raw_data["results"][0].keys()]
people_columns = [[col_name, 'text'] for col_name in data_header]
next_page = raw_data["next"]

# Pegando apenas os valores dos dicionários para serem inseridos no banco.
data = [list(tup.values()) for tup in raw_data["results"]]

params = {
    "port" : ENV["PORT"],
    "database" : ENV["DATABASE"],
    "user" : ENV["PG_USER"],
    "password" : ENV["PG_PASSWORD"],
    "host" : ENV["PG_HOST"]
}

# Criando tabela de personagens
con = psycopg2.connect(**params)

cur = con.cursor()

# testando Conexão
db.db_version(cur)

# Criando a tabela no banco caso ela não exista
pt.create_table(people_columns, cur, con)

# Populando a tabela

pt.insertion(data, data_header, cur, con)

