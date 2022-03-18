import sys
import argparse

from create1 import create_user
from update1 import update_info
from read1 import user_info, all_users_info
from delete1 import delete_user


user_emails = []
users_storage = {}

while True:
    act = input('Please enter create or read, or update, or delete ')

    if act == 'create':
        print('action = ', act)

        email = input('Email ')
        name = input('Name ')
        password = input('Password ')
        phone = input('Phone ')

        create_user(email,
                    name,
                    password,
                    phone,
                    user_emails,
                    users_storage)
        print('user_emails = ', user_emails)
        print('users_storage = ', users_storage)

    elif act == 'read_all':
        print('action = ', act)
        all_users_info(users_storage)

    elif act == 'read_user':
        print('action = ', act)
        user_e = input('Enter user email ')

        message = user_info(user_e, user_emails, users_storage)

    elif act == 'update':
        print('action = ', act)
        u_mail = input('enter the email of the user you want to update: ')
        update_info(u_mail, users_storage, user_emails)

    elif act == 'delete':
        print('action = ', act)
        d_mail = input('Enter email to be deleted: ')
        delete_user(d_mail, users_storage, user_emails)

        print()
    else:
        print('Please enter create or read, or update, or delete ')