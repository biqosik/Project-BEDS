import sqlite3


class Claimed_items:

    @staticmethod
    def db_items(*args):
        database = args[0]
        n_id = args[1]
        username = args[2]
        tool_name = args[3]
        dates = args[4]

        with sqlite3.connect(database) as db:
            assessment = db.cursor()
        insert = "INSERT INTO hire_tool(n_id, username, tool_name, dates, paid) VALUES (?,?,?,?,?) "
        assessment.execute(insert, [n_id, username, tool_name, dates, 1])
        delete = "DELETE FROM tool_availability WHERE n_id = ? AND username = ? AND lend_date = ?"
        assessment.execute(delete, [n_id, username, dates])
        db.commit()
        print("We did it !!!")
        db.close()
