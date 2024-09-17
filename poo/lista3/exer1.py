class Vehicle:
    def __init__(self, speed, tire_direction, owner):
        self.speed = speed
        self.tire_direction = tire_direction
        self.owner = owner

class VehiclePrinter:
    @staticmethod
    def print_info(vehicle):
        print(f"Proprietário: {vehicle.owner}, Velocidade: {vehicle.speed} km/h, Direção dos pneus: {vehicle.tire_direction} graus")
