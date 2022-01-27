import sys
import argparse




eurkbyn = 2.91
eurkusd = 1.11
usdkbyn = 2.5


parser = argparse.ArgumentParser()
parser.add_argument('--exchange', type=str,)
parser.add_argument('--your', type=str, )
parser.add_argument('--amount', type=int, )

args = parser.parse_args()

you = args.your
exc = args.exchange
am = args.amount

if you == 'usd':
    if exc == 'byn':
        byn = am * usdkbyn
        print('Ты ввел', am, 'usd')
        print(("конвертированная сумма в byn = ", byn))
    elif exc == 'eur':
        eur = am / eurkusd
        print('Ты ввел', am, 'usd')
        print(("конвертированная сумма в eur = ", eur))


