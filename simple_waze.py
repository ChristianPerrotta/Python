# code and UI uses Portuguese instead of English
# calculates total distance run

dist = 0
dir = input('Informe a direção ("parar" finaliza): ')

while (dir != "parar"):
    dist += 0.1
    dir = input('Informe a direção ("parar" finaliza): ')

print(f"Ao todo, foram percorridos {dist} km.")