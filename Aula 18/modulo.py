


def exibir_menu() -> None:
    print("""
|======== M e n u ========|
| 0 - Encerrar programa   |
| 1 - Adicionar Dado      |
| 2 - Adicionar irmao     |
| 3 - Exibir dicionario   |
| 4 - Reiniciar Familias  |
|=========================|
""")

def exibe_dados(p: dict) -> None:
    for k1, v1 in p.items():
        print(f"Nome: {k1}")
        for k2, v2 in v1.items():
            if isinstance(v2, dict): # se for um dicionario
                # tratar como dicionario - Particionar as informacoes
                print(f"\t{k2}")
                for k3, v3 in v2.items():
                    print(f"\t\t{k3}: {v3}")
            else:
                # tratar como um outro dado (simples)
                print(f"\t{k2}: {v2}")
def key_existe(p: dict, k: str) -> bool:
    return k in p

def irmao_existe(p:dict, ni: str) -> bool:
    return ni not in p

def criando_dado(p: dict, u: str, k: str, v: str) -> dict:
    p[u][k] = v

def criando_irmao(p: dict, u: str, k: str, ni: str) -> None:
    p[u]["irmaos"][k] = ni
