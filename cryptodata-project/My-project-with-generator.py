from myproject import cryptocoin
cryptocoin.instantiate_from_something()
def generator_of_cryptocoin(list):
    i = 0
    while True:
        current = list[i]
        if i>len(list)-2:
            break
        yield current
        i+=1
list_of_coin=generator_of_cryptocoin(cryptocoin.all)
# for i in list_of_coin:
#     print(i)
print(next(list_of_coin))
print(next(list_of_coin))
print(next(list_of_coin))
print(next(list_of_coin))

