import csv

class Item:
    
    pay_rate = 0.8 # The pay rate after 20% of discount    
    all = []
    
    def __init__(self, name:str, price:float, quantity=0):
        # Run validations to received arguments
        assert price >= 0, f'Price {price} is not greater than or equal to zero'
        assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero'
        
        # Assign to self object
        print(f'An instance of {self.__class__.__name__} created: {name}')
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)
        
    def totalPrice(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        return self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
    
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            # The built in function is_integer() return True if the float is -> point zero
            return num.is_integer() 
        elif isinstance(num, int):
            return True
        else:
            return False
    
    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}', {self.price}, {self.quantity})"
    
   
class Phone(Item):
       
    def __init__(self, name:str, price:float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )
        
        # Run validations to received arguments
        assert broken_phones >= 0, f'Price {broken_phones} is not greater than or equal to zero'
        
        # Assign to self object
        self.broken_phones = broken_phones
    
             

phone1 = Phone("jscPhonev10", 600, 5, 1)
phone2 = Phone("jscPhonev20", 730, 5, 2)
 
if __name__ == "__main__":
    print(Phone.all)