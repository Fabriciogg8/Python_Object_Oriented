class Item:
    def __init__(self):
        print("I am created!")
    
    def calculate_total_price(self, x, y): 
        return x * y
    
    
item_1 = Item()
item_1.name = "Phone"
item_1.price = 100
item_1.quantity = 5
value_1 = item_1.calculate_total_price(item_1.price, item_1.quantity)


item_2 = Item()
item_2.name = "Laptop"
item_2.price = 1000
item_2.quantity = 3
value_2 = item_2.calculate_total_price(item_2.price, item_2.quantity)
 
 
if __name__ == "__main__":
    print(value_1)
    print(value_2)