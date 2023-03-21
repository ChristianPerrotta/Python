# code and UI uses Portuguese instead of English
# changes animals from a "pasture" to another

def lines (n):
    for line in range(1, n + 1):
        for num in range(1, line + 1):
            print(num, end=' ')
        print('\n')

num = int(input("Informe um número inteiro positivo: "))
lines(num)