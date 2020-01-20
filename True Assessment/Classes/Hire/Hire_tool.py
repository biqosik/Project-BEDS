import datetime
import sqlite3

from Classes.Help.Availability_today import Availabililty
from Classes.Payment.Pay import Pay


class Hire_tool:

    @staticmethod
    def hiring(database, username):
        try:
            nothing = Availabililty.Check_availability_today(database)
            if nothing is False:
                return
            choice = int(input("Please choose available ID of an item: "))
            choice_name = str(input("Please write an name of an item: "))
            choose_item = "SELECT * FROM tool WHERE tool_name = ? AND n_id = ?"
            with sqlite3.connect(database) as db:
                assessment = db.cursor()
            date = datetime.date.today()
            assessment.execute(choose_item, [choice_name, choice])
            got = assessment.fetchall()
            if got:
                choice_1 = str(input(("""Are you sure you want to lend today this item? 
                Y for Yes, N for No: """)))
                choice_1.lower()
                if choice_1 == 'y' or 'yes':
                    Pay.payment(database, choice, username, choice_name, date)
                else:
                    return
            else:
                print ("That's not in available today")
                return

        except ValueError:
            print('Oops something went wrong !!!')
            return
