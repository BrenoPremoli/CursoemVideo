valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 200
cont = 0
while True:
    if total >= ced:
        total -= ced
        cont += 1
    else:
        if cont > 0:
            print(f'São {cont} cédulas de R${ced}')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        cont = 0
        if total == 0:
            break
print('Obrigado pela preferência.')