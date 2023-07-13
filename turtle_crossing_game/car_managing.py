from single_car import SingleCar, possible_position


class Car():
    def __init__(self):
        self.all_cars = []

    def create_first_car(self):
        first_car = SingleCar()
        self.all_cars.append(first_car)

    def create_another_car(self):
        another_car = SingleCar()
        new_car_position = possible_position()
        # Don't want to overlap cars:
        for car in self.all_cars[-4:]:
            while new_car_position[-1] == car.ycor():
                new_car_position = possible_position()
        another_car.goto(new_car_position)
        self.all_cars.append(another_car)

    def move_left(self, pixels=10):
        for car in self.all_cars:
            car.goto((car.xcor() - pixels), car.ycor())
