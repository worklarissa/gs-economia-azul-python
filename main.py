from database import conexao_banco

def show_menu():
    print("Menu:")
    print("1. Ver Participação Participação na Emissão Global de Plásticos para o Oceano")
    print("2. Ver Poluição nas cidades")
    print("3. Sair")
    return input("Escolha uma opção: ")

def fetch_part_despejo(cursor):
    cursor.execute("SELECT * FROM T_PARTICIPACAO_RESIDUOS")
    for row in cursor.fetchall():
        print(row)

def fetch_poluicao_cidades(cursor):
    cursor.execute("SELECT * FROM T_POLUICAO_AGUA_CIDADES")
    for row in cursor.fetchall():
        print(row)

def main():
    connection = conexao_banco()
    if connection is None:
        return

    cursor = connection.cursor()

    # Menu para o usuário
    while True:
        choice = show_menu()
        if choice == '1':
            fetch_part_despejo(cursor)
        elif choice == '2':
            fetch_poluicao_cidades(cursor)
        elif choice == '3':
            break
        else:
            print("Opção inválida, tente novamente.")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
