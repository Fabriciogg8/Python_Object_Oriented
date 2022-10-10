# Python Object Oriented

<a name="top"></a>

## [English](#item1)
## [Spanish](#item2)

 
<a name="item1"></a>

### English
 
#### Used technology: Python

##### Abstract

In this repository, I will detail some examples of Object Oriented with python language.

# Object Oriented 

## main_1.py

In this file I declare 4 variables, with their corresponding value. Then we print the data type of this variables, and we see in the output the keyword of class at the beginning. This is showing that every data in python is an instance of a class (strings, integers, etc). So each data type is an object. 

## main_2.py

First we will create the class that we need, and then we can create an instance (same as object) for that class. 

To create a class we need to use this keyword, followed by the name we want to give it. 

```py
class Item:
```

Now we can create an **instance** of that class by doing the following:

```py
item_1 = Item()
```

After we have an instance, we can give it different **attributes with the dot**. 

```py
item_1.name = "Phone"
item_1.price = 100
item_1.quantity = 5
```

### Creating methods 

We can create methods in our class that will be accessible from our instances. We do this just like when we write a function. 
Importantly, we need a parameter called **self**. This parameter refers to the object itself.

```py
class Item:
    def someCalc(self):
        pass 
```

We can give parameters to the method so that we can use the attributes we define.

```py
class Item:
    def someCalc(self, x, y):
        return x * y

item_1.someCalc(self.price, self.quantity)
```

### Constuctor 

The problem we had in the class we defined earlier is that we have hard coded the attributes of our objects. It is better to create an instance successfully, that the attributes must be passed from the beginning.

For these we have an especial method with a unique name which is called:

```py
class Item:
    def __init__(self):
        pass
```

When we create an instance, Python calls this magic method automatically. We can test this by doing a print inside the __init__ method. 

## main_3.py

We can take advantage of the constructor method and pass more parameters to it.

```py
class Item:
    def __init__(self, name):
        self.name = name
```

Now when we created a new instance, we need to give this argument to the create the object. 

```py
item_1 = Item('Laptop')
```

We can also pass a default value to a parameter. This means that if we don't change it later, this is the value that will be set on all objects.

```py
    def __init__(self, name, price, quantity=0):
```

After instantiating an object, we can pass it more arguments. This is similar to the first thing we learn, so we can give other arguments to some instances and not all. For example, we can create two objects, a keyboard and a laptop, corresponding to the same class. But to the keyboard we add an argument outside the class, called has_numpad.

```py
item_2 = Item('Keyboard')
item_2.has_numpad = False
```

Now we have to understand that if we create the class with parameters, these can be used inside the methods of the class. This means that we don't need to use parameters in the methods, if the parameters are already given to the instance.

Constructor
```py
    def __init__(self, name, price, quantity=0):
```
Method
```py
    def totalPrice(self):
        return self.price * self.quantity
```

### Static Typing

In this case, we want to pass an integer in the constructor parameters, but if we pass a string, the method still works, although this is something we don't want. The solution is to use static typing. So first we need to pass the parameter name, then a colon, and then the type of data we expect to receive.

```py
    def __init__(self, name:str, price:float, quantity=0):
```
We can see that in the quantity we do not add a data type. This is because when we assign a default value, the parameters will recognize what data type they are. 

### Asserts

Also, if we want to check that nobody inserts a negative number in the price and quantity, we can make an **assert**. We can add a string to the statement to have a better understanding of the error.

```py
assert price >= 0, f'Price {price} is not greater than or equal to zero'
assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero'
```

### Class atributes

Imagine that we need to apply to all instances the same value for a parameter. In the case of a store we can imagine it as a discount.These are called **class attributes**, they will belong to the class itself, however you can also access this attribute for the instance.  

```py
class Item:
    pay_rate = 0.8 # The pay rate after 20% of discount     
    def __init__(self) 
```

Now we can access that parameter from the class. 

```py
print(Item.pay_rate) #output 0.8
```

and also we access the parameter form the instance level. This is because the instance will first try to find the parameter at the instance level, and if it doesn't find it, it will look at the class level.

```py
print(item_1.pay_rate) #output 0.8
print(item_2.pay_rate) #output 0.8
```

