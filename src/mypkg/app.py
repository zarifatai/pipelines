class App:
    def __init__(self) -> None:
        print("App initialized")

    def calculate_area(self, length: float, height: float) -> float:
        return length * height

    def calculate_volume(self, length: float, height: float, width: float) -> float:
        return length * height * width


if __name__ == "__main__":
    app = App()
    length = 25.0
    height = 30.0
    width = 15.0

    print(app.calculate_area(length, height))
    print(app.calculate_volume(length, height, width))
