import pigpio

class ServoMotor():
    def __init__(self, gpio_pin):
        self.gpio_pin = gpio_pin
        self.pi = pigpio.pi()
        self.pi.set_mode(self.gpio_pin, pigpio.OUTPUT)

    def angle2duty(self, angle):
        return int(95000 / 180 * angle + 72500)

    def drive(self, degree):
        self.pi.hardware_PWM(self.gpio_pin, 50, self.angle2duty(degree))