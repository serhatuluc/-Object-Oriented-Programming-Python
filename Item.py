# Object oriented programming will be focused in this
# document. Inheritance and static methods are included also.
import csv
class Item:
    pay_rate = 0.8  # The pay rate after 20% discount #class attribute
    all = []

    def __init__(self, name: str, price: float, quantity=0):  # quantity=0 can be used
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Price {quantity} is not greater than zero!"

        # Assign to self object
        self.__name = name #Single underscore would work but it makes itself reachable
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

        # ---------------------------------------------------
        # Training
        # print(f"An instance created: {name}")
        # print("I AM CREATED")   #please check it to understand fully
        # -----------------------------------------------------

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate  # Item.pay_rate can be used. Check it to grab it

    def apply_increment(self,increment_value):
        self.__price=self.__price+self.__price*increment_value

    # With this property name of object can not be changed
    @property #getter
    def name(self):
        return self.__name #Double underscore should be used to hide attribute from being reached

    @name.setter
    def name(self,value):
        if len(value)>10:
            raise Exception("The name is too long")
        self.__name=value

    def calculate_total_price(self):
        return self.__price * self.quantity


    #Datas are taken from csv file.(items.csv)
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=int(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e:5.0,10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}','{self.__price}','{self.quantity}' )"

