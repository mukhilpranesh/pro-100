class Atm:
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number

    def cash_withdrawal(self, amount):
        print(f"Withdrawing ${amount} from ATM using card number: {self.card_number}")

    def balance_enquiry(self):
        print(f"Checking balance for card number: {self.card_number}")

    def change_pin(self, new_pin):
        self.pin_number = new_pin
        print(f"PIN changed successfully for card number: {self.card_number}")

    def mini_statement(self):
        print(f"Fetching mini statement for card number: {self.card_number}")

if __name__ == "__main__":
    atm_user = Atm("1234567890", "1234")
    atm_user.cash_withdrawal(200)
    atm_user.balance_enquiry()
    atm_user.change_pin("4321")
    atm_user.mini_statement()
