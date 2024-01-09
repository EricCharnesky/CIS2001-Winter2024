class Chair:

    def __init__(self):
        self._color = ""
        self._number_of_legs = 0
        self._has_wheels = False
        self._height_in_meters = 0

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    # good object oriented programming goal - encapsulation
    # protect the integrity for our class
    # ensuring we have valid values for attributes
    def set_height_in_meters(self, height_in_meters: float):
        if height_in_meters < 0:
            height_in_meters = 0

        self._height_in_meters = height_in_meters



                    # indicates has_wheels should be a bool
    def set_has_wheels(self, has_wheels: bool):
        self._has_wheels = has_wheels

                    # indicates it will return a bool - code based documentation
    def get_has_wheels(self) -> bool:
        # text based comment documentation
        """get_has_wheels returns a boolean value of if it has wheels"""
        return self._has_wheels



def print_chair_details(chair: Chair):
    print(chair.get_color())
    print(chair.get_has_wheels())

erics_chair = Chair()

# bad practice - don't access private attributes directly
erics_chair._color = "blue"

erics_chair.set_has_wheels("yes")
erics_chair.set_has_wheels(True)

value = erics_chair.get_has_wheels()

print_chair_details(erics_chair)
