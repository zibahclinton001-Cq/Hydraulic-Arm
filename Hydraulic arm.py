import time

class HydraulicArm:
    def __init__(self):
        self.shoulder = 0
        self.elbow = 0
        self.hand_open = True
        print("Arm ready")

    def move_shoulder(self, angle):
        print(f"Shoulder {self.shoulder} -> {angle}")
        self.shoulder = angle
        time.sleep(1)

    def move_elbow(self, angle):
        print(f"Elbow {self.elbow} -> {angle}")
        self.elbow = angle
        time.sleep(1)

    def open_hand(self):
        self.hand_open = True
        print("Hand OPEN")

    def close_hand(self):
        self.hand_open = False
        print("Hand CLOSED")

arm = HydraulicArm()

arm.move_shoulder(45)
arm.move_elbow(90)

arm.move_shoulder(20)
arm.move_elbow(30)
arm.open_hand()
arm.close_hand()

arm.move_shoulder(90)
arm.move_elbow(45)
arm.open_hand()

print("Done")