class Car():
    wheels = 4
    car_count = 0

    def __init__(self, model, price):
        self.model = model
        self._price = price

        Car.car_count += 1
        self.car_nr = Car.car_count

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if float(new_price) / float(self._price) > 0.7:
            self._price = new_price
            return "New price is " + str(self._price)

        return "New price is too low. You can max lower it with 30%."

    def present_car(self):
        return "The model {m} costs {p}$.".format(
            m=self.model, p=self._price
        )

    def __add__(self, other):
        return self._price + other.get_price()

    def __iadd__(self, other):
        self._price += other.get_price()
        return self

    @classmethod
    def wheel_message(cls):
        print("A car normally have {nr} wheels".format(nr=cls.wheels))

bmw = Car("BMW", 100000)
volvo = Car("Volvo", 150000)

print(bmw.model)

print(volvo.model)

print(bmw.wheels)
