import csv


class cryptocoin:
    all = []
    currency_rate = 15

    def __init__(self, code, name, symbol, market_cap, price, circulating_supply, volume, one_hour, twenty_four_hour,
                 seven_day, invested_money=0):

        # Run validations to the received arguments
        # assert __invested_money >= 0, f"Price {__invested_money} is not greater than zero!"

        # Assign to self object
        self.code = code
        self.name = name
        self.symbol = symbol
        self.market_cap = market_cap
        self.price = price
        self.circulating_supply = circulating_supply
        self.volume = volume
        self.one_hour = one_hour
        self.twenty_four_hour = twenty_four_hour
        self.seven_day = seven_day
        self.__invested_money = invested_money

        # List of coins is created
        cryptocoin.all.append(self)

    @staticmethod
    def search_name(val):  # Function to search coin by the name. Output is the instance with all information
        for instance in cryptocoin.all:
            if val.upper() == instance.name:
                return instance

    @classmethod
    def instantiate_from_something(cls):  # Function to get data from csv.
        with open('all_coins.csv', 'r') as f:
            reader = csv.DictReader(f)
            coins = list(reader)

        for coin in coins:
            cryptocoin(
                code=int(coin.get('code')),
                name=(coin.get('name').upper()),
                symbol=(coin.get('symbol').upper()),
                market_cap=(coin.get('market_cap')),
                price=(coin.get('price')),
                circulating_supply=(coin.get('circulating_supply')),
                volume=(coin.get('volume')),
                twenty_four_hour=(coin.get('twenty_four_hour')),
                one_hour=(coin.get('one_hour')),
                seven_day=(coin.get('seven_day'),),
                invested_money=(coin.get('invested_money'))
            )

    @property  # Most important thing here is that property decorator allows to users to only read and unable to change it.
    def invested_money(self):
        return self.__invested_money

    @invested_money.setter  # Setter it allows back to change the variable. If you want to be variable to be fixed, unactivate the function
    def invested_money(self, val):
        if val < 0:
            raise Exception('It can be a negative number')
        self.__invested_money = str(val)

    @staticmethod
    def top_cryptos_for_day(
            val):  # Function takes one argument that is the percentage increase coin, search through all the instances and finds matches .
        for instance in cryptocoin.all:
            if instance.twenty_four_hour == '' or instance.twenty_four_hour == '?':
                continue
            elif float(instance.twenty_four_hour) >= val:
                print(instance)

    @staticmethod
    def top_cryptos_for_hour(val):
        for instance in cryptocoin.all:
            if instance.one_hour == '' or instance.one_hour == '?':
                continue
            elif float(instance.one_hour) >= val:
                print(instance)

    @staticmethod
    def top_cryptos_for_week(val):
        for instance in cryptocoin.all:
            if instance.seven_day == '' or instance.seven_day == '?':
                continue
            elif float(instance.seven_day) >= val:
                print(instance)

    def apply_currency_rate(self):  # Function to convert between currencies
        self.price = float(self.price) * self.currency_rate
        print(str(self.price) + " TL")

    def __repr__(self):  # This function allows to create list of objects
        return f"cryptocoin('{self.code}','{self.name}','{self.symbol}','{self.market_cap}','{self.price}','{self.circulating_supply}','{self.volume}','{self.twenty_four_hour}','{self.one_hour}','{self.seven_day}','{self.invested_money}' )"


cryptocoin.instantiate_from_something()
# print(cryptocoin.all)
cryptocoin.top_cryptos_for_week(25)


def NextMission():  # Clear this part after you have completed the mission.
    DoIt = '''You should find a fitting data structure for the project and explore about inheritance or using more than
    one classes in a file.'''
    return DoIt


print(NextMission())
