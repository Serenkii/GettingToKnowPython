# https://youtu.be/Ej_02ICOIgs

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
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000)

print(Item.all)
for instance in Item.all:
    print(instance.name)

# print(Item.__dict__)  # All the attributes for Class level
# print(item1.__dict__)  # All the attributes for instance level
