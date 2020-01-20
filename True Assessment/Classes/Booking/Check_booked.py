import sqlite3


class Check_booked:
    @staticmethod
    def check_book(database, username):
        with sqlite3.connect(database) as db:
            assessment = db.cursor()
        find = "SELECT * FROM tool_availability WHERE username = ?"
        assessment.execute(find, [username])
        data = assessment.fetchall()
        if not data:
            print("Oops nothing here.")
            return
        print("Those are your booked items: ")
        for row in data:
            print(" ID = ", row[0],
                  " Owner =", row[1],
                  " Renting Username =", row[2],
                  " Item =", row[3],
                  " Date =", row[4], )
