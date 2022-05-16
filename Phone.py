from Item import Item
class Phone(Item):
    all=[]
    def __init__(self, name: str, price: float, quantity=0,broken_phones=0):  # quantity=0 can be used
        #Call to super function to have access to all attributes / methods
        super().__init__(
            name,price,quantity
        )


        # Run validations to the received arguments
        assert broken_phones >= 0, f"Price {broken_phones} is not greater than zero!"

        # Assign to self object
        self.broken_phones=broken_phones


# phone1=Phone("JscPhonev10", 500, 5)
# phone1.broken_phones = 1
# phone2= Phone("JscPhonev20", 700, 5)  # Child class's datas
# phone2.broken_phones = 1
# print(phone1.calculate_total_price())


# print(Item.is_integer(10.0))
# Item.instantiate_from_csv() #Since all objects instantiated from csv file. No need to define objects one by one
# print(Item.all)


# -------------------------------------------
# item1 = Item("Phone", 100, 10)
# item1.apply_discount()
# print(item1.price)
# print(item1.calculate_total_price())


# -------------------------------------------------------------
# item1.name = 'Phone'
# item1.price = 100         # No need for these 3 line anymore since init method.
# item1.quantity = 5
# -----------------------------------------------------------------

# item2 = Item("Laptop", 1000, 3)
# item2.pay_rate = 0.7  # new pay rate is decided. Not as class attributes
# item2.apply_discount()
# print(item2.price)
# print(item2.calculate_total_price())

# ------------------------------------------------------
# item2.name = 'Laptop'  #No need for these 3 line anymore since init method.
# item2.price = 100
# item2.quantity = 3
# ---------------------------------------------------------
# item3 = Item("Phone", 100, 1)
# item4 = Item("Laptop", 1000, 3)
# item5 = Item("Cable", 10, 5)
# item6 = Item("Mouse", 50, 5)
# item7 = Item("Keyboard", 75, 5)

# --------------------------------------------------------
# All objects are listed in 'all' (class attribute)
# for instance in Item.all:
# print(instance.name)
# ----------------------------------------------------------

# print(Item.all)  # Repr function make it happen