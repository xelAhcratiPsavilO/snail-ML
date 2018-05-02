import turtle
import car as car
import camera

class Controller(object):

    def __init__(self, car = car):
        self.car = car
        turtle.setup(400,500)
        self.window = turtle.Screen()
        self.window.title('snAIl Controller')
        self.window.bgcolor('blue')

    def create_temp_photo(self):
        img_data = camera.grab_image_data()
        dir_path = camera.create_path("temp")
        camera.create_directory(dir_path)
        return camera.save_photo(dir_path, img_data)

    def up(self):
        self.car.forward(0.2)

    def down(self):
        self.car.reverse(0.2)

    def right(self):
        self.car.turn_right(0.2)

    def left(self):
        self.car.turn_left(0.2)

    def piv_right(self):
        self.car.pivot_right(0.2)

    def piv_left(self):
        self.car.pivot_left(0.2)

    def exit(self):
        self.window.bye()

def main():
    w = Controller()
    w.window.onkey(w.up, 'Up')
    w.window.onkey(w.down, 'Down')
    w.window.onkey(w.right, 'Right')
    w.window.onkey(w.left, 'Left')
    w.window.onkey(w.piv_right, '/')
    w.window.onkey(w.piv_left, '.')
    w.window.onkey(w.exit, 'q')
    w.window.listen()
    w.window.mainloop()

    pass

if __name__ == "__main__":
   main()