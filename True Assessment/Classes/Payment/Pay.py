from Classes.Help.Claimed_DB import Claimed_items   # Import Class from other folder


class Pay:
    @staticmethod
    def payment(*args):     # Saving value for args.
        database = args[0]
        choice = args[1]
        username = args[2]
        choice_name = args[3]
        date = args[4]
        try:
            choice_pay = int(input("""Choose how you wanna pay.
                        1.Credit Card
                        2.PayPal
                        3.Bank Transfer:"""))   # Choice
            if type(choice_pay) is int:
                Claimed_items.db_items(database, choice, username, choice_name, date)   # Processing to Claimed_items
            else:
                return False
        except ValueError:
            print("Nope something wrong")
            return False
