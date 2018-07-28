class Car():
    def __init__(self, brand):
        self.brand = brand

    def get_brand(self):
        print(self.brand)

    def open_door(self,door_number):
        print("Opening Door " + str(door_number))

    def blinker_control(self,left_blinker,right_blinker):
        self.left_blinker = left_blinker
        self.right_blinker = right_blinker
        print("L:" + str(self.left_blinker))
        print("R:" + str(self.right_blinker))