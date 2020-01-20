import datetime


class Checking_value:
    @staticmethod
    def checking_value():
        try:
            print("Give date in digits ex. 2020/1/1")
            year = int(input('Enter a year: '))
            month = int(input('Enter a month: '))
            day = int(input('Enter a day: '))
            date1 = datetime.date(year, month, day)
            date2 = datetime.date.today()
            if type(date1) == datetime.date:
                if (date1 >= date2) and ((date1 - date2).days) <= 28:
                    print("Okay let me think... ")
                    return datetime.date(year, month, day)
                else:
                    print(""" !!!!!!! NO !!!!!!!
                    Did you put date that was already?
                    Remember that also you can only book or check, up to 4 weeks (28 days)""")
                    return False

        except ValueError:
            print("You didn't give me a correct date.")
            return False
