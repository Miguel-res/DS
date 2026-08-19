import os
os.system("cls")


while True:
    print("""
0 - Sair
1 - Inicializar o estoque
2 - Modificar uma quantidade
3 - Modificar o nome de um produto
4 - Remover um produto
5 - Listar os produtos
6 - Listar as quantidades
7 - Exibir o estoque
8 - Consultar um produto
""")
    escolha = int(input("Escolha as opções: "))
    if escolha >= 0 and escolha <= 8:
        match escolha:
            case 0:
                print("desligando programa")
                break
            case 1:
                print("Iniciando estoque")
                estoque = {
                    "Arroz": 10,
                    "Feijão": 15,
                    "Macarrão": 20
                }
                produto = input("Qual o produto: ")
                quant = input("Quantidade: ")
                estoque[quant] = produto
                print(estoque)
                print(estoque)
            case 2:
                produto = input("Qual o produto: ")
                quant = input("Quantidade: ")
                estoque[quant] = produto
                print(estoque)
            case 3:
                nome = input("Qual o nome do produto?: ")
                nome_novo = input("Quem é o novo produto?: ")
                estoque[nome_novo] = estoque.pop(nome)
                print(estoque)
            case 4:
                deletar = input("Qual você quer deletar: ")
                del estoque[deletar]
                print(estoque)
            case 5:
                for k, v in estoque.items():
                    print(f"keys: {k}")
            case 6:
                for k, v in estoque.items():
                    print(f"Values: {v}")
            case 7:
                for k, v in estoque.items():
                    print(f"Keys: {k} Values: {v}")
            case 8:
                nome = input("Qual você quer: ")
                if nome in estoque.keys():
                    print(f"Produto {nome} \nQuantidade: {estoque[nome]}")
                else:
                    print("Produto não existente")


