from psycopg2.extras import execute_values

def create_table(column_data, cur, con, schema='public'):
  """
  Cria a tabela people no banco de dados
  Precisa receber uma lista de strings com os nomes e tipos das colunas como parametro column_data no seguinte
  formato [['nome_da_coluna', 'tipo_da_coluna'] .......]
  """
  sql = f"""CREATE TABLE IF NOT EXISTS {schema}.people (\n\tid bigserial"""
  str_cols =  [f',\n\t{col_name} {col_type}' for col_name, col_type in column_data]
  sql += ''.join(str_cols)
  sql += ');'
  cur.execute(sql)
  con.commit()
  return 'Tabela criada'

def insertion(data, header, cur, con, schema='public'):
  """
  Insere dados na tabela people no banco de dados
  Precisa receber uma lista de strings com os nomes das colunas como parametro header
  e o parametro data recebe as tuplas a serem inseridas no banco
  """
  sql = f"INSERT INTO {schema}.people ( {','.join(header)})\n\tVALUES %s;"
  execute_values(cur, sql, data)
  con.commit()
  return 'Tabela populada'
  
