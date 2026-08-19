import os
os.system("cls")

def inicializar() -> None:
    print("criando dicionario...")
    funcionario = {
    "Jonas": "pedreiro"
    }
    print(f"Dicionario de profições criado{funcionario}")

def modificar_value() -> None:
    profissao = input("Qual a profissão: ")
    nome = input("qual o nome do cidadão(Tem que estar no Dicionario): ")
    funcionario[nome] = profissao
    print(funcionario)
funcionario = dict()

while True:
    print("""
0 - Sair
1 - Inicializar o dicionario
2 - Modificar um value
3 - Modificar uma key
4 - Remover uma key
5 - Listar as keys
6 - Listar os values
7 - Exibir o dicionario
""")

    escolha = int(input("Escolha as opções: "))
    if escolha >= 0 and escolha <= 7:
        match escolha:
            case 0:
                print("desligando programa")
                break
            case 1:
                inicializar()
            case 2:
                modificar_value()
            case 3:
                
                nome = input("Qual o nome do Cidadão?: ")
                nome_novo = input("Quem voce deseja registrar?: ")
                funcionario[nome_novo] = funcionario.pop(nome)
                print(funcionario)

            case 4:

                deletar = input("Qual você quer deletar: ")
                del funcionario[deletar]
                print(funcionario)

            case 5:
                for k, v in funcionario.items():
                    print(f"keys: {k}")

            case 6:
                for k, v in funcionario.items():
                    print(f"Values: {v}")
            case 7:
                for k, v in funcionario.items():
                    print(f"Keys: {k} Values: {v}")
    else:
        print("Escolha uma das opções")