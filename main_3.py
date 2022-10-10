class Item:
    
    pay_rate = 0.8 # The pay rate after 20% of discount    
    
    def __init__(self, name:str, price:float, quantity=0):
        # Run validations to received arguments
        assert price >= 0, f'Price {price} is not greater than or equal to zero'
        assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero'
        
        # Assign to self object
        print(f'An instance created: {name}')
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def totalPrice(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        return self.price * self.pay_rate
    
    
item_1 = Item("Phone", 100, 1)
value_1 = item_1.totalPrice()
value_d1 = item_1.apply_discount()

item_2 = Item("Laptop", 100, 1)
# Reassign the pay_rate value
item_2.pay_rate = 0.7
value_2 = item_2.totalPrice()
value_d2 = item_2.apply_discount()

item_3 = Item("Mouse", 50)
value_3 = item_3.totalPrice()


 
if __name__ == "__main__":
    print(value_1, value_2, value_3)    
    print(Item.pay_rate)
    # print(Item.__dict__)
    # print(item_1.__dict__)
    print(value_d1)
    print(value_d2)
    