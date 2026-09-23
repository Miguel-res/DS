
def exibir_menu() -> None:
    print("""
|====== M E N U ======|
| 1 - Gravar linhas   |
| 2 - Listar arquivo  |
| 3 - Pesquisar nome  |
|=====================|
""")
def exibir_submenu() -> None:
    print("""
a. Nome
b. Idade
c. Altura
""")

def exibir_subsubmenu() -> None:
    print("""
a. Simples
b. maior ou igual
c. Menor ou igual
d. Entre
""")


def gravar_arquivo(na: str) -> None:
    with open(na, "a", encoding="utf-8") as arquivo:
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

def listar_arquivo(na: str) -> None:
    with open(na, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            # "Edson,45,1.9"
            lista = linha.split(',')
            #             0       1     2
            # lista = ["Edson", "45", "1.9"]
            print(30 * '-')
            print(f"Nome.........: {lista[0]}")
            print(f"Idade........: {lista[1]}")
            print(f"Altura.......: {lista[2]}")

def exibir_linha(l: list) -> None:
    print("Registro:" + 30 * '-' )
    print(f"Nome.........: {l[0]}")
    print(f"Idade........: {l[1]}")
    print(f"Altura.......: {l[2]}")
    print(30 * '-')

def pesquisar_nome(na: str, n: str) -> None:
    with open(na, "r", encoding="utf-8") as arquivo:
        encontrou = False
        for linha in arquivo:
            lista = linha.split(',')
            if lista[0] == n:
                exibir_linha(lista)
                encontrou = True
        return encontrou

def pesquisar_idade_simples(na: str, id: int) -> None:
    with open(na, "r", encoding="utf-8") as arquivo:
        encontrou = False
        for linha in arquivo:
            lista = linha.split(',')
            if lista[1] == id:
                exibir_linha(lista)
                encontrou = True
        return encontrou

def pesquisar_idade_maior(na: str, id: int) -> None:
    with open(na, "r", encoding="utf-8") as arquivo:
        encontrou = False
        for linha in arquivo:
            lista = linha.split(',')
            if lista[1] >= id:
                exibir_linha(lista)
                encontrou = True
        return encontrou

def pesquisar_idade_menor(na: str, id: int) -> None:
    with open(na, "r", encoding="utf-8") as arquivo:
        encontrou = False
        for linha in arquivo:
            lista = linha.split(',')
            if lista[1] <= id:
                exibir_linha(lista)
                encontrou = True
        return encontrou

def pesquisar_idade_entre(na: str, ini: int, fim: int) -> None:
    with open(na, "r", encoding="utf-8") as arquivo:
        encontrou = False
        for linha in arquivo:
            lista = linha.split(',')
            if lista[1] >= ini and lista[1] <= fim:
                exibir_linha(lista)
                encontrou = True
        return encontrou

def pesquisar_altura_simples(na: str, alt: float) -> None:
    with open(na, "r", encoding="utf-8") as arquivo:
        encontrou = False
        for linha in arquivo:
            lista = linha.split(',')
            if lista[2] == alt:
                exibir_linha(lista)
                encontrou = True
        return encontrou

def pesquisar_altura_maior(na: str, alt: float) -> None:
    with open(na, "r", encoding="utf-8") as arquivo:
        encontrou = False
        for linha in arquivo:
            lista = linha.split(',')
            if lista[2] >= alt:
                exibir_linha(lista)
                encontrou = True
        return encontrou

def pesquisar_altura_menor(na: str, alt: float) -> None:
    with open(na, "r", encoding="utf-8") as arquivo:
        encontrou = False
        for linha in arquivo:
            lista = linha.split(',')
            if lista[2] <= alt:
                exibir_linha(lista)
                encontrou = True
        return encontrou

def pesquisar_altura_entre(na: str, ini: float, fim: float) -> None:
    with open(na, "r", encoding="utf-8") as arquivo:
        encontrou = False
        for linha in arquivo:
            lista = linha.split(',')
            if lista[2] >= ini and lista[2] <= fim:
                exibir_linha(lista)
                encontrou = True
        return encontrou        