import sys
import argparse

# Задача №1
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.


# eurkbyn = 2.91
# eurkusd = 1.11
# usdkbyn = 2.5


# while True:
#
#     input_amount = input('Введите сумму')
#
#     nn = int(input_amount) / usdkbyn
#     print('Ты ввёл', input_amount, 'USD')
#     print('конвертированная сума в USD = ', nn)
#
#     break


# Задача №2
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.

# usd = 78
# eur = 89
# chf = 86
# gpb = 107
# cny = 12
#
# while True:
#
#     input_amount = input('Введите сумму')
#
#     nn = int(input_amount) / usd
#     print('Ты ввёл', input_amount, 'RUB')
#
#     print('конвертированная сума в USD = ', nn)
#
#     break


# k_rub = {'USD': 78, 'EUR': 89, 'CHF': 86, 'GBP': 107, 'CNY': 12}
# amount = input('Введите сумму')
# if int(amount) >= 0:
#     print('Ты ввёл ', amount, 'RUB')
#     for k, v in k_rub.items():
#         r = int(amount) / int(v)
#         print('конвертированная сумма в ', k ,' = ', round(r, 2))


# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#   1. На вход обменнику вводишь количество денег int.
# 2. На выходе в консоль выводится отввет в таком виде:
# "Ты ввёл int (Валюта)"
# "конвертированная сумма в USD = int"
# "конвертированная сумма в EUR = int"
# "конвертированная сумма в CHF = int"
# "конвертированная сумма в GBP = int"
# "конвертированная сумма в CNY = int"
# 3. Скипт должен выдать сообщение
# "Введите положительное число." Если число меньше 0.
# "Вы ввели не число. Введите число." Если введены буквы.
# "Вы ввели пустое поле. Введите число." Если введено пустое значение.

# k_rub = {'USD': 78, 'EUR': 89, 'CHF': 86, 'GBP': 107, 'CNY': 12}
# amount = input('Введите сумму')
#
# if amount.strip() == '' or len(amount) == 0:
#     print("Вы ввели пустое поле. Введите число.")
#
# else:
#     try:
#         if int(amount) >= 0:
#             print('Ты ввёл ', amount, 'RUB')
#             for k, v in k_rub.items():
#                 r = int(amount) / int(v)
#                 print('конвертированная сумма в ', k ,' = ', round(r, 2))
#         elif int(amount) < 0:
#             print("Введите положительное число.")
#     except:
#         print("Вы ввели не число. Введите число.")


# Задача №4
# Обменник. Скрипт запускается в консоли и работает постоянно. Остановится нажатием ctrl+c.
#     1. Скрипт сначала выводит "Выберите валюту из ['USD','EUR','CHF','GBP','CNY']"
#     2. Пользователь вводит один из 5 вариантов ['USD','EUR','CHF','GBP','CNY']
#     3. Потом Скрипт выводит "Введите сумму"
#     4. Пользователь вводит сумму int
#     5. Скрипт выводит:
#             "Вы ввели сумму int и валюту "Валюта" "
#             "конвертированная сумма в "Валюта" = int"
#     6. Скипт должен выдать сообщение
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
#     7. После сообщеня об ошибке, скрипт должен автоматом вернуться к шагу 1.











k_usd = {'USD': 1, 'EUR': 0.87, 'CHF': 0.92, 'GBP': 0.73, 'CNY': 6.35}
k_eur = {'USD': 1.14, 'EUR': 1, 'CHF': 1.05, 'GBP': 0.84, 'CNY': 7.21}
k_chf = {'USD': 1.08, 'EUR': 0.95, 'CHF': 1, 'GBP': 0.80, 'CNY': 6.86}
k_gpb = {'USD': 1.36, 'EUR': 1.20, 'CHF': 1.26, 'GBP': 1, 'CNY': 6.62}
k_cny = {'USD': 0.16, 'EUR': 0.14, 'CHF': 0.15, 'GBP': 0.12, 'CNY': 1}
usd = 'USD'
eur = 'EUR'
chf = 'CHF'
gpb = 'GPB'
cny = 'CNY'
while True:
    currency = input("Выберите валюту из ['USD','EUR','CHF','GBP','CNY']")

    if currency.strip() == '' or len(currency) == 0:
        print("Вы ввели пустое поле. Введите число.")

    else:
        try:
            if currency == usd:
                summ = input("Введите сумму")
                if int(summ) >= 0:
                    print('Вы ввели сумму ', summ, 'и валюту ', usd)
                    for k, v in k_usd.items():
                        r = int(summ) * v
                        print('конвертированная сумма в ', k, ' = ', round(r, 2))
            if currency == eur:
                summ = input("Введите сумму")
                if int(summ) >= 0:
                    print('Вы ввели сумму ', summ, 'и валюту ', eur)
                    for k, v in k_eur.items():
                        r = int(summ) * v
                        print('конвертированная сумма в ', k, ' = ', round(r, 2))
            if currency == chf:
                summ = input("Введите сумму")
                if int(summ) >= 0:
                    print('Вы ввели сумму ', summ, 'и валюту ', chf)
                    for k, v in k_chf.items():
                        r = int(summ) * v
                        print('конвертированная сумма в ', k, ' = ', round(r, 2))
            if currency == gpb:
                summ = input("Введите сумму")
                if int(summ) >= 0:
                    print('Вы ввели сумму ', summ, 'и валюту ', gpb)
                    for k, v in k_gpb.items():
                        r = int(summ) * v
                        print('конвертированная сумма в ', k, ' = ', round(r, 2))
            if currency == cny:
                summ = input("Введите сумму")
                if int(summ) >= 0:
                    print('Вы ввели сумму ', summ, 'и валюту ', cny)
                    for k, v in k_cny.items():
                        r = int(summ) * v
                        print('конвертированная сумма в ', k, ' = ', round(r, 2))
            elif int(summ) < 0:
                print("Введите положительное число.")
        except:
            print("Вы ввели не число. Введите число.")





