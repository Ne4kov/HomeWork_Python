import random
from faker import Faker

# Написать скрипт который в создаст список целых чисел.

# ll = []
# for i in range(0, 100):
#     ll.append(i)
# print(ll)


# Написать скрипт который в создаст список целых чётных чисел.

# ll = []
# for i in range(1,100):
#     if i%2 == 0:
#         ll.append(i)
# print(ll)


# или тоже но короче

# ll = [i for i in range(0, 100) if i % 2 == 0]
# print(ll)


# или

# a = [i for i in range(2,100,2)]
# print(a)




# Написать скрипт который в создаст список целых нечётных чисел.

# ll = []
# for i in range(1,100):
#     if i%2 == 1:
#         ll.append(i)
# print(ll)


# Написать скрипт который из списка целых чисел выведет чётные числа.

# ll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,]
# aa = []
# for i in ll:
#     if i%2 == 0:
#         aa.append(i)
# print(aa)



# Написать скрипт который из списка целых чисел выведет нечётные числа.

# ll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,]
# aa = []
# for i in ll:
#     if i%2 == 1:
#         aa.append(i)
# print(aa)


# Написать скрипт который из списка целых чисел выведет чётные числа которые делятся на 5 без остатка.

# ll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,]
# aa = []
# for i in ll:
#     if i%5 == 0:
#         if i%2 == 0:
#             aa.append(i)
#
# print(aa)

# Написать скрипт который из списка целых чисел выведет количество  чётных чисел которые делятся на 5 без остатка.

# ll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,]
# aa = []
# for i in ll:
#     if i%5 == 0:
#         if i%2 == 0:
#             aa.append(i)
#
# print(len(aa))


# Написать скрипт который в создаст список целых рандомных чисел.

# q=[]
# for i in range(0,100):
#     zxc = random.randint(1, 20)
#     q.append(zxc)
# print(q)


# Написать функцию которая, получив на вход любой из выше созданных списков, разобьёт его на списки по 5 элементов.

# ll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
#
# def gener(lst, n):
#     for i in range(0, len(lst), n):
#         yield lst[i:i+n]
#
# print(list(gener(ll, 5)))


# Написать функцию которая, получив на вход список целых чисел, вернёт 2 списка, список чётных и список нечётных чисел.

# ll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
#
# def even_odd(list):
#     even = []
#     odd = []
#     for i in list:
#         if i%2==0:
#             even.append(i)
#         if i%2==1:
#             odd.append(i)
#     print('even = ', even, 'odd = ',odd)
#
# even_odd(ll)



# Написать скрипт который сгенерирует список под названием 5_stars из списков по 5 элементов целых чисел.

# _5_stars = [[i * random.randint(1, 20) for i in range(1, 6)] for j in range(1, 6)]
#
# print(_5_stars)

# Написать скрипт который выведет список из сумм каждого внутреннего списка из  5_stars

# _5_stars = [[i * random.randint(1, 10) for i in range(1, 6)] for j in range(1, 6)]
# a = []
#
# for i in range(len(_5_stars)):
#     if i < 5:
#         b = sum((_5_stars)[i])
#         a.append(b)
#
# print(a)

# Написать функцию которая на вход получает список 5_stars,а вернёт 2 списка.
# В одном списке внутренние списки из 5_stars сумма чисел которых >= 100,
# а другой сумма чисел которых < 100.
# Если какого-то списка не получится, то вместо него вернуть текст “No lists”



# def lists(list):
#     a = []
#     c = []
#     for i in range(len(_5_stars)):
#         if i < 5:
#             b = sum((_5_stars)[i])
#             if b >= 100:
#                 a.append((list)[i])
#             elif b < 100:
#                 c.append((list)[i])
#             else:
#                 print('No lists')
#     print('>= 100:', a, '   < 100:', c)
#
#
# _5_stars = [[i * random.randint(1, 10) for i in range(1, 6)] for j in range(1, 6)]
#
#
# lists(_5_stars)


# Написать функцию которая получив на вход ваш возраст,
# выведет вам через какой срок вы сумеете отложить 10 000$, 20 000$, 30 000$, 50 000$, 100 000$ в кубышку.

# def cubyshka(old):
#     dd = {'10 000$': 25 , '20 000$': 30, '30 000$': 35, '50 000$': 40, '60 000$': 50}
#     if 0 <= old < 20:
#         print('Вы еще слишком молоды))')
#     elif 20 <= old < 50:
#         for k, v in dd.items():
#             b = v-old
#             if b >=0:
#                 print('Вы сможете отложить ', k, 'в кубышку через ', b, 'лет/года')
#     else:
#         print('Поздняк метаться, пора тратить))')
#
# cubyshka(49)


