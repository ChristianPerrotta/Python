# code and UI uses Portuguese instead of English
# changes animals from a "pasture" to another

vacas = ['vacas =', "branco", "preto", "marrom", "malhado"]
galinhas = ['galinhas =', "branca", "preta", "marrom", "amarela"]
porcos = ['porcos =', "rosa", "preto", "marrom", "malhado"]
cavalos = ['cavalos =', "branco", "preto", "marrom", "cinza"]

pasto1 = [vacas, galinhas, porcos, cavalos]
pasto2 = []

# movendo as listas
for _ in range(1, 4):
    pasto2.append(pasto1.pop())

print("Animais no pasto 2: ")
for a in pasto2:
    print(*a, sep=" ")
    
print("\nAnimais no pasto 1: ")
for a in pasto1:
    print(*a, sep=" ")