class Car:
    def __init__(self, brand, model, not_customized: bool):
        self.brand = brand
        self.model = model
        self.not_customized = not_customized

    def add_car_to_db(self):
        print(f"----{self.brand} {self.model} added to DB")
        return True

    def del_car_from_db(self):
        print(f"----{self.brand} {self.model} removed to DB")
        return True

    # @customize.setter
    def customize(self):
        self.not_customized = False
