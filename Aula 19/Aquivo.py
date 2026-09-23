import os
os.system("cls")
import Modulo as M

nome_arquivo = "Arquivo.txt"
while True:
    M.exibir_menu()
    escolha = input("Escolha uma opção: ")
    match escolha:
            case '1':
                M.gravar_arquivo(nome_arquivo)
            case '2':
                M.listar_arquivo(nome_arquivo)
                with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
                    for linha in arquivo:
                        # "Edson,45,1.9"
                        lista = linha.split(',')
                        #             0       1     2
                        # lista = ["Edson", "45", "1.9"]
                        print(30 * '-')
                        print(f"Nome.........: {lista[0]}")
                        print(f"Idade........: {lista[1]}")
                        print(f"Altura.......: {lista[2]}")
            case '3':
                M.exibir_submenu()
                escolha2 = input("Escolha como quer procurar: ").split
                match escolha2:
                    case 'a' | 'A':
                        nome_procurado = input("Quem quer procurar: ")
                        if not M.pesquisar_nome(nome_arquivo, nome_procurado):
                            print(f"O nome '{nome_procurado}' não existe no arquivo")
                    case 'b' | 'B':
                        M.exibir_subsubmenu()
                        escolha3 = input("Escolha como quer procurar: ")
                        match escolha3:
                            case 'a' | 'A':
                                idade = int(input("Qual a idade: "))
                                M.pesquisar_idade_simples(nome_arquivo, idade)
                            case 'b' | 'B':
                                idade = int(input("Qual a idade: "))
                                M.pesquisar_idade_maior(nome_arquivo, idade)
                            case 'c' | 'C':
                                idade = int(input("Qual a idade: "))
                                M.pesquisar_idade_menor(nome_arquivo, idade)
                            case 'd' | 'D':
                                inicio_ida = int(input("Qual a idade: "))
                                fim_ida = int(input("Qual a idade: "))
                                M.pesquisar_idade_entre(nome_arquivo, inicio_ida, fim_ida)
                    case 'c' | 'C':
                        M.exibir_subsubmenu()
                        escolha3 = input("Escolha como quer procurar: ")
                        match escolha3:
                            case 'a' | 'A':
                                altura = float(input("Qual a altura"))
                                M.pesquisar_altura_simples(nome_arquivo, altura)
                            case 'b' | 'B':
                                altura = float(input("Qual a altura"))
                                M.pesquisar_altura_maior(nome_arquivo, altura)
                            case 'c' | 'C':
                                altura = float(input("Qual a altura"))
                                M.pesquisar_altura_menor(nome_arquivo, altura)
                            case 'd' | 'D':
                                inicio_alt = float(input("Qual a altura"))
                                fim_alt = float(input("Qual a altura"))
                                M.pesquisar_altura_entre(nome_arquivo, inicio_alt, fim_alt)
                    