class Car:


    def __init__(self, power, brand = "Unknown", max_speed = 0,
                  year = 2000, color = "white"):
            self.__power = power
            self.__brand = brand
            self.__max_speed = max_speed
            self.year = year
            self.color = color


    def get_power(self):
        return self.__power

    def get_brand(self):
        return self.__brand

    def get_max_speed(self):
        return self.__max_speed

    def __str__(self):
        return (f"{self.__brand}: {self.__power} к.с., "
                f"{self.__max_speed} км/год, {self.year}, {self.color}")

    def __repr__(self):
        return (f"Car(power={self.__power}, brand={self.__brand!r}, "
                f"max_speed={self.__max_speed}, year={self.year}, "
                f"color={self.color!r})")

    def __del__(self):
        print(f"Об'єкт {self.__brand} знищено")


def main():
    car1 = Car()
    car2 = Car(150, "BMW", 240, 2018, "black")
    car3 = Car(110, "Skoda", 190, 2015, "red")


    for car in (car1, car2, car3):
        print(car)
        print(repr(car))
        print(car.get_power(), car.get_brand(), car.get_max_speed(),
              car.year, car.color)


if __name__ == "__main__":
    main()
