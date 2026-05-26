#Задание
class Facade():
    pass

facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)


#Задание
class Grade:
    minimum_passing = 65

class Rules:
    def washing_brushes(self):
        return "Point bristles towards the basin while washing your brushes."


#Задание
class Circle:
    pi = 3.14
    def __init__(self, diameter):
        self.radius = diameter/2
        print(f'New circle with diameter: {diameter}')

    def area(self, radius):
        return self.pi * radius ** 2

    def circumference(self):
        return 2 * self.pi * self.radius

    def __repr__(self):
        return f"Circle with radius {self.radius}"


teaching_table = Circle(36)
medium_pizza = Circle(12)
round_room = Circle(11460)

print(teaching_table.circumference())
print(medium_pizza.circumference())
print(round_room.circumference())

print(teaching_table.__repr__())
print(medium_pizza.__repr__())
print(round_room.__repr__())


#Задание
print(dir(5))
def this_function_is_an_object():
    pass
print(dir(this_function_is_an_object()))