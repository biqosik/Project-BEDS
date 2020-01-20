import sqlite3


class Login:

    def __init__(self, *args):
        self.database_path = args[0]

    def login_in(self):
        # /// Connecting to db ///
        with sqlite3.connect(self.database_path) as db:
            asses = db.cursor()
        # /// find_user here takes us to username and password column in db ///
        find_user = ("SELECT username FROM user WHERE username = ? AND password = ?")
        # /// username and password here you put your details and it goes to db and check if it is correct///
        username = input('Please provide username: ')
        password = input('Please provide password: ')
        asses.execute(find_user, [username, password])
        results = asses.fetchall()
        # /// if results is True that means you have put good username and password, and goes to tools menu. ///
        if results:
            return username
        # /// if not than print an error and goes to menu function again ///
        else:
            print("Oops!!, Username or Password not matched")


