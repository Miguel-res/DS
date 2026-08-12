def exibir_dicionario(a: dict)->None:
    print(f"Nome.....: {a['nome']}")
    print(f"Idade....: {a['idade']}")
    print(f"Curso....: {a['curso']}")
    return a

def pedir_dicionario(a: dict)->None:
    a['nome'] = input("qual o nome do aluno: ")
    a['idade'] = input("qual a idade do aluno: ")
    a['curso'] = input("qual o curso do aluno: ")

import os
os.system ("cls")
#dicionario = dict()
#dicionario = {}
#print(dicionario)

aluno = {
    # key : values
    'nome': 'edson',
    'idade': 51,
    'curso': 'DS'
}

#exibir_dicionario(aluno)

#pedir_dicionario()

aluno['idade'] = 30
print(aluno['idade'])