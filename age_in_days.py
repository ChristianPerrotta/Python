# code and UI uses Portuguese instead of English
# user enters current age with years, months and days
# program replies with current age in days
# does not consider leap years
# two approaches for user input

# considerando que a pessoa vá digitar as três informações separadamente:
anos = int(input("Informe quantos anos você tem: "))
meses = int(input("Informe quantos meses você tem, além dos anos: "))
dias = int(input("Informe quantos dias você tem, além dos anos e meses: "))
idadeEmDias = (anos*365) + (meses*30) + dias
print(f"Você já viveu {idadeEmDias} dias.")

# considerando que a pessoa vá digitar as três informações de uma vez só, com espaços,
# estritamente como está na entrada do programa, no comando:
anos, meses, dias = input("Informe sua idade em anos, meses e dias: ").split()
idadeEmDias = (int(anos)*365) + (int(meses)*30) + int(dias)
print(f"Você já viveu {idadeEmDias} dias.")
