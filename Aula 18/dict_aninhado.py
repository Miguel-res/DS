import os
os.system("cls")
import modulo as m
# SUBALGORITMOS
os.system("cls")

# Dicionário de dicionário (níveis)
pessoa = {
        "Edson":{
            "nomepai": "Jurandir",
            "nomemae": "Ester",
            "irmao": "Edilson",
        },
        "Marcelo":{
            "nomepai": "Antonio",
            "nomemae": "Maria",
            "irmao": "Adriano",
        }
    }
pessoa2 = {
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
    # Exibir o dicionario de forma correta
    os.system("cls")
    m.exibe_dados(pessoa2)
    # Criando uma key nivel 1
    usuario = input("Pessoa: ")
    if m.key_existe(pessoa2, usuario): # se existir
        chave = input("Nova chave: ")
        conteudo = input("Conteudo: ")
        m.criando_dado(pessoa2, usuario, chave, conteudo)
    else:
        print("Pessoa nao existe!")

    m.exibe_dados(pessoa2)
    # Criando uma key nível 2
    os.system("cls")
    
    m.exibe_dados(pessoa2)
    while True:
        nome_irmao = input("Nome irmão: ")
        if m.irmao_existe(pessoa2, nome_irmao):
            numero = len(pessoa2["Edson"]["irmaos"]) + 1
            chave = f"irmao{numero}"
            m.criando_irmao(pessoa2, usuario, chave, nome_irmao)
            m.exibe_dados(pessoa2)
        else:
            break






