from Classes.Booking.Check_booked import Check_booked
from Classes.Help.DateValue import Checking_value
from Classes.Help.Claimed_DB import Claimed_items
import sqlite3


class Advance_payment:
    @staticmethod
    def advance_pay(*args):
        database = args[0]
        username = args[1]  # Saving value from args
        Check_booked.check_book(database, username)     # Going for Check_booked
        try:
            choice = int(input("Type N_ID of item you wanna pay in advance: "))     # Choice
            choice_date = Checking_value.checking_value()   # DataValue.py
            if not choice_date:
                return False
            with sqlite3.connect(database) as db:
                assessment = db.cursor()
            id_choice = "SELECT * FROM tool_availability WHERE n_id = ? AND username = ? AND lend_date = ?"
            assessment.execute(id_choice, [choice, username, choice_date])  # Finding id_choice
            confirm = assessment.fetchall()
            if confirm:
                for row in confirm:
                    print("Okay so you wanna pay for N_id =", row[0], 'Item = ', row[3], 'On date = ', row[4])
                    print("""Choose how you wanna pay.
                    1.Credit Card
                    2.PayPal
                    3.Bank Transfer:""")
                    Claimed_items.db_items(database, row[0], username, row[3], row[4])  # Claimed_DB.py
                    return
            else:
                print("That is not your item")
                return
        except ValueError as e:
            print(__name__, ':', 'Payment', " - ", e)
