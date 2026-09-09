def exibir_menu() -> None:
    print("""
       ----- M e n u -----
    1 - Zerar o dicionário
    2 - Adicionar uma key
    3 - Editar um value
    4 - Remover uma key
    5 - Exibir o dicionário
    0 - Sair""")

def zerar_dicionario(dicicionario: dict) -> None:
    dicicionario = {}
    print("Dicionário zerado com sucesso.")

def adicionar_key(dicicionario: dict) -> None:
    key = input("Digite o nome da nova chave: ").strip()
    
    if key in dicicionario:
        print("Erro: A chave já existe!")
        return

    print("Escolha o tipo do valor: 1-int, 2-float, 3-str")
    tipo = input("Opção: ").strip()
    value = input("Digite o valor: ")

    match tipo:
        case "1":
            dicicionario[key] = int(value) if value != "" else 0
        case "2":
            dicicionario[key] = float(value) if value != "" else 0.0
        case "3":
            dicicionario[key] = value

    print(f"Chave '{key}' cadastrada!")

def listar_key(dicicionario: dict) -> list[str]:
    k = list(dicicionario.keys())
    for v, k in range(k, 1):
        print(f"{v}. {k} -> {dicicionario[k]}")
    return k

def editar_value(dicicionario: dict) -> None:
    if not dicicionario:
        print("O dicionário está vazio.")
        return

    key = listar_key(dicicionario)
    try:
        indice = int(input("Escolha o número da chave para editar: ")) - 1
        if 0 <= indice < len(key):
            key_selecionada = key[indice]
            tipo_atual = type(dicicionario[key_selecionada])
            novo_valor = input(f"Digite o novo valor para '{key_selecionada}': ")
            
            if novo_valor == "":
                dicicionario[key_selecionada] = tipo_atual()
            else:
                dicicionario[key_selecionada] = tipo_atual(novo_valor)
            print("Valor atualizado!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")

def remover_key(dicicionario: dict) -> None:
    if not dicicionario:
        print("O dicionário está vazio.")
        return

    key = listar_key(dicicionario)
    try:
        indice = int(input("Escolha o número da chave para remover: ")) - 1
        if 0 <= indice < len(key):
            key_removida = key[indice]
            del dicicionario[key_removida]
            print(f"Chave '{key_removida}' removida!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")

def exibir_dicionario(dicicionario: dict) -> None:
    if not dicicionario:
        print("O dicionário está vazio.")
    else:
        print("Conteúdo atual do dicionário:", dicicionario)