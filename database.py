# função que encapsula o banco de dados
import oracledb
from login import user,senha

def conexao_banco():
    dsn = oracledb.makedsn('oracle.fiap.com.br', 1521, service_name='ORCL')
    connection = oracledb.connect(user=user, password=senha, dsn=dsn)

    cursor = connection.cursor()
    print('conectado')
    return connection
    


