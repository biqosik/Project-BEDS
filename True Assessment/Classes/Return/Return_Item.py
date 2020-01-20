import sqlite3
import datetime  # Importing Modules.


class Returning:
    @staticmethod
    def return_item(database, username):
        try:
            with sqlite3.connect(database) as db:
                assessment = db.cursor()
            assessment.execute("SELECT * FROM claimed_tools WHERE username = username")  # Database
            your_items = assessment.fetchall()
            for row in your_items:
                print(row)  # Printing username items
            compare_date = "SELECT * FROM claimed_tools WHERE username = ? AND n_id = ?"
            choice = int(input("Please put ID of an item you wish to return: "))  # Choice ID
            assessment.execute(compare_date, [username, choice])
            u_choice = assessment.fetchall()    # Check / Get ID from Database
            delete_claimed = "DELETE FROM claimed_tools WHERE n_id = ?"
            for row in u_choice:
                tdate = row[4]  # Saving return date from database item
            if u_choice:
                todaay = datetime.datetime.strptime(tdate, '%Y-%m-%d')  # Making tdate a date type
                return_date = todaay.date()
                today = datetime.date.today()
                if return_date >= today:     # If return date is not postponed
                    assessment.execute(delete_claimed, [choice])    # Delete Item from DB table
                    db.commit()
                    print("You have successfully returned an item !!!")
                else:
                    print("Oops you have forgot to give back tool in right time !!! You will have to pay a fee.")
                    assessment.execute(delete_claimed, [choice])    # Delete Item from DB table
                    db.commit()
            else:
                print("Oops something went bad !!!")
        except ValueError:
            print("Oops something wrong")
            return
