from Classes.Help.Availability_today import Availabililty
from Classes.Hire.Take_tool import Take_paid
from Classes.Hire.Hire_tool import Hire_tool


class Hiring_tool:
    def __init__(self, *args):
        self.database = args[0]
        self.username = args[1]
        self.hire_tool()

    def hire_tool(self):
        try:
            choice = int(input("""Please select menu: 
            1.Check for today availability tools
            2.Take your already payed tool
            3.Hire tools that are available today
            4.Exit to menu: """))
            if choice == 1:
                Availabililty.Check_availability_today(self.database)
                self.hire_tool()
            elif choice == 2:
                Take_paid.paid_tools(self.database, self.username)
                self.hire_tool()
            elif choice == 3:
                Hire_tool.hiring(self.database, self.username)
                self.hire_tool()
            elif choice == 4:
                return
            else:
                print("Oops something went wrong")
                self.hire_tool()
        except ValueError as e:
            print(__name__, ': Hire Menu - ', e)
