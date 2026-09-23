import os
os.system("cls")
while True:
    print("""
|====== M E N U ======|
| 1 - Gravar linhas   |
| 2 - Listar arquivo  |
| 3 - Pesquisar nome  |
|=====================|
""")
    escolha = input("Escolha uma opção: ")
    match escolha:
        case '1':
            with open("arquivo.txt", "a", encoding="utf-8") as arquivo:
                print("Digite o nome ou ENTER em nome para finalizar...")
                while True:
                    print(30 * '-')
                    nome = input("Nome: ")
                    if nome == '':
                        break
                    else:
                        idade = int(input("Idade: "))
                        altura = float(input("Altura:"))
                        arquivo.write(f"{nome},{idade},{altura}\n")
        case '2':
            with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    # "Edson,45,1.9"
                    lista = linha.split(',')
                    #             0       1     2
                    # lista = ["Edson", "45", "1.9"]
                    print(30 * '-')
                    print(f"Nome.........: {lista[0]}")
                    print(f"Idade........: {lista[1]}")
                    print(f"Altura.......: {lista[2]}")
        case '3':
            with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
                procura = input("Quem você Procura: ")
                for linha in arquivo:
                    lista = linha.split(',')
                    if procura == lista[0]:
                        print(f"Nome.........: {lista[0]}")
                        print(f"Idade........: {lista[1]}")
                        print(f"Altura.......: {lista[2]}")
