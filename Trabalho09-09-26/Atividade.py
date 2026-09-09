import modulo as m


dicionario: dict = {}

while True:
    m.exibir_menu()
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            m.zerar_dicionario(dicionario)
        case "2":
            m.adicionar_key(dicionario)
        case "3":
            m.editar_value(dicionario)
        case "4":
            m.remover_key(dicionario)
        case "5":
            m.exibir_dicionario(dicionario)
        case "0":
            print("Encerrando o programa...")
            break
        case _:
            print("Opção inválida, tente novamente.")