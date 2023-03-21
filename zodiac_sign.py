# user inputs their day and month of birth, program outputs their zodiac sign
# interface text in Portuguese

day = int(input("Informe o dia do nascimento: "))
month = input("Informe o mês de nascimento: ")

if month == 'março':
    if day < 21: signo = 'Peixes'
    else: signo = 'Áries'
elif month == 'abril':
    if day < 21: signo = 'Áries'
    else: signo = 'Touro'
elif month == 'maio':
    if day < 21: signo = 'Touro'
    else: signo = 'Gêmeos'
elif month == 'junho':
    if day < 21: signo = 'Gêmeos'
    else: signo = 'Câncer'
elif month == 'julho':
    if day < 23: signo = 'Câncer'
    else: signo = 'Leão'
elif month == 'agosto':
    if day < 23: signo = 'Leão'
    else: signo = 'Virgem'
elif month == 'setembro':
    if day < 23: signo = 'Virgem'
    else: signo = 'Libra'
elif month == 'outubro':
    if day < 23: signo = 'Libra'
    else: signo = 'Escorpião'
elif month == 'novembro':
    if day < 22: signo = 'Escorpião'
    else: signo = 'Sagitário'
elif month == 'dezembro':
    if day < 22: signo = 'Sagitário'
    else: signo = 'Capricórnio'
elif month == 'janeiro':
    if day < 21: signo = 'Capricórnio'
    else: signo = 'Aquário'
else:
    if day < 19: signo = 'Aquário'
    else: signo = 'Peixes'
    
print(f'Seu signo é {signo}.')