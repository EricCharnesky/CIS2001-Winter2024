class Polygon:

    def __init__(self, number_of_sides):
        self._side_lengths = []
        self._number_of_sides = number_of_sides
        for side in range(number_of_sides):
            self._side_lengths.append(0)

    def get_number_of_sides(self):
        return self._number_of_sides

    def set_side_length(self, side_index, length):
        self._side_lengths[side_index] = length

    def get_side_length(self, side_index):
        return self._side_lengths[side_index]

    def get_perimeter(self):
        return sum(self._side_lengths)


class Rectangle(Polygon):

    def __init__(self, length, width):
        super().__init__(4)
        self.set_side_length(0, length)
        self.set_side_length(1, width)

    def set_side_length(self, side_index, length):
        if side_index % 2: # odd index
            super().set_side_length(1, length)
            super().set_side_length(3, length)
        else: # even
            super().set_side_length(0, length)
            super().set_side_length(2, length)

    def get_area(self):
        return self.get_side_length(0) * self.get_side_length(1)


class Square(Rectangle):

    def __init__(self, length):
        super().__init__(length, length)

    def set_side_length(self, side_index, length):
        super().set_side_length(0, length)
        super().set_side_length(1, length)


class Triangle(Polygon):

    def __init__(self, base, height):
        super().__init__(3)
        self._base = base
        self._height = height

    def get_area(self):
        return self._base * self._height * .5



class Item:

    def __init__(self, name, quantity, unit_price):
        self._name = name
        self.set_quantity(quantity)
        self.set_unit_price(unit_price)

    def get_name(self):
        return self._name

    def set_unit_price(self, unit_price):
        if unit_price < 0:
            unit_price = 0
        self._unit_price = unit_price

    def get_unit_price(self):
        return self._unit_price

    def set_quantity(self, quantity):
        if quantity < 0:
            quantity = 0
        self._quantity = quantity

    def get_quantity(self):
        return self._quantity

    def get_total_price(self):
        return self._unit_price * self._quantity

    def __str__(self):
        return f"{self._quantity} {self._name} @ ${self._unit_price: .2f} - Total: ${self.get_total_price(): .2f}"


class Taxable_Item(Item):

    def __init__(self, name, quantity, unit_price, tax_rate):
        super().__init__(name, quantity, unit_price)
        # self._tax_rate = 0 - makes the warning go away
        self.set_tax_rate(tax_rate)

    def set_tax_rate(self, tax_rate):
        if tax_rate >= 1:
            tax_rate *= .01
        elif tax_rate < 0:
            tax_rate = 0
        self._tax_rate = tax_rate

    def get_total_price(self):
        return super().get_total_price() * (1 + self._tax_rate)

    def __str__(self):
        return super().__str__() + f" ( Tax Rate: {self._tax_rate * 100}% )"


class Shopping_Cart:

    def __init__(self):
        self._items = []

    def add_item(self, item: Item):
        self._items.append(item)

    def checkout(self):
        grand_total = 0
        for item in self._items:
            print(item)
            grand_total += item.get_total_price()

        print(f"Grand Total: ${grand_total: .2f}")




recees = Taxable_Item("Reece's", 10, 1.99, 6)
apples = Item("Gala", 12, 1)

cart = Shopping_Cart()

cart.add_item(recees)
cart.add_item(apples)

cart.checkout()







class Mammal:

    def __init__(self, name, species, noise):
        self.HAS_HAIR = True
        self.GIVES_LIVE_BIRTH = True
        self._name = name
        self._species = species
        self._noise = noise

    def get_name(self):
        return self._name

    def get_species(self):
        return self._species

    def get_noise(self):
        return self._noise


class Human(Mammal):

    def __init__(self, name, noise):
        super().__init__(name, "homosapien", noise)




some_mammal = Mammal("generic mammal", "generic speicies", "womp womp")
