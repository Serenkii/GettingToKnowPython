import csv


class Item:
    pay_rate = 0.8  # class attribute: The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert isinstance(name, str), f"Type of name {name} is not a string."
        assert isinstance(price, float) or isinstance(price, int), f"Type of price {price} is not a number."
        assert isinstance(quantity, int), f"Type of quantity {quantity} is not an int."
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero."

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    # Why so complicated to make something private
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def __this_is_a_private_method(self):
        pass

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))  # you could leave quantity=... etc out
            )

    # https://stackoverflow.com/questions/136097/difference-between-staticmethod-and-classmethod
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
