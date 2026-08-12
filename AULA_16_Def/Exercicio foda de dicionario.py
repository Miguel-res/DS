import os
os.system("cls")

while True:
    print("""
0 - Sair
1 - Inicializar o dicionario
2 - Modificar um value
3 - Modificar uma key
4 - Remover um value
5 - Remover uma key
6 - Listar as keys
7 - Listar os values
8 - Exibir o dicionario
""")

    escolha = int(input("Escolha as opções: "))
    if escolha >= 0 and escolha <= 8:
        match escolha:
            case 0:
                print("desligando programa em 3")
                break
            case 1:
                print("")
    