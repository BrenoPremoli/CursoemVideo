cont = s = 0
while True:
    n = int(input('Digite um valor [999 para PARAR]: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'A soma dos {cont} valores foi {s}.')