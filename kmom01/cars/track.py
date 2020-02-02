import time
import json
from car import Car

class RaceTrack():

    def __init__(self, finishline, sleep):
        self.finishline = finishline
        self.sleep = sleep

        self.cars = []
        self.create_cars()

    def create_cars(self):
        """
        Fetch four cars from json-file
        """
        json_cars = json.load(open("cars.json", encoding='utf-8'))
        for car in json_cars:
            self.cars.append(Car.create_from_json(car))

    def race(self):
        finished = []
        while not finished:
            self.clear_console()
            self.print_finishline()
            self.move_cars()

            finished = self.get_finished_cars()

            time.sleep(self.sleep)

        self.print_winners(finished)

    def get_finished_cars(self):
        return [car for car in self.cars if car.get_pos() >= self.finishline]

    def move_cars(self):
        for car in self.cars:
            car.move()
            print(car.get_model())
            self.print_finishline()

    def print_finishline(self):
        print(" " * self.finishline + "|")

    @staticmethod
    def print_winners(finished):
        print("Winner is!")
        for car in finished:
            msg = "{} finished first out of {} cars!"
            print(msg.format(car.present_car(), Car.car_count))

    @staticmethod
    def clear_console():
        print(chr(27) + "[2J" + chr(27) + "[;H")

if __name__ == "__main__":
    rt = RaceTrack(20, 0.2)
    rt.race()
