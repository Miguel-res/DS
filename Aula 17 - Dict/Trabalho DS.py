import os
os.system("cls")
dicionario = {}
while True:
    opcao = input("""
    M E N U
    -------
    0 - Sair
    1 - Zerar o dicionário
    2 - Adicionar uma key
    3 - Editar um value
    4 - Remover uma key
    5 - Exibe o dicionário
          
          Escolha: """)
    
    match opcao:
        case 0:
            print("Desligando programa...")
            break
        case 1:
            del dicionario
            print(">>>>> Dicionário zerado!")
        case 2:
            nome_key = input("Nome da key: ")   
        case 3:
        case 4:
        case 5:
            