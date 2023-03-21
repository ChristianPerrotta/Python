# code and UI uses Portuguese instead of English
# checks whether a number is prime or not

n = int(input("Informe o número: "))
prime = True
if n <= 1:
    print("O número não é primo.")
    #coloquei 0, 1 e 2 aqui como casos especiais
elif n == 2:
    print("O número é primo.")
else:
    for x in range(2, n):
        if n%x == 0:
            prime = False
            break
    if prime == True:
        print("O número é primo.")
    else:
        print("O número não é primo.")