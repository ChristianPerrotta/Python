# code and UI uses Portuguese instead of English
# prints all the prime numbers between two given integers

n1 = int(input("Informe o primeiro número (menor): "))
n2 = int(input("Informe o segundo número (maior): "))
print(f"Os números primos entre {n1} e {n2} são:")
for num in range (n1, n2 + 1):
    if num > 1:
        for i in range (2, num):
            if (num%i) == 0:
                break
        else: print(num, end=" ")