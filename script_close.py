from motor import ServoMotor

GPIO_PIN = GPIO_PIN
CLOSEDEGREE = CLOSEDEGREE
sm = ServoMotor(GPIO_PIN)
sm.drive(CLOSEDEGREE)