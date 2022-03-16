import re

usd = 'USD'
eur = 'EUR'
chf = 'CHF'
gpb = 'GPB'
cny = 'CNY'

def cyrren_f(k_usd, us):
    while True:
        a = input('Введите сумму')
        comp = re.compile('-')
        m = comp.match(a)
        if m:
            print('вы ввели отрицательное число')
            continue
        elif len(a) == 0:
            print('Вы ничего не ввели')
            continue
        elif not a.isnumeric():
            print('это не число, можно число, плеаз?')
            continue
        elif int(a) >= 0:
            print('Вы ввели сумму ', a, 'и валюту ', us)
            for k, v in k_usd.items():
                r = int(a) * v
                print('конвертированная сумма в ', k, ' = ', round(r, 2))
        break


