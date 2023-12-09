#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0, total = 0):
        self.discount = discount
        self.total = total
        self.items = []

    def add_item(self, title, price, multiply = 1):
        for item in range(multiply):
            self.items.append(title)
        final_price = price * multiply    
        self.total += final_price
        self.last_transaction = final_price
    
    def apply_discount(self):
        if self.discount > 0:
            discount_price = self.total * (self.discount / 100)
            self.total -= discount_price
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")    
    
    def void_last_transaction(self):
        self.total -= self.last_transaction

#case example
yo = CashRegister(20, 1000)
yo.apply_discount()


