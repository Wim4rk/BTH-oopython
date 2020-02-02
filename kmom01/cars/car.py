import random

class Car():
    """
    Represent a car
    """
    model1 = """
{pos}.-'--`-._
{pos}'-O---O--'
"""
    model2 = r"""
{pos}   __
{pos} _| =\__
{pos}/o____o_\
"""
    model3 = r"""
{pos}  ______
{pos} /|_||_\`.__
{pos}(   _    _ _\
{pos}=`-(_)--(_)-'
"""
    model4 = """
{pos}     .--.
{pos}.----'   '--.
{pos}'-()-----()-'
"""

    wheels = 4
    car_count = 0


    def __init__(self, model, price, driver):
        self.model = model
        self.driver = driver
        self._price = price

        self._speed = random.uniform(0.5, 2)
        self._position = 0

        Car.car_count += 1

    @classmethod
    def create_from_json(cls, json_data):
        return cls(json_data["model"], json_data["price"], json_data["driver"])

    def present_car(self):
        return "{d} with the car {m}. The car costs {p}$.".format(
            m=self.model, p=self._price, d=self.driver
        )

    def get_price(self):
        return self._price

    def get_model(self):
        spaces = " " * round(self._position)
        return getattr(self, self.model).format(pos=spaces)

    def set_price(self, new_price):
        if float(new_price) / float(self._price) > 0.7:
            self._price = new_price
            return "New price is " + str(self._price)

        return "New price is too low. You can lower it with 30% max."


    def move_cars(self):
        for car in self.cars:
            print(car.get_model())

    def move(self):
        self._position += random.uniform(0.5, 2.5) + self._speed

    def get_pos(self):
        return self._position

    def __add__(self, other):
        return self._price + other.get_price()

    def __iadd__(self, other):
        self._price += other.get_price()
        return self

    @classmethod
    def wheel_message(cls):
        print("A car normally have {nr} wheels".format(nr=cls.wheels))

# bmw = Car("BMW", 100000)
# volvo = Car("Volvo", 150000)

# print(bmw.model)
#
# print(volvo.model)
#
# print(bmw.wheels)
