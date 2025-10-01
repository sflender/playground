# source: https://jigarius.com/blog/shopify-software-developer-interview


class Ship:
    def __init__(self):
        self.x = 0  # should be within (-5,5)
        self.y = 0  # should reach 250
        self.speed = 0

    def check_position(self):
        print(f"current position: x={self.x}, y={self.y}, speed={self.speed}")
        if self.x<-5 or self.x>5:
            print("wrong trajectory")
        if self.y>250:
            print("you have crossed the destination")
        if self.y==250:
            print("you have reached the destination")

    def update(self, action):

        if action=="W":
            if self.speed==5:
                print("maximum speed")
            else:
                self.speed += 1
            self.y += self.speed
            self.check_position()

        elif action == "S":
            if self.speed==1:
                print("minimum speed")
            else:
                self.speed -= 1
            self.y += self.speed
            self.check_position()

        elif action == "A":
            self.x-=1
            self.y += self.speed
            self.check_position()

        elif action == "D":
            self.x+=1
            self.y += self.speed
            self.check_position()

        else:
            print("invalid action")


if __name__ == "__main__":
    ship = Ship()
    actions = ["W", "W", "W", "A", "W", "D", "D", "D", "D", "D", "D", "S", "S", "S", "S"]
    for action in actions:
        ship.update(action)
        # print(f"current position: x={ship.x}, y={ship.y}, speed={ship.speed}")