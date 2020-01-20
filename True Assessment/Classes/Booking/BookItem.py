import sqlite3
from sqlite3 import Error
from Classes.Help.DateValue import Checking_value
from Classes.Search_a_tool import show_items


class Book_item:
    @staticmethod
    def booking(database, username):
        try:
            with sqlite3.connect(database) as db:
                assessment = db.cursor()
            print("Please give what date you want to book your item.")
            date1 = Checking_value.checking_value()
            if not date1:
                return
            find_date = ("SELECT * FROM tool_availability WHERE lend_date=?")
            assessment.execute(find_date, [date1])
            items = assessment.fetchall()
            if items:
                print("Those items are already taken on this date: ")
                for row in items:
                    print(" ID = ", row[0],
                          " Owner =", row[1],
                          " Renting Username =", row[2],
                          " Item =", row[3],
                          " Date =", row[4], )
                book_tool(database, date1, username)
            else:
                print("There aren't any items booked for this day.")
                book_tool(database, date1, username)
        except Error as e:
            print("Booking problem: ", e)


def book_tool(database, date1, username):
    try:
        with sqlite3.connect(database) as db:
            assessment = db.cursor()
        show_items(database)
        choice = input("""Please provide id of item that you want to book:
         Please remember that if you will book item even if you won't actually lend it you will still pay 1 day fee of an item !!!
         If you want to go back simply press 'Q': """)
        if choice == 'q' or choice == 'Q':
            return
        choice_name = str(input("Please provide name of an item: "))
        find_item = ("SELECT * FROM tool WHERE n_id=?")
        check_booked = "SELECT * FROM claimed_tools WHERE dates = ? AND n_id = ? AND tool_name = ?"
        assessment.execute(find_item, [choice])
        user = assessment.fetchall()
        for row in user:
            row1 = row[1]
            row2 = row[2]
        if user:
            find_date = ("SELECT * FROM tool_availability WHERE lend_date = ? AND n_id = ?")
            assessment.execute(find_date, [date1, choice])
            got = assessment.fetchall()
            assessment.execute(check_booked, [date1, choice, choice_name])
            claimed = assessment.fetchall()
            if got or claimed:
                print("Oops this item is already booked for this day or somebody has already borrowed it.")
            else:
                insert = 'INSERT INTO tool_availability (lend_date, n_id, tool_owner, username, tool_name) VALUES (?,?,?,?,?)'
                assessment.execute(insert, [date1, choice, row1, username, row2])
                db.commit()
                print("YEAH WE DID IT.")
                return
        else:
            print("!!! There is no item with that id !!!")

    except ValueError:
        print("You gave me something wrong !!")
        book_tool()
