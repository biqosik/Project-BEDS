import sqlite3


class Create_account:
    def __init__(self, *args):
        self.database = args[0]

    def create_acc(self):
        # /// It's connecting to DB ///
        with sqlite3.connect(self.database) as db:
            asses = db.cursor()
        # /// find_user is a var that search db of existing username ///
        find_user = ("SELECT username FROM user WHERE username = ?")
        # /// below there are var that stores new username and new password. ///
        n_username = input('Please provide username: ')
        n_password = input('Please provide password: ')
        # /// execute now search for a username you have putted if it is in base. ///
        asses.execute(find_user, [n_username])
        if asses.fetchall():
            # /// If it is than will create comment that Username is taken and go back to create_acc function ///
            print("Oops, Username Taken!!!")
            return
        elif len(n_password) < 7:
            # /// This one checks if password is not to short. If yes than go back to create_acc function ///
            print("Oops, password too short")
            self.create_acc()
        else:
            # /// If everything is alright and username doesn't exist in database it puts new username and his
            # password into DB and go back to menu function ///
            print('Success!!', "Account Created")
            insert = 'INSERT INTO user(username, password, type_of_user)VALUES (?,?,?)'
            asses.execute(insert, [n_username, n_password, 1])
            db.commit()
            return n_username
