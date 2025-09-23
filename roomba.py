

class Roomba:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.max_x = 10
        self.max_y = 10
        self.directions = ['N', 'E', 'S', 'W']  # clockwise order
        self.direction_idx = 0  # initial direction is North (index 0)

    def action(self, command):
        for cmd in command:
            if cmd == 'L':
                self.turn_left()
            elif cmd == 'R':
                self.turn_right()
            elif cmd == 'F':
                self.move_forward()
            elif cmd == '?':
                print(f"Current position: ({self.x}, {self.y}), Facing: {self.directions[self.direction_idx]}")
            else:
                print("Invalid command")

    def turn_left(self):
        self.direction_idx = (self.direction_idx - 1) % 4

    def turn_right(self):
        self.direction_idx = (self.direction_idx + 1) % 4

    def move_forward(self):
        direction = self.directions[self.direction_idx]
        if direction == 'N':
            if self.y < self.max_y:
                self.y += 1
            else:
                print("Reached northern boundary")
        elif direction == 'E':
            if self.x < self.max_x:
                self.x += 1
            else:
                print("Reached eastern boundary")
        elif direction == 'S':
            if self.y > 0:
                self.y -= 1
            else:
                print("Reached southern boundary")
        elif direction == 'W':
            if self.x > 0:
                self.x -= 1
            else:
                print("Reached western boundary")

        

if __name__ == "__main__":
    roomba = Roomba()
    commands = "F?F?R?F?F?"
    roomba.action(commands)