class Car:
    def __init__(self, model, price_per_day):
        self.model = model
        self.price_per_day = price_per_day
        self.is_available = True

    def rent(self):
        if self.is_available:
            self.is_available = False
            return "Mashina ijaraga berildi"
        return "Mashina band"

    def return_car(self):
        self.is_available = True
        return "Mashina qaytarildi"


class RentalService:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_cars(self):
        for car in self.cars:
            status = "Bo‘sh" if car.is_available else "Band"
            print(car.model, "-", status)

    def rent_car(self, model, days):
        for car in self.cars:
            if car.model == model and car.is_available:
                car.rent()
                return f"Narx: {days * car.price_per_day} so‘m"
        return "Mashina topilmadi"


service = RentalService()
service.add_car(Car("Malibu", 500000))
service.add_car(Car("Gentra", 300000))

service.show_cars()
print(service.rent_car("Malibu", 3))
service.show_cars()
