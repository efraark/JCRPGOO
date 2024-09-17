class Bicycle:
    MAX_GEAR = 18
    MIN_SERIAL_NUMBER = 1000

    def __init__(self, speed, pedal_cadence, current_gear, serial_number):
        self.speed = max(0, speed)
        self.pedal_cadence = max(0, pedal_cadence)
        self.current_gear = min(max(1, current_gear), self.MAX_GEAR)
        self.serial_number = max(serial_number, self.MIN_SERIAL_NUMBER)

class BicyclePrinter:
    @staticmethod
    def print_info(bicycle):
        print(f"Velocidade: {bicycle.speed} km/h, Cadência: {bicycle.pedal_cadence} rpm, Marcha: {bicycle.current_gear}, Nº de Série: {bicycle.serial_number}")
