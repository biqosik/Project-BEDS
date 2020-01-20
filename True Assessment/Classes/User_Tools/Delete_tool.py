import sqlite3


class DeleteTool:
    def __init__(self, *args):
        self.database = args[0]
        self.username = args[1]
        self.delete_tool()

    def delete_tool(self):
        with sqlite3.connect(self.database) as db:
            asses = db.cursor()
        check_username = "SELECT * FROM tool WHERE username = ?"
        asses.execute(check_username, [self.username])
        result = asses.fetchall()
        owner_id = []
        if result:
            for row in result:
                print(" ID = ", row[0],
                      " Username =", row[1],
                      " Tool name =", row[2],
                      " Price =", row[3],
                      " Description =", row[4], )
                owner_id.append(row[0])
            choice = input("Which item do you want to delete? Type in ID nr : ")
            delete_item = "DELETE FROM tool WHERE n_id = ? AND username = ?"
            user_item = False
            for u_id in owner_id:
                if u_id == choice:
                    user_item = True
            if user_item is True:
                try:
                    choice_1 = input("""ARE YOU SURE?
                    Type y for yes
                    Type n for no: """)
                    choice_1.lower()
                    if choice_1 == 'y' or choice_1 == 'yes':
                        asses.execute(delete_item, [choice, self.username])
                        db.commit()
                        return
                    else:
                        return
                except SyntaxError as e:
                    print(__name__, ':', "Delete_tool", " - ", e)
                    self.delete_tool()
            else:
                print("That is not your item")
                return
        else:
            print("Oops!!! You do not have any items.")
            return
