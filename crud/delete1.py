def delete_user(d_mail, users_storage, user_emails):
    if d_mail in user_emails:
        del users_storage[d_mail]
        print('Success! User', d_mail, 'deleted.')
    else:
        print('No user with email:', d_mail)


    print(users_storage)

