from Classes.Menu.MainMenu import Menu
from Classes.Menu.Tool_menu import ToolMenu
from sqlite3 import Error
import sqlite3

database_path = 'Database/assessment.db'
function_name = '__init__'


try:
    with sqlite3.connect(database_path) as db:
        asses = db.cursor()
    asses.execute(
        "CREATE TABLE IF NOT EXISTS user(username TEXT NOT NULL, password TEXT NOT NULL, type_of_user INTEGER NOT NULL )")
    asses.execute(
        "Create TABLE IF NOT EXISTS tool(n_id TEXT NOT NULL UNIQUE, username TEXT NOT NULL, tool_name TEXT NOT NULL, price_per_day FLOAT NOT NULL, price_half_day FLOAT NOT NULL, description TEXT NOT NULL )")
    asses.execute("Create TABLE IF NOT EXISTS tool_availability (n_id TEXT NOT NULL, tool_owner TEXT NOT NULL, username TEXT NOT NULL, tool_name TEXT NOT NULL, lend_date DATE )")
    asses.execute("Create TABLE if NOT EXISTS hire_tool (n_id TEXT NOT NULL, username TEXT NOT NULL, tool_name TEXT NOT NULL, dates DATE, paid INTEGER NOT NULL)")
    asses.execute("Create TABLE if NOT EXISTS claimed_tools(n_id TEXT NOT NULL, username TEXT NOT NULL, tool_name TEXT NOT NULL, dates DATE, return_date DATE NOT NULL)")
    db.commit()
except Error as e:
    print(__name__, ':', function_name, " - ", e)

try:
    registered_user = None
    while registered_user is None:

        menu = Menu(database_path)
        registered_user = menu.first_menu()

        if registered_user is not None:
            ToolMenu(registered_user, database_path)


except Error as e:
    print(__name__, ':', function_name, " - ", e)
    exit()
