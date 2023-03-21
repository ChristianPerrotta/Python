# code and UI uses Portuguese instead of English
# calculates area of a rectangle, with two possible approaches for user input

# considerando que a pessoa vá digitar as duas informações separadamente:
base = int(input("Informe a base do retângulo: "))
altura = int(input("Informe a altura do retângulo: "))
print(f"A área do retângulo vale {base*altura} unidades de área.")

# considerando que a pessoa vá digitar as duas informações de uma vez só, com espaços,#estritamente como está na entrada do programa, no comando:
base, altura = input("Informe a base e a altura do retângulo: ").split()
print(f"A área do retângulo vale {int(base)*int(altura)} unidades de área.")