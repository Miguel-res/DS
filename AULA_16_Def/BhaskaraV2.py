import os
os.system("cls")
def calcular_delta(a:int, b:int, c:int) -> int:
        delta = (b**2)-4*a*c
    
        if delta < 0:
            print("delta deu negativo")
        else:
            return delta


a = int(input("digite o valor de a: "))
if a==0:
    print("isso não é uma equação de segundo grau")
b = int(input("digite o valor de b: "))
c = int(input("digite o valor de c: "))
calcular_delta(a, b, c)
print
