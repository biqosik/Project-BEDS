from Classes.Login.Login import Login
from Classes.Login.Create_acc import Create_account


class Menu:
    def __init__(self, *args):
        self.database_path = args[0]

    def first_menu(self):
        # /// User input a choice 1 or 2, and program checks if 1 than go to login if 2 than go to create account if
        # something else than print error and going back to menu function again///
        choice = int(input("""Press to continue. 
        1:Login 
        2:Create Account
        3:Exit program: """))
        database_path = self.database_path
        try:
            if choice == 1:
                login = Login(database_path)
                username = login.login_in()
                return username
            elif choice == 2:
                create = Create_account(database_path)
                username_n = create.create_acc()
                return username_n
            elif choice == 3:
                exit()
            else:
                print("Oops something went wrong")
                self.first_menu()

        except ValueError as e:
            print(__name__, ':', "MainMenu", " - ", e)
            print("Oops!!! Something went wrong !!")
            self.first_menu()