# Написать функцию которая получив на вход стартовую ЗП Junior QA и количество лет стажа
# выведет в консоль прогресс роста ЗП по каждому году из введенного количества лет стажа.
# Внутри функция учитывает дорожную карту развития скилов QA и список, полезных для компании, активностей
# которые может делать QA. Free implementation of function body logic


# def zp(start_zp, stasch):
#
#     skills = ['management', 'mentoring', 'postman', 'python', 'sql']
#
#
#     if stasch > 0:
#         for i in range(1, stasch+1):
#             k = i * 0.4
#             zp = round((start_zp + start_zp * k), 0)
#             increase = random.randint(100, 1000)
#             itog = increase + zp
#             r = skills[random.randint(0, 4)]
#
#
#             print(f'After {i} years, your salary will be {zp} USD, and increase for {r}:{increase} USD. Total: {itog} USD')
#
# zp(500, 10)



# Написать скрипт который сгенерирует список имён пользователей. Список имён вывести в консоль.

# def names_list(leng):
#  f = Faker()
#  names = []
#  for i in range(leng):
#       names.append(f.name())
#  return names
#
# print(names_list(70))


# Написать скрипт который сгенерирует список имён файлов. К каждому имени  файла надо прикрепить номер итерации цикла как порядковый номер.

# def file_names_list(len):
#  f = Faker()
#  f_names = []
#
#  for i in range(len):
#   f_names.append(f.file_name())
#
#  return f_names
#
# f_n = file_names_list(70)
#
# k = 0
# for n in range(len(f_n)):
#     k +=1
#     f_n[n] = str(k) + ". " + f_n[n]
#
# print(f_n)

# Написать скрипт который сгенерирует список списков.
# Каждый элемент списка это список в котором 0-й элемент - это имя пользователя, а 1-й - элемент это дата регистрации.


# def names_data_list(len):
#
#     f = Faker()
#     n_date = []
#     for i in range(len):
#         n_date.append([f.user_name(), str(f.date_time_this_century())])
#     return n_date
#
# print(names_data_list(2))

# Написать скрипт который сгенерирует список Employees списков . Каждый элемент списка - это список в котором:
# 0-й - элемент - это имя пользователя,
# 1-й - элемент - это логин,
# 2-й - элемент - это пароль,
# 3-й - элемент - это email (email тоже генерировать),
# 4-й - элемент - это дата регистрации

# def data_list(len):
#
#     f = Faker()
#     employees = []
#     for i in range(len):
#         employees.append(([f.name(), f.user_name(), f.password(), f.email(),str(f.date_time_this_century())]))
#     return employees
#
# print(data_list(10))



# Написать скрипт который сгенерирует список family списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - семейный статус (True, False - генерировать рандомно)

# def data_family(len):
#     f = Faker()
#     family = []
#     for i in range(len):
#         family.append(([f.user_name(), f.name(), bool(random.randint(0, 1))]))
#     return family
#
# print(data_family(10))


# Написать скрипт который сгенерирует список gender списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - гендер (1-м, 0-ж)


# def gender(len):
#     f = Faker()
#     gen = []
#     for i in range(len):
#         rand = random.randint(0, 1)
#         if rand == 1:
#             gen.append([f.user_name(), f.name_male(), rand])
#         else:
#             gen.append([f.user_name(), f.name_female(), rand])
#     return gen
#
# print(gender(10))


# Написать скрипт который сгенерирует список salary списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - зарплата (генерироовать от 300$ до 5000$)

#Для выполнения последнего задания, добавлю в этот список гендер

# def salary_data(len):
#     f = Faker()
#     salary = []
#     for i in range(len):
#         gend = random.randint(0, 1)
#         if gend == 1:
#             salary.append([f.user_name(), f.name_female(), random.randint(300, 5000), gend])
#         else:
#             salary.append([f.user_name(), f.name_male(), random.randint(300, 5000), gend])
#     return salary, gend
#
# print(salary_data(10))


# Написать скрипт который создаст список мён работников из salary у которых ЗП от 1500$ до 3000$


# def salary_1500_3000(len):
#     f = Faker()
#     salary = []
#     for i in range(len):
#         salary.append(([f.user_name(), f.name(), random.randint(300, 5000)]))
#     return salary
#
#
# salary_1 = salary_1500_3000(70)
# print(salary_1)
# name = []
# for n in salary_1:
#     if type(n) == list:
#         for k in n:
#             if type(k) == int:
#                 if 1500 <= k < 3000:
#                     name.append(n[1])
# print(name)


