import datetime
import sqlite3
from sqlite3 import Error


class Availabililty:
    @staticmethod
    def Check_availability_today(database):
        try:
            print("Those are available items to lend: ")
            date = datetime.date.today()
            check1 = "SELECT * FROM tool_availability WHERE lend_date = ? AND n_id = ?"
            check2 = "SELECT * FROM hire_tool WHERE dates = ? AND n_id = ?"
            check3 = "SELECT * FROM tool"
            check4 = "SELECT * FROM claimed_tools WHERE dates = ? AND n_id = ?"
            with sqlite3.connect(database) as db:
                assessment = db.cursor()
            assessment.execute(check3)
            tools = assessment.fetchall()
            if tools:
                for row in tools:
                    assessment.execute(check1, [date, row[0]])
                    availability = assessment.fetchall()
                    assessment.execute(check2, [date, row[0]])
                    hires = assessment.fetchall()
                    assessment.execute(check4, [date, row[0]])
                    claimed = assessment.fetchall()
                    if not availability and not hires and not claimed:
                        print(" ID = ", row[0],
                              " Owner =", row[1],
                              " Item =", row[2],
                              " Price_per_day =", row[3],
                              " Price_per_half_day = ", row[4], )
            else:
                return False
        except Error as e:
            print(__name__, ': Availability - ', e)
            return False
