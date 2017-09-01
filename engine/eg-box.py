# basic moving box

import engine
import random
WIDTH = 640
HEIGHT = 480
speed = 0
class Box(engine.GameObject):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 'square', 'red')
    def move(self):
        global speed
        self.y -= speed
        speed += 0.005
def keyboard_cb(key):
        if key == 'space':
            global speed 
            speed -= 1
if __name__ == '__main__':
    engine.init_screen(WIDTH, HEIGHT)
    engine.init_engine()
    box = Box()
    engine.set_keyboard_handler(keyboard_cb)
    engine.add_obj(box)
    engine.engine()
    
