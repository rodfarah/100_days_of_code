from single_car import SingleCar, possible_position


class Car():
    """Instantiate car object."""

    def __init__(self):
        self.all_cars = []

    def create_first_car(self):
        """Create first car."""
        first_car = SingleCar()
        self.all_cars.append(first_car)

    def create_another_car(self):
        """Create one more car"""
        another_car = SingleCar()
        new_car_position = possible_position()
        # Don't want to overlap cars horizontally:
        for car in self.all_cars[-4:]:
            while new_car_position[-1] == car.ycor():
                new_car_position = possible_position()
        another_car.goto(new_car_position)
        self.all_cars.append(another_car)

    def move_left(self, pixels=5):
        """Move car object to the left. You may choose number of pixels (speed) as a parameter."""
        for car in self.all_cars:
            car.goto((car.xcor() - pixels), car.ycor())

    def possible_colision(self) -> list:
        """Return "y coordinate" of a car if this car is in +30 or -30 "x coordinate" compared to a turtle "x coordinate"."""
        return [car.ycor() for car in self.all_cars if 30 > car.xcor() > -30]
