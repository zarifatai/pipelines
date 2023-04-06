class MyObject:
    def __init__(self, length: float, height: float, width: float) -> None:
        self.length = length
        self.height = height
        self.width = width

    def calculate_area(self) -> float:
        return self.length * self.height

    def calculate_volume(self) -> float:
        return self.length * self.height * self.width

    def get_attributes(self) -> tuple[float, float, float]:
        return (self.length, self.height, self.width)


if __name__ == "__main__":
    length = 25.0
    height = 30.0
    width = 15.0

    obj = MyObject(length, height, width)

    print(obj.calculate_area())
    print(obj.calculate_volume())
