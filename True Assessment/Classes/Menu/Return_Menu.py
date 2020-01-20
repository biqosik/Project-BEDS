from Classes.Return.Return_Item import Returning
from Classes.Return.Problem_return import problems


class Return_menu:
    def __init__(self, database, username):
        self.database = database
        self.username = username
        self.returning_menu()

    def returning_menu(self):
        try:
            choice = int(input("""Please provide an option 
            1. Return a Tool
            2. Problem with returning tool
            3. Return to Menu: """))
            if choice == 1:
                Returning.return_item(self.database, self.username)
            elif choice == 2:
                problems()
            elif choice == 3:
                return
            else:
                print("Oops something went wrong")
                self.returning_menu()
        except ValueError:
            print("Oops something went wrong")
            return
