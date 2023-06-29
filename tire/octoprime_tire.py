from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_worn_data):
        self.tire_worn_data = tire_worn_data

    def needs_service(self):
        ans = 0
        for value in self.tire_worn_data:
            ans += value
        return (ans >= 3)