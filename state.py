from motor import ServoMotor

class State():
    def turn(self):
        raise NotImplementedError("turn is abstractmethod")

class Open(State):
    GPIO_PIN = GPIO_PIN
    OPENDEGREE = OPENDEGREE
    def __init__(self):
        self.motor = ServoMotor(self.GPIO_PIN)

    def turn(self):
        self.motor.drive(self.OPENDEGREE)

class Close(State):
    GPIO_PIN = GPIO_PIN
    CLOSEDEGREE = OPENDEGREE
    def __init__(self):
        self.motor = ServoMotor(self.GPIO_PIN)

    def turn(self):
        self.motor.drive(self.CLOSEDEGREE)

class Context:
    def __init__(self):
        self.open = Open()
        self.close = Close()
        self.state = self.open

    def change_state(self, event):
        if event == "Open":
            self.state = self.open
        elif event == "Close":
            self.state = self.close
        else:
            raise ValueError(
                "change_state method must be in {}".format(["open", "close"]))

    def turn(self):
        self.state.turn()