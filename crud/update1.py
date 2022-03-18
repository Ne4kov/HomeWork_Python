def update_info(u_mail, users_storage, user_emails):

    #    Можно изменить только все параметры сразу, кроме Email:

    # if u_mail in user_emails:
    #     name = input('Name ')
    #     password = input('Password ')
    #     phone = input('Phone ')
    #     users_storage[u_mail] = {'name':name,
    #                         'password':password,
    #                         'phone':phone,
    #                         }
    #     print('User_email = ', u_mail, '\n', 'New user_info:', users_storage[u_mail])

    #    Можно изменить только все параметры сразу:

    # if u_mail in user_emails:
    #     del users_storage[u_mail]
    #     email = input('Enter new email ')
    #     name = input('Enter new name ')
    #     password = input('Enter new Password ')
    #     phone = input('Enter new Phone ')
    #     users_storage[email] = {'name': name,
    #                             'password': password,
    #                             'phone': phone,
    #                             }
    #     print('User_email = ', email, '\n', 'New user_info:', users_storage[email])
    #     print(users_storage)


                #Можно выбрать какой параметр изменить:


    if u_mail in user_emails:
        par = input('Enter update parameter: name or password, or phone, or email ')
        if par == 'name':
            name = input('Enter new Name: ')
            users_storage_u = {'name': name}
            users_storage[u_mail].update(users_storage_u)
            print('Succses! username', u_mail, 'changed to', name)
            print(users_storage)
        # elif par == 'Email':
        #     email = input('Enter new Email: ')
        #     abc = {}
        #     u_stor = {}
        #     w = []
        #     abc.update(users_storage[u_mail])
        #     for k, v in abc.items():
        #         w.append(v)
        #     name = w[0]
        #     password = w[1]
        #     phone = w[2]
        #     u_stor[email] = {'name': name, 'password': password, 'phone': phone}
        #     del users_storage[u_mail]
        #     users_storage.update(u_stor)
        #     print(users_storage)
        elif par == 'email':
            email = input('Enter new Email: ')
            users_storage[email] = users_storage[u_mail]
            del users_storage[u_mail]
            print(users_storage)
        elif par == 'password':
            password = input('Enter new Name: ')
            users_storage_u = {'password': password}
            users_storage[u_mail].update(users_storage_u)
            print('Succses! password', u_mail, 'changed!')
            print(users_storage)
        elif par == 'phone':
            phone = input('Enter new Phone: ')
            users_storage_u = {'phone': phone}
            users_storage[u_mail].update(users_storage_u)
            print('Succses! phone', u_mail, 'changed!')
            print(users_storage)
        else:
            print('Invalid parameter.')
    else:
        print()




