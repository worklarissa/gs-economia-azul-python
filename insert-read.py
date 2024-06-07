#  programa que le arquivos e grava o conteúdo no banco de dados e também lê as infromações do banco de daso e exibe para o uimport csv
import csv
import database as db

conexao = db.conexao_banco()

# def abrir_arquivo():
#   with open('2- participacao-despejo-residuo-plastico.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)




def inserir_dados(conexao):
    cursor = conexao.cursor()
    try:
         with open('2- participacao-despejo-residuo-plastico.csv', 'r') as file:
             reader = csv.reader(file)
             next(reader)
             for row in reader:
                 print(row)
                 entidade, codigo, ano, part_plastico = row
                 sql = "INSERT INTO T_PARTICIPACAO_RESIDUOS (entidade, codigo, ano, part_plastico) VALUES (:1, :2, :3, :4)"
                 cursor.execute(sql, (entidade, codigo, ano, part_plastico))
                 print('inserido')
         conexao.commit()
       
    except Exception as e:
         print('Erro')
    finally:
        cursor.close()
    
    try:
        with open('5- poluicao-agua-cidades.csv', 'r', encoding='utf8') as file:
            reader_teste = csv.reader(file)
            next(reader_teste)
            for row in reader_teste:
                print(row)
                cidade, regiao, entidade, qualidade_ar, poluicao_agua = row
                sql = "INSERT INTO T_POLUICAO_AGUA_CIDADES (cidade, regiao, entidade, qualidade_ar, poluicao_agua) VALUES (:1, :2, :3, :4, :5)"
                cursor.execute(sql, (cidade, regiao, entidade, qualidade_ar, poluicao_agua))
                print('inserido')
        conexao.commit()
    
    except Exception as e:
        print(e)
    finally:
        cursor.close()

inserir_dados(conexao)



