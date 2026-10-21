import json
import os
os.system("cls")
arquivo = "Vet.json"
while True:
    print("""
0 - SAIR
1 - Cadastrar [cadastra um que não exista]
2 - Listar
3 - Buscar
4 - Editar
5 - Excluir
""")
    escolha = input("Escolha: ")

    match escolha:
        case 0:
            print("desligando programa")
            break
        case 1:
            if os.path.exists(arquivo):
    # abre o arquivo para leitura

                with open(arquivo, 'r', encoding="utf-8") as f:
                    # coonverte o json em uma lista de dicionarios
                    animais = json.load(f) # se existir ele gera uma lista com dados

            # solicitar os dados ao usuário
            cpf = input("Cpf do dono: ")
            nome = input("Nome do animal: ")
            idade = int(input("Idade do animal: "))
            raca = float(input("Raça: "))

            # Verificar se o cpf já existe ou não
            existe = False

            for animal in animais:
                if animal["cpf"] == cpf:
                    existe == True
                    break

            if existe:
                print("Cpf já está cadastrado! ")
            else:
                # Criar um dicionario com dados
                animal = {
                    'cpf do dono': cpf,
                    'nome do animal': nome,
                    'idade do animal': idade,
                    'raça': raca
                }

                # adiciona o dicionario à lista
                animais.append(animal)

                with open(arquivo, 'w', encoding="utf-8") as f:
                    # grava a lista no formato json
                    json.dump(animais, f, indent = 4, ensure_ascii = False)

            print("Pessoa cadastrada!")

        case 2:
            if os.path.exists(arquivo):
                # abre o arquivo para leitura

                with open(arquivo, 'r', encoding="utf-8") as f:
                    # coonverte o json em uma lista de dicionarios
                    animais = json.load(f) # se existir ele gera uma lista com dados

                # verificar se existem registros
                if len(animais) == 0:
                    print("Nenhum animal cadastrada")
                else:
                    print("------ listagem dos animais ------")

                    # percorre todos os registros
                    print(f"{'CPF':14} | {'NOME':20} | {'IDADE':7} | {'RAÇA':8}")
                    print(60 * "-")
                    for animal in animais:
                        print(f"{animal['cpf do dono']:14} | {animal['nome do animal']:20} | {animal['idade do animal']:7d} | {animal['raça']:8.2f}")

            else:
                print("Arquivo não encontrado!")

        case 3:
            if os.path.exists(arquivo):
                # abre o arquivo para leitura

                with open(arquivo, 'r', encoding="utf-8") as f:
                    # coonverte o json em uma lista de dicionarios
                    animais = json.load(f) # se existir ele gera uma lista com dados

                cpf = input("CPF: ")

                encontrado = None

                # percorrer os registros
                for animal in animais:
                    if animal['cpf'] == cpf:
                        encontrado = animal
                        break

                # verifica se encontrou a pessoa
                if encontrado is not None:
                    print(f"""
                    CPF: {encontrado['cpf']}
                    Nome: {encontrado['nome']}
                    Idade: {encontrado['idade']}
                    Raça: {encontrado['raça']}
                    """)
                else:
                    print("Pessoa não encontrada!")
            else:
                print("Arquivo não encontrado!")

        case 4:
            if os.path.exists(arquivo):
                # abre o arquivo para leitura
            
                with open(arquivo, 'r', encoding="utf-8") as f:
                    # coonverte o json em uma lista de dicionarios
                    animais = json.load(f) # se existir ele gera uma lista com dados
            
                            # verificar se existem registros
                if len(animais) == 0:
                    print("Nenhuma pessoa cadastrada")
                else:
                    print("------ listagem das pessoas ------")
            