import os
os.system("cls")
import modulo as m
familia = {
        "Edson":{
            "nomepai": "Jurandir",
            "nomemae": "Ester",
            "irmaos": {
                "irmao1":"Edilson",
                "irmao2":"Elaine",
            }
        },
        "Marcelo":{
            "nomepai": "Antonio",
            "nomemae": "Maria",
            "irmaos": {
                "irmao1": "Adriano",
                "irmao2": "Samuel",
                "irmao3": "Carla",
            }
        }
    }
while True:
    m.exibir_menu()
    opcao = int(input("Escolha: "))
    match opcao:
        case 0:
            print("Encerrando Programa...")
            break
        case 1:
            usuario = input("Pessoa: ")
            if m.key_existe(familia, usuario): # se existir
                chave = input("Nova chave: ")
                conteudo = input("Conteudo: ")
                m.criando_dado(familia, usuario, chave, conteudo)
            else:
                print("Pessoa nao existe!")
        case 2:
            while True:
                nome_irmao = input("Nome irmão: ")
                if m.irmao_existe(familia, nome_irmao):
                    numero = len(familia["Edson"]["irmaos"]) + 1
                    chave = f"irmao{numero}"
                    m.criando_irmao(familia, usuario, chave, nome_irmao)
                    m.exibe_dados(familia)
                else:
                    break
        case 3:
            m.exibe_dados(familia)
        case 4:
            familia = {
                "Edson":{
                    "nomepai": "Jurandir",
                    "nomemae": "Ester",
                    "irmaos": {
                        "irmao1":"Edilson",
                        "irmao2":"Elaine",
                    }
                },
                "Marcelo":{
                    "nomepai": "Antonio",
                    "nomemae": "Maria",
                    "irmaos": {
                        "irmao1": "Adriano",
                        "irmao2": "Samuel",
                        "irmao3": "Carla",
                    }
                }
            }