# Написать скрипт который создаст список имён мужчин из gender.

# def gender(len):
#     f = Faker()
#     gen = []
#     for i in range(len):
#         rand = random.randint(0, 1)
#         if rand == 1:
#             gen.append([f.user_name(), f.name_male(), rand])
#         else:
#             gen.append([f.user_name(), f.name_female(), rand])
#     return gen
#
# lists = gender(70)
#
# male_list = []
# for i in lists:
#     if i[2] == 1:
#         male_list.append(i[1])
# print(male_list)


# Написать скрипт который создаст список имён женщин из gender.

# def gender(len):
#     f = Faker()
#     gen = []
#     for i in range(len):
#         rand = random.randint(0, 1)
#         if rand == 1:
#             gen.append([f.user_name(), f.name_male(), rand])
#         else:
#             gen.append([f.user_name(), f.name_female(), rand])
#     return gen
#
# lists = gender(70)
#
# female_list = []
# for i in lists:
#     if i[2] == 0:
#         female_list.append(i[1])
# print(female_list)


# Написать скрипт который создаст список имён неженатых мужчин из family.

# def data_family(len):
#     f = Faker()
#     family = []
#     for i in range(len):
#         gend = random.randint(0, 1) # нужно добавть гендер в список
#         if gend == 1:
#             family.append(([f.user_name(), f.name_male(), gend, bool(random.randint(0, 1))]))
#         else:
#             family.append(([f.user_name(), f.name_female(), gend, bool(random.randint(0, 1))]))
#     return family
#
# lists = data_family(70)
# print(lists)
# not_married = []
# for i in lists:
#     if i[3] == False and i[2] == 1:
#         not_married.append(i[1])
# print(not_married)



# Написать скрипт который создаст список имён незамужних женщин из family.


# def data_family(len):
#     f = Faker()
#     family = []
#     for i in range(len):
#         gend = random.randint(0, 1) # нужно добавть гендер в список
#         if gend == 1:
#             family.append(([f.user_name(), f.name_male(), gend, bool(random.randint(0, 1))]))
#         else:
#             family.append(([f.user_name(), f.name_female(), gend, bool(random.randint(0, 1))]))
#     return family
#
# lists = data_family(70)
# print(lists)
# not_married = []
# for i in lists:
#     if i[3] == False and i[2] == 0:
#         not_married.append(i[1])
# print(not_married)


# Написать скрипт который создаст список имён неженатых мужчин с ЗП больше или равной 1500$. Используйте Employees, family, gender, salary. Реализуйте как скрипт, без функций


# f = Faker()
# family = []
# for i in range(70):
#     gend = random.randint(0, 1) # нужно добавть гендер, и зарплату в список
#     if gend == 1:
#         family.append(([f.user_name(), f.name_male(), gend, bool(random.randint(0, 1)), random.randint(300, 5000)]))
#     else:
#         family.append(([f.user_name(), f.name_female(), gend, bool(random.randint(0, 1)), random.randint(300, 5000)]))
# print(family)
# list_1 = []
# for n in family:
#     if n[2] == 1 and n[3] == False and n[4] >= 1500:
#         list_1.append(n[1])
#
# print(list_1)


# Реализуйте последний пункт через через функции.

def salary_data(len):
    f = Faker()
    salary = []
    for i in range(len):
        gend = random.randint(0, 1)
        if gend == 1:
            salary.append([f.user_name(), f.name_female(), random.randint(300, 5000), gend])
        else:
            salary.append([f.user_name(), f.name_male(), random.randint(300, 5000), gend])
    return salary



def data_family(len):
    f = Faker()
    family = []
    for i in range(len):
        gend = random.randint(0, 1) # нужно добавть гендер в список
        if gend == 1:
            family.append(([f.user_name(), f.name_male(), gend, bool(random.randint(0, 1))]))
        else:
            family.append(([f.user_name(), f.name_female(), gend, bool(random.randint(0, 1))]))
    return family


def mega_list(len):

    list_2 = salary_data(len)
    list_3 = data_family(len)


    male_not_marr_list = []
    male_1500 = []

    for i in list_2:
        if i[3] == 1 and i[2] >= 1500:
            male_1500.append(i[1])

    for k in list_3:
        if k[2] == 1 and k[3] == False:
            male_not_marr_list.append(k[1])

    last_list = male_1500 + male_not_marr_list

    return last_list



print(mega_list(70))