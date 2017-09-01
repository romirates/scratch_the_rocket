# complex polygon as shape

import turtle
import engine
import time

WIDTH = 640
HEIGHT = 480
class Rocket(engine.GameObject):
    def __init__(self):
        super().__init__(0, 0, +1, 0, 'rocket', 'black')
        self.speed = 0
    def heading(self):
        return 180
    def delete(self):
        super().delete()
        engine.exit_engine()
    def move(self):
        if self.y >= HEIGHT/4 :
            banner("BOUM!")
            self.delete()
        self.y -= self.speed
        self.speed += 0.05


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
        rocket.shape = "rocket_burn"
        rocket.speed -= 1

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
    B = 50
    turtle.begin_poly()
    turtle.fd(B)
    turtle.rt(45)
    turtle.fd(B*1/4)
    turtle.rt(90)
    turtle.fd(B*1/4)
    turtle.rt(45)
    turtle.fd(B)
    
    turtle.end_poly()
    poly = turtle.get_poly()
    turtle.register_shape('rocket', poly)   
    
def makeRocketBurn():
    B = 50
    turtle.begin_poly()
    turtle.fd(B)
    turtle.rt(45)
    turtle.fd(B*1/4)
    turtle.rt(90)
    turtle.fd(B*1/4)
    turtle.rt(45)
    turtle.fd(B)
    """
    turtle.lt(45)
    turtle.fd(B*1/8-1)
    turtle.end_poly()
    """
    poly = turtle.get_poly()
    turtle.register_shape('rocket_burn', poly)
    
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
"""
def makeshape():
	B = 25				# base unit size
	turtle.begin_poly()
	turtle.fd(B)			# roof
	turtle.rt(45)
	turtle.fd(B * 3/4)		# windshield
	turtle.lt(45)
	turtle.fd(B)			# hood
	turtle.rt(90)
	turtle.fd(B * 3/4)		# front
	turtle.rt(90)
	turtle.fd(B * 1/7)
	turtle.lt(90)
	turtle.circle(-B/2, 180)	# front tire
	turtle.lt(90)
	turtle.fd(B)
	turtle.lt(90)
	turtle.circle(-B/2, 180)	# back tire
	turtle.lt(90)
	turtle.fd(B * 1/7)
	turtle.rt(90)
	turtle.fd(B * 5/6)		# back
	turtle.end_poly()
	poly = turtle.get_poly()
	turtle.register_shape('car', poly)
"""
"""def makeshape():
    B = 50
    turtle.begin_poly()
    turtle.fd(B)
    turtle.rt(45)
    turtle.fd(B*1/4)
    turtle.rt(90)
    turtle.fd(B*1/4)
    turtle.rt(45)
    turtle.fd(B)
    turtle.rt(45)
    turtle.fd(B*1/8)
    turtle.lt(10)
    turtle.fd(10)
    poly = turtle.get_poly()
    turtle.register_shape('rocket', poly)
    """

