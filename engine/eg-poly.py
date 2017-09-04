# complex polygon as shape

import turtle
import engine
import time

WIDTH = 640
HEIGHT = 480
class Rocket(engine.GameObject):
    def __init__(self):
        super().__init__(0, 0, 0, 0, 'rocket', 'black')
        self.speed = 0
        self.time = 0
    def delete(self):
        super().delete()
        engine.exit_engine()
    def isoob(self):
        if super().isoob():
            self.x = -self.x
    def move(self):
        if self.y >= HEIGHT/4 :
            banner("BOUM!")
            self.delete()
        self.y -= self.speed
        self.x = self.x + self.deltax
        self.speed += 0.04
        if self.shape == 'rocketBurn' and self.time == 0 :
            self.shape = 'rocket'
        else:
            self.time -= 1
        if self.y <= -HEIGHT / 2 + 20:
            if self.speed >= 2:
                banner("Crash")
            else:
                banner("Win")
    def heading(self):
        return 90 - 4*self.deltax
        
class Sun(engine.GameObject):
    def __init__(self):
        super().__init__(-10, (HEIGHT/2)-40, 0, 0, 'cercle', 'yellow')
class Ground(engine.GameObject):
    def __init__(self):
        super().__init__(0, -HEIGHT/2, 0, 0, 'ground', 'black')
    def heading(self):
        return 90

def keyboard_cb(key):
    if key == 'space':
        if rocket.shape == 'rocket': rocket.shape = 'rocketBurn'
        rocket.speed -= 1/2
        rocket.time = 30
    if key == 'Right':
        rocket.deltax += 1/2
    if key == 'Left':
        rocket.deltax -= 1/2

def banner(s):
	turtle.home()
	turtle.color('black')
	turtle.write(s, True, align='center', font=('Arial', 48, 'italic'))
	time.sleep(3)
	turtle.undo()

def makeSun():
    turtle.home()
    turtle.begin_poly()
    turtle.circle(50)
    turtle.end_poly()
    
    poly = turtle.get_poly()
    turtle.register_shape('cercle', poly)

def makeGround():
    s = turtle.Shape("compound")
    ground = ((-320, 120), (-280, 41), (-240, 27),
    (-200, 59), (-160, 25), (-120, 43), (-80, 56),
    (-40, 20), (0, 20), (40, 20), (80, 44),
    (120, 28), (160, 66), (200, 29), (240, 64),
    (280, 34), (320, 140), (320, 0), (-320,0) )
    s.addcomponent(ground, "black", "black")
    turtle.register_shape('ground', s)
    
def makeRocket():
    #make rocket shape
    B = 10
    turtle.home()
    turtle.lt(180)
    turtle.begin_poly()
    s = turtle.Shape("compound")
    rocketShape = ((B,0), (2*B,0), (2*B,B), (3*B,B), 
    (2*B,2*B), (2*B, 3*B), (3/2*B,5*B), (B, 3*B),
    (B, 2*B), (0,B), (B,B), (B,0) )
    turtle.end_poly()
    s.addcomponent(rocketShape, "black", "black")
    turtle.register_shape('rocket', s)   
    
def makeRocketBurn():
    #make rocket shape
    B = 10
    turtle.home()
    turtle.begin_poly()
    s = turtle.Shape("compound")
    rocketShape = ((B,0), (2*B,0), (2*B,B), (3*B,B), 
    (2*B,2*B), (2*B, 3*B), (3/2*B,5*B), (B, 3*B),
    (B, 2*B), (0,B), (B,B), (B,0) )
    turtle.end_poly()
    #add rocket to the "compound shape"
    s.addcomponent(rocketShape, "black", "black")
    
    #make motor
    turtle.home()
    turtle.begin_poly()
    motorShape = ((3/2*B,0), (B,-1/2*B), (2*B,-1/2*B))
    turtle.end_poly()
    s.addcomponent(motorShape, "red", "red")
    turtle.register_shape('rocketBurn', s)
    
if __name__ == '__main__':
    engine.init_screen(WIDTH, HEIGHT)
    engine.init_engine()
    makeRocket()
    makeRocketBurn()
    makeSun()
    makeGround()
    engine.set_keyboard_handler(keyboard_cb)
    global rocket
    rocket = Rocket()
    engine.add_obj(rocket)
    engine.add_obj(Sun())
    engine.add_obj(Ground())
    engine.engine()

