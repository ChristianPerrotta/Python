from calculator_module import *

print("-"*10)
print("Esta é uma calculadora básica.")
print("-"*10)

while(True):
    n1 = float(input("Esolha o primeiro número da operação: "))
    n2 = float(input("Esolha o segundo número da operação: "))
    print("Escolha a operação a ser feita:")
    op = input("[1] Adição\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n[5] Sair\n")
    
    match op:
        case "1":
            result = ad(n1, n2)
        case "2":
            result = subtr(n1, n2)
        case "3":
            result = mult(n1, n2)
        case "4":
            result = div(n1, n2)
        case "5":
            break
        case _:
            print("Operação inválida")
            continue
    
    print(f"O resultado da operação é {result}.")