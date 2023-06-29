from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_worn_data):
        self.tire_worn_data = tire_worn_data

    def needs_service(self):
        for value in self.tire_worn_data:
            if value >= 0.9:
                return True
        return False