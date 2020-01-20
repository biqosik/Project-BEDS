from Classes.User_Tools.Show_user_tools import Show_user_tools
from Classes.User_Tools.Create_tool import CreateTool
from Classes.User_Tools.Delete_tool import DeleteTool


class UserTool_Menu:
    def __init__(self, *args):
        self.database = args[0]
        self.username = args[1]
        self.user_tool_menu()

    def user_tool_menu(self):
        database_path = self.database
        username = self.username
        try:
            choice = int(input("""Please select an option:
                1: Show currently active username tools
                2: Create a new tool
                3: Delete already existing tool
                4: Go back to Menu: """))
            if choice == 1:
                Show_user_tools(database_path, username)
                self.user_tool_menu()
            elif choice == 2:
                CreateTool(database_path, username)
                self.user_tool_menu()
            elif choice == 3:
                DeleteTool(database_path, username)
                self.user_tool_menu()
            elif choice == 4:
                return
            else:
                print("Oops something went wrong")
                self.user_tool_menu()
        except ValueError:
            print("Oops something went wrong !!!")
            self.user_tool_menu()
