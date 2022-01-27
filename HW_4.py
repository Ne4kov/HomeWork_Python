import sys
import argparse




eurkbyn = 2.91
eurkusd = 1.11
usdkbyn = 2.5



parser = argparse.ArgumentParser()
parser.add_argument('--num1', type=int)
parser.add_argument('--num2', type=int)
# parser.add_argument('--action', type=str)
#
args = parser.parse_args()
usd = args.num1 / usdkbyn
print('Ты ввел', args.num1, 'BYN')
print("конвертированная сумма в USD = ", usd)