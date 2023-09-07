from models import NewsModel, Users
from view import Authenticate


if __name__ == '__main__':
    authorised_user = None
    print('hello world')
    while True:
        print('\n...........................')
        print('What do you want to do?')
        print('Choose Following OPtions:=')
        print('''
            L : To Login
            S: Sign Up
            R: Read News
            C: Create News
            U: Update News
            D: Delete News
        ''')
        option = input('>>>>  ')
        if option.upper() == 'L':
            print('----Login Page:----- ')
            print("Enter Your Credentials")
            print('--------------------')
            username = input('Username: ')
            password = input('Password: ')
            authenticate = Authenticate()
            authorised_user = authenticate.login(
                username=username, password=password)
            print(authorised_user)

        elif option.upper() == 'S':
            authorised = None
            print('\n----Sign Up Page:----- ')
            print("Enter Your Details")
            print('--------------------')
            username = input('Username: ')
            password = input('Password: ')
            user_instance = Users(username=username, password=password)
            user_instance.create()
            print('USER CREATED SUCCESSFULLY!!')

        elif option.upper() == 'R':
            print('\nFULL RETRIVE OR PARTIAL RETRIVE:')
            print('Full Retrive (F)')
            print('Pratial Retrive (P)')
            retrive_type = input('>>> ')
            if retrive_type.upper() == 'F':
                news_instance = NewsModel()
                data = news_instance.get()
                print('\n')
                print('\n')
                # print(data)
                for item in data:
                    for key, value in item.items():
                        print(f"{key} : {value}\n ")

                    print('-------------------------------------------')

            elif retrive_type.upper() == 'P':
                print('\n Choose News ID: ')
                try:
                    news_id = int(input('>>>> '))
                except Exception as e:
                    print(e)

                news_instance = NewsModel()
                data = news_instance.get(id=news_id)
                print('\n')
                print('\n')
                # print(data[0])
                for key, value in data[0].items():
                    print(f"{key} : {value}\n ")

            else:
                print("Invalid Retrive Type")

        elif option.upper() == 'C':
            print('\n------------')
            if authorised_user is None:
                print('Authentication Required !! Please Login First')
            else:
                authenticate = Authenticate()
                verified = authenticate.verify_user(user_id=authorised_user)
                if verified.get('user_id') is not None:
                    print('\n PROVIDE DATA TO CREATE NEWS: ')
                    title = input('Title:>>> ')
                    description = input('description:>>> ')
                    news = NewsModel(title=title, description=description)
                    news.create()

                    print('\nNews Created Successfully!!!')
                else:
                    authorised_user = None
                    print('\nUser Token Expired!! Please Login Again')

        elif option.upper() == 'D':
            print('\n------------')
            if authorised_user is None:
                print('Authentication Required !! Please Login First')
            else:
                authenticate = Authenticate()
                verified = authenticate.verify_user(user_id=authorised_user)
                if verified.get('user_id') is not None:
                    print('\n PROVIDE ID TO DELETE NEWS: ')
                    id = input('Id:>>> ')
                    news = NewsModel()
                    news.delete(id=id)
                    print('\nNews Deleted Successfully!!!')
                else:
                    authorised_user = None
                    print('\nUser Token Expired!! Please Login Again')

        elif option.upper() == 'U':
            print('\n------------')
            if authorised_user is None:
                print('Authentication Required !! Please Login First')
            else:
                authenticate = Authenticate()
                verified = authenticate.verify_user(user_id=authorised_user)
                if verified.get('user_id') is not None:
                    print('\n PROVIDE ID TO UPDATE: ')
                    id = input('Id:>>> ')
                    news = NewsModel()
                    news_item = news.get(id=id)

                    if len(news_item) > 0:
                        print(
                            '\nProvided Updated Items. SKip if you do not want to Update:\n')
                        updated_dict = {}
                        for key, value in news_item[0].items():
                            if key != 'id':
                                user_input = input(f'({value})\n{key}: \n>>> ')
                                if len(user_input.strip()) > 0:
                                    updated_dict[f'{key}'] = user_input
                        updated_dict['id'] =  news_item[0].get('id')
                        news.update(data = updated_dict)

                    else:
                        print(f'News with id : {id} is not available!!!')

                else:
                    authorised_user = None
                    print('\nUser Token Expired!! Please Login Again')
