import sqlite3


class CreateTool:

    def __init__(self, *args):
        self.database = args[0]
        self.username = args[1]
        self.create_tool()

    def create_tool(self):
        with sqlite3.connect(self.database) as db:
            asses = db.cursor()

        asses.execute('SELECT n_id FROM tool ORDER BY n_id')
        tables = []
        try:
            ziggs = asses.fetchall()
            for row in ziggs:
                row = int(row[0])
                tables.append(row)
            tables.sort()
            n_id = int(tables[-1]) + 1
        except IndexError:
            n_id = 1
        n_tool = input("Please insert name of a tool: ")
        try:
            n_price = float(input("Please insert price of this tool per day: "))
            n_price_half = float(input("Please insert price of this tool per half day: "))
        except ValueError:
            print("Oops!!!, Did you by accident messed something ?")
            self.create_tool()
        n_description = input("Please give some description about this tool: ")
        insert = 'INSERT INTO tool(n_id,username, price_per_day, price_half_day, description, tool_name) VALUES (?, ?, ?, ?, ?, ?)'
        asses.execute(insert,
                      [n_id, self.username, (str(n_price) + "£"), (str(n_price_half) + "£"), n_description, n_tool])
        db.commit()
        print("I think we made it.")
        return
