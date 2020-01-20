from Classes.Booking.CheckAvailability import Check_Availability
from Classes.Booking.BookItem import Book_item
from Classes.Booking.Check_booked import Check_booked
from Classes.Payment.Advance_Payment import Advance_payment


class Booking_menu:
    def __init__(self, *args):
        self.database = args[0]
        self.username = args[1]
        self.book_menu()

    def book_menu(self):
        database = self.database
        username = self.username
        try:
            choice = int(input("""Please select an option.
            1. Check availability of items.
            2. Book item
            3. Check your booked items
            4. Pay in Advance.
            5. Exit to menu: """))
            if choice == 1:
                Check_Availability(database)
                self.book_menu()
            elif choice == 2:
                Book_item.booking(database, username)
                self.book_menu()
            elif choice == 3:
                Check_booked.check_book(database, username)
                self.book_menu()
            elif choice == 4:
                Advance_payment.advance_pay(database, username)
                self.book_menu()
            elif choice == 5:
                return
            else:
                print("Oops something went wrong")
                self.book_menu()
        except ValueError:
            print("Oops something went wrong !!")
            self.book_menu()
