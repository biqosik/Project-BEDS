from Classes.Search_a_tool import Search_tool
from .UserToolMenu import UserTool_Menu
from .Booking_menu import Booking_menu
from .Return_Menu import Return_menu
from .Hire_Tool_Menu import Hiring_tool


class ToolMenu:
    def __init__(self, *args):
        self.username = args[0]
        self.database_path = args[1]
        self.tools_menu()

    def tools_menu(self):
        try:
            choice = int(input("""Please select menu:
            1: Search Tool
            2: Return a Tool
            3: Tool owner menu
            4: Booking menu
            5: Hire a Tool
            6: Exit Program: """))
            username = self.username
            database = self.database_path
            if choice == 1:
                Search_tool(database)
                self.tools_menu()
            elif choice == 2:
                Return_menu(database, username)
                self.tools_menu()
            elif choice == 3:
                UserTool_Menu(database, username)
                self.tools_menu()
            elif choice == 4:
                Booking_menu(database, username)
                self.tools_menu()
            elif choice == 5:
                Hiring_tool(database, username)
                self.tools_menu()
            elif choice == 6:
                print("See ya again!! :)")
                exit()
            else:
                print("Oops!!! Something went wrong !!")
                self.tools_menu()
        except ValueError as e:
            print(__name__, ':', "Tool_menu", " - ", e)
            print("Oops!!! Something went wrong !!")
            self.tools_menu()
