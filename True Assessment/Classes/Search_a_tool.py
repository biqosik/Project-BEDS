import sqlite3


def search_a_tool(database):
    choice_in_search = input("""Please select an option:
    1: Full storage
    2: Individual search for a tool
    3: Go back to Tool Menu: """)
    try:
        if int(choice_in_search) == 1:
            show_items(database)
        elif int(choice_in_search) == 2:
            choice_in_individual = input("""Please select an option:
            1: Search by Username
            2: Search by Tool_Name """)
            if int(choice_in_individual) == 1:
                search_tool_username(database)
            elif int(choice_in_individual) == 2:
                search_tool_name(database)
            else:
                print("Oops!!!, Something went wrong!!")
                search_a_tool(database)
        elif int(choice_in_search) == 3:
            return
        else:
            print("Oops!!! Something went wrong !!")
            search_a_tool(database)
    except ValueError:
        print("Oops!!!, Something went wrong!!")
        search_a_tool(database)


def search_tool_username(database):
    with sqlite3.connect(database) as db:
        asses = db.cursor()
    find_by_username = "SELECT * FROM tool WHERE username = ?"
    username_name = input("Please provide username: ")
    asses.execute(find_by_username, [username_name])
    result = asses.fetchall()
    if result:
        for row in result:
            print(" ID = ", row[0],
                  " Username =", row[1],
                  " Tool name =", row[2],
                  " Price =", row[3],
                  " Description =", row[4], )
        search_a_tool(database)
    else:
        print("That username does not exist or this user does not have any active tools.")
        search_a_tool(database)


def search_tool_name(database):
    with sqlite3.connect(database) as db:
        asses = db.cursor()
    find_by_tool_name = "SELECT * FROM tool WHERE tool_name = ?"
    tool_name = input("Please provide tool_name: ")
    asses.execute(find_by_tool_name, [tool_name])
    result = asses.fetchall()
    if result:
        for row in result:
            print(" ID = ", row[0],
                  " Username =", row[1],
                  " Tool name =", row[2],
                  " Price =", row[3],
                  " Description =", row[4], )
        search_a_tool(database)
    else:
        print("That item does not exist or it is not available.")
        search_a_tool(database)


def show_items(database):
    with sqlite3.connect(database) as db:
        asses = db.cursor()
    howly = asses.execute('SELECT * FROM tool ORDER BY username')
    for row in howly:
        print(" ID = ", row[0],
              " Username =", row[1],
              " Tool name =", row[2],
              " Price =", row[3],
              " Description =", row[4], )
    return


class Search_tool:
    def __init__(self, database):
        self.database = database
        search_a_tool(self.database)
