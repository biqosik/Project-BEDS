import sqlite3


class Show_user_tools:
    def __init__(self, *args):
        self.database = args[0]
        self.username = args[1]
        self.booting()

    def booting(self):
        with sqlite3.connect(self.database) as db:
            asses = db.cursor()
        user_tools = ("SELECT * FROM tool WHERE username = ?")
        asses.execute(user_tools, [self.username])
        tool_results = asses.fetchall()
        if tool_results:
            for row in tool_results:
                print(" ID = ", row[0],
                      " Username =", row[1],
                      " Tool name =", row[2],
                      " Price =", row[3],
                      " Description =", row[4], )
        else:
            print("Oops there is nothing available my friend.")
