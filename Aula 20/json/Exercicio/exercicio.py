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

                with open(arquivo, 'r', encoding="utf-8") as f:
                    animais = json.load(f) 

            cpf = input("Cpf do dono: ")
            nome = input("Nome do animal: ")
            idade = int(input("Idade do animal: "))
            raca = float(input("Raça: "))

            existe = False

            for animal in animais:
                if animal["cpf"] == cpf:
                    existe == True
                    break

            if existe:
                print("Cpf já está cadastrado! ")
            else:
                animal = {
                    'cpf do dono': cpf,
                    'nome do animal': nome,
                    'idade do animal': idade,
                    'raça': raca
                }

                animais.append(animal)

                with open(arquivo, 'w', encoding="utf-8") as f:
                    json.dump(animais, f, indent = 4, ensure_ascii = False)

            print("Pessoa cadastrada!")

        case 2:
            if os.path.exists(arquivo):

                with open(arquivo, 'r', encoding="utf-8") as f:

                    animais = json.load(f) 


                if len(animais) == 0:
                    print("Nenhum animal cadastrada")
                else:
                    print("------ listagem dos animais ------")

                    print(f"{'CPF':14} | {'NOME':20} | {'IDADE':7} | {'RAÇA':8}")
                    print(60 * "-")
                    for animal in animais:
                        print(f"{animal['cpf do dono']:14} | {animal['nome do animal']:20} | {animal['idade do animal']:7d} | {animal['raça']:8.2f}")

            else:
                print("Arquivo não encontrado!")

        case 3:
            if os.path.exists(arquivo):

                with open(arquivo, 'r', encoding="utf-8") as f:
                    animais = json.load(f) 

                cpf = input("CPF: ")

                encontrado = None

                for animal in animais:
                    if animal['cpf'] == cpf:
                        encontrado = animal
                        break

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
                                    
                with open(arquivo, 'r', encoding="utf-8") as f:
                    animais = json.load(f) 
                                    
                    if len(animais) == 0:
                        print("Nenhum animal cadastrada")
                    else:
                        print("------ listagem dos animais ------")
                        
                        print(f"{'CPF':14} | {'NOME':20} | {'IDADE':7} | {'RAÇA':8}")
                        print(60 * "-")
                        for animal in animais:
                            print(f"{animal['cpf do dono']:14} | {animal['nome do animal']:20} | {animal['idade do animal']:7d} | {animal['raça']:8.2f}")
                        
                        id_editar = input("Informe o CPF do Dono que deseja editar: ").strip()
                        
                        print("Digite os novos dados (ou aperte ENTER para manter o valor atual):")
                        novo_nome = input(f"Novo Nome [{animais['nome']}]: ").strip()
                        nova_especie = input(f"Nova Espécie [{animais['especie']}]: ").strip()
                        nova_idade = input(f"Nova Idade [{animais['idade']}]: ").strip()
                        
                        if novo_nome:
                            animais["nome"] = novo_nome
                        if nova_especie:
                            animais["especie"] = nova_especie
                        if nova_idade:
                            animais["idade"] = nova_idade
                        
                        with open(arquivo, "w", encoding="utf-8") as f:
                            json.dump(animais, f, indent=4, ensure_ascii=False)
                        
                            print("Pet atualizado com sucesso!")
        case 5:
            if os.path.exists(arquivo):
                        
                            with open(arquivo, 'r', encoding="utf-8") as f:
                                animais = json.load(f) 
                        
                            if len(animais) == 0:
                                print("Nenhum animal cadastrada")
                            else:
                                print("------ listagem dos animais ------")
            
                                print(f"{'CPF':14} | {'NOME':20} | {'IDADE':7} | {'RAÇA':8}")
                                print(60 * "-")
                                for animal in animais:
                                    print(f"{animal['cpf do dono']:14} | {animal['nome do animal']:20} | {animal['idade do animal']:7d} | {animal['raça']:8.2f}")
            
                            id_excluir = input("Informe o CPF do Dono que deseja excluir: ").strip()

                            pet_encontrado = None
                            for pet in pets:
                                if pet["id"] == id_excluir:
                                    pet_encontrado = pet
                                    break

                            if pet_encontrado is not None:
                                print(f"""
                                --- REGISTRO ENCONTRADO PARA EXCLUSÃO ---
                                ID: {pet_encontrado['id']}
                                Nome: {pet_encontrado['nome']}
                                Espécie: {pet_encontrado['especie']}
                                Idade: {pet_encontrado['idade']}
                                """)

                            confirmar = input("Tem certeza que deseja excluir? (S/N): ").strip().upper()

                            if confirmar == "S":
                                pets.remove(pet_encontrado)

                                with open(arquivo, "w", encoding="utf-8") as f:
                                    json.dump(pets, f, indent=4, ensure_ascii=False)

                                print("Pet excluído com sucesso!")
                            else:
                                print("Operação cancelada")
            