# code and UI uses Portuguese instead of English
# calculates total water waste from water flow rate and duration of leakage

qt = int(input("Informe o número de vazamentos: "))
litros = 0
for i in range(qt):
    vazao = float(input(f"Quantos litros por hora no vazamento {i+1}? "))
    horas = float(input(f"Por quantas horas ocorreu o vazamento {i+1}? "))
    litros += vazao*horas

print(f"O total de água desperdiçada foi de {litros} litros.")