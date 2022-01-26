from item import Item
from phone import Phone

# https://youtu.be/Ej_02ICOIgs

Item.instantiate_from_csv()

phone1 = Phone("Samsung", 932154)

print(Item.all)
print(Phone.all)
phone1.name = "Whyyyy"
print(phone1.name)

# for instance in Item.all:
#     print(instance.name)


# print(Item.__dict__)  # All the attributes for Class level
# print(item1.__dict__)  # All the attributes for instance level
