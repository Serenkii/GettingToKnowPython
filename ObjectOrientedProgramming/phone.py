from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)

        # validations
        assert isinstance(broken_phones, int), f"Type of broken_phones {broken_phones} is not an int."
        assert broken_phones >= 0, f"Price {broken_phones} is not greater than or equal to zero!"

        self.broken_phones = broken_phones