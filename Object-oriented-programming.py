from Item import Item
# from Phone import Phone


item8=Item("Myitem",750)

#Setting an attribute
# item8.price=900

#Getting an attribute
print(item8.name)

item8.apply_increment(0.2)
item8.apply_discount()
print(item8.price)


