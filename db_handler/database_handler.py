def db_version(cur):
    """
    Verifica a versão do banco
    """
    print('PostgresSQL version')
    cur.execute('SELECT PostGIS_Full_Version()')
    print(cur.fetchone())
    return True


def clear_table(schema, tablename, cur, con):
    """
    Limpa a tabela e restaura a sequence para 0
    """
    sql = f"TRUNCATE {schema}.{tablename} RESTART IDENTITY CASCADE;"
    cur.execute(sql)
    con.commit()
    return True
