from motor import ServoMotor

GPIO_PIN = GPIO_PIN
OPENDEGREE = OPENDEGREE
sm = ServoMotor(GPIO_PIN)
sm.drive(OPENDEGREE)