### Magic attribute

We can call a magic attribute, which we have for all the objects, which is already given by python, this is: **__dict__**. 

```py
print(Item.__dict__) 
print(item_1.__dict__) 
``` 
In this way we can see the attributes of the objects, with their corresponding value. 

We can also **reassign** the value of a class method, on the instance. For example if we want to pass 70% to a specific object we can say:

```py
item_1.pay_rate = 0.7
```  

So in the other objects the value of this parameter will still be 0.8. When using a class attribute inside a method, the best practice is to use **self.pay_rate** (in this example), because we can call **Item.pay_rate** but it will call the parameter on the class, and not the one on the instance, having a disagreement if we change the value for that instance.

### main_4.py

We can create a list inside our class to aggregate all the instances we create of that class. So we can see when we want how many objects are created. 

So we create an empty list and then in the constructor we add an action to execute, that adds the instance to the list. 

```py
Item.all.append(self) #all is the list
``` 

Now we can also do a for loop to iterate through the list and print all the instances. 

### __repr__

The repr() method returns a string containing a printable representation of an object. The best practice is to return the object in the exact form it was created.

```py
def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})
``` 

### Class Method

We will create a csv file from where to read the instances of the class. This method it would be a class method. For this we need to use a **decorator**, that will be responsable to convert this method into a class method. The decorators in python is just a quick way to change the behavior of the functions. 

This class method still receives a parameter but in this case the parameter name is **cls** instead of self. So when we call a class method the class itself is passed as the first parameter. 

```py
@classmethod
def instantiate_from_csv(cls):
    pass
```

Therefore, the class methods:
* They cannot access the attributes of the instance.
* But if they can modify the attributes of the class.

### Static Method

This method should perform a function for us, that has some logical connection to a class. For example if we want to check if a number is an int or a float, then this is a good candidate for creating a static method. 

The static method are never sending, in the background, the **instance (in other words self)** as the first parameter. In other words, static methods could be seen as **normal functions**, except that they are bound to a specific class.

```py
@staticmethod
def is_integer(num):
    pass
```
***It is very rare to call a class method or a static method from an instance, although it will not give an error.***


### main_5.py

### Inheritance

We can create a separate class that will inherit the functionalities of the parent class. We have to pass the parent class inside the parentheses.

```py
class Phone(Item):
    pass   
```

### super

When we initialize the __init__ method inside a child class, python expects the super function to be called intentionally. This function allows us to have full access to all the attributes of the parent class. 

```py
def __init__(self, name:str, price:float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )
```

When we pass the parameters in the super function we can ask ourselves, if this is a duplication of code? because we already have the parameters that we receive in the child class. That is something that could be solved by **keyword arguments**.

### Access to the class name

We can do this by calling two magic methods:

```py
{self.__class__.__name__}
```

### Project

To continue, we will organize the code in different files, inside the project folder. We continue working on the main.py file.

We create an Item instance, and then we can override an attribute, calling that attribute and adding a new value. 

```py
item1 = Item("My item", 5)
item1.name = "Other item"

print(item1) #Output >>> Item ('Other item', 5, 0)
``` 

### Encapsulation

What if we want to restrict our users, to change the attribute of name. This is something we might want to achieve with critical attributes, like the name of your instances. So we can create **read only** so called attributes. This is called **encapsulation**.

To start creating read only attributes, we need to use decorators. Like the next example:

```py
@property
def read_only_attribute(self):
    return "AAA"
```
 
If we now try to change the value of the attribute, we will receive an error. 

Now, if we want to wrap an attribute that is passed in the constructor, we create a method for that attribute with the **@property** decorator. And in the constructor we use that attribute with a double underscore, which means it's a private method. 

```py
# Assign to self object
print(f'An instance of {self.__class__.__name__} created: {name}')
self.__name = name # We create the attribute with double underscore
```
and create the method

```py
@property
def name(self):
    return self.__name
```

### Setter

If we want to be able to change the value of the attribute, we can create a method, with a decorator. This decorator needs to have the attribute name and **.setter**. 

```py
@name.setter
def name(self, value):
    self.__name = value
``` 



## [Spanish](#item2)

 
<a name="item2"></a>

### Español 

