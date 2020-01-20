import datetime
import sqlite3


class Take_paid:
    @staticmethod
    def paid_tools(database, username):
        date = datetime.date.today()
        with sqlite3.connect(database) as db:
            assessment = db.cursor()
        today_item = "SELECT * FROM hire_tool WHERE dates = ? AND username = ?"
        assessment.execute(today_item, [date, username])
        get_all = assessment.fetchall()
        taber = []
        if get_all:
            for row in get_all:
                print(row)
                taber.append(row[0])
            choice = int(input("Which ID you wanna take right now? : "))
            specialized = False
            try:
                for tab in taber:
                    if int(tab) == choice:
                        specialized = True
                if specialized is True:
                    choice_item = str(input("Please write item name : "))
                    for choices in get_all:
                        if choices[2] is choice_item:
                            choice_item = choices[2]      #COS NIE TAK KURWA
                else:
                    print("That's not yours isn't it ?")
                    return
            except ValueError:
                print ("That's not something we probably have.")
                return
            if choice_item is False:
                return
            insert = "INSERT INTO claimed_tools(n_id, username, tool_name, dates, return_date) VALUES (?,?,?,?,?)"
            assessment.execute(insert, [choice, username, choice_item, date, '2020-01-30'])
            delete_from = "DELETE FROM hire_tool WHERE n_id = ? AND dates = ?"
            assessment.execute(delete_from, [choice, date])
            db.commit()
            print("Okay we have done it.")
        else:
            print("I see you don't have anything booked today")
            return
