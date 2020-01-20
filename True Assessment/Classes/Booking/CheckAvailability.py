import sqlite3
from Classes.Help.DateValue import Checking_value


class Check_Availability:

    def __init__(self, *args):
        self.database = args[0]
        self.checking_val()

    def checking_val(self):
        date1 = Checking_value.checking_value()
        if not date1:
            return
        with sqlite3.connect(self.database) as db:
            assessment = db.cursor()
        find_date = "SELECT * FROM tool_availability where lend_date = ?"
        assessment.execute(find_date,[date1])
        user = assessment.fetchall()
        if user:
            print("Those items are already booked on this date: ")
            for row in user:
                print(" ID = ", row[0],
                      " Owner =", row[1],
                      " Renting Username =", row[2],
                      " Item =", row[3],
                      " Date =", row[4], )
        else:
            print ("There is no booked items on this day.")
            return False



