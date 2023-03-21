# code and UI uses Portuguese instead of English
# calculates the average distance of an given asteroid from Earth

ast = {}
while (True):
    nome = input("Digite o nome do asteroide: ")
    d1 = int(input("Informe as últimas 5 distâncias do asteroide à Terra, em km.\nDistância 1: "))
    d2 = int(input("Distância 2: "))
    d3 = int(input("Distância 3: "))
    d4 = int(input("Distância 4: "))
    d5 = int(input("Distância 5: "))
    ast[nome] = [d1, d2, d3, d4, d5]
    continuar = input("Registrar outro asteroide? (S/N) ")
    if continuar == 'N':
        break

for a in ast.keys():
    media = sum(ast[a])/5
    print(f"A distância média do asteroide {a} à Terra é {media} km.")