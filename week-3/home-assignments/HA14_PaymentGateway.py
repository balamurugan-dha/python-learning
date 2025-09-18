class CreditCardPayment:
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment:
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class BankTransferPayment:
    def process_payment(self, amount):
        print(f"Processing bank transfer of ${amount}")

def make_payment(payment_method, amount):
    payment_method.process_payment(amount)

if __name__ == "__main__":
    credit_card = CreditCardPayment()
    paypal = PayPalPayment()
    bank_transfer = BankTransferPayment()
    
    payments = [credit_card, paypal, bank_transfer]
    amounts = [100, 50, 200]
    
    for payment, amount in zip(payments, amounts):
        make_payment(payment, amount)