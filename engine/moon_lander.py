# complex polygon as shape

import turtle
import engine
import time
import math

WIDTH = 640
HEIGHT = 480
ground1 = ((-320, 120), (-280, 41), (-240, 27),
    (-200, 59), (-160, 25), (-120, 43), (-80, 56),
    (-40, 20), (0, 20), (40, 20), (80, 44),
    (120, 28), (160, 66), (200, 29), (240, 64),
    (280, 34), (320, 140), (320, 0), (-320,0) )
GRAVITY = 0.004
SUNRADIUS = 300
ROCKETBASE = 10
def makeSunShape():
    turtle.home()
    turtle.begin_poly()
    turtle.circle(SUNRADIUS)
    turtle.end_poly()
    
    poly = turtle.get_poly()
    turtle.register_shape('cercle', poly)

def makeGroundShape(level):
    s = turtle.Shape("compound")
    ground = level
    s.addcomponent(ground, "black", "black")
    turtle.register_shape('ground', s)

def makeRocketShape():
    B = ROCKETBASE
    turtle.home()
    turtle.lt(180)
    turtle.begin_poly()
    s = turtle.Shape("compound")
    rocketShape = ((1/2*B,0), (1/2*B,B), (0,3*B), (-1/2*B,B), 
    (-1/2*B,0), (-1/2*B, 0), (-3/2*B,-B), (-1/2*B, -B),
    (-1/2*B, -2*B), (1/2*B,-2*B), (1/2*B,-B), (3/2*B,-B) )
    turtle.end_poly()
    s.addcomponent(rocketShape, "black", "black")
    turtle.register_shape('rocket', s)   

def makeRocketBurnShape():
    B = ROCKETBASE
    turtle.home()
    turtle.begin_poly()
    s = turtle.Shape("compound")
    rocketShape = ((1/2*B,0), (1/2*B,B), (0,3*B), (-1/2*B,B), 
    (-1/2*B,0), (-1/2*B, 0), (-3/2*B,-B), (-1/2*B, -B),
    (-1/2*B, -2*B), (1/2*B,-2*B), (1/2*B,-B), (3/2*B,-B) )
    turtle.end_poly()
    #add rocket to the "compound shape"
    s.addcomponent(rocketShape, "black", "black")
    
    #make motor
    turtle.home()
    turtle.begin_poly()
    motorShape = ((0,-2*B), (-1/2*B,-5/2*B), (1/2*B,-5/2*B))
    turtle.end_poly()
    s.addcomponent(motorShape, "red", "red")
    turtle.register_shape('rocketBurn', s)


class Rocket(engine.GameObject):
    deltay = 0
    time = 0
    angle = 90
    def __init__(self):
        makeRocketShape()
        makeRocketBurnShape()
        super().__init__(0, 0, 0, 0, 'rocket', 'black')
        
    def delete(self):
        super().delete()
        engine.exit_engine()
        
    def isoob(self):

        if self.y >= HEIGHT//2 or self.y <= -HEIGHT//2:
            return True
        else:
            return False
    def throttleUp(self):
        if rocket.shape == 'rocket': rocket.shape = 'rocketBurn'
        self.deltay = self.deltay + 1/2 if self.angle % 360 > 180 else self.deltay - 1/2
        self.deltax = math.cos(math.radians(self.angle))*4
        self.time = 30
    def throttleLeft(self):
        self.angle += 1
    def throttleRight(self):
        self.angle -= 1
    def move(self):
        self.deltay += GRAVITY
        self.y -= self.deltay
        self.x = self.x + self.deltax
        if self.shape == 'rocketBurn' and self.time == 0 :
            self.shape = 'rocket'
        else:
            self.time -= 1
        if self.y <= -HEIGHT / 2 + 20:
            if self.deltay >= 2:
                banner("Crash")
            else:
                banner("Win")
        if self.x >= WIDTH//2 or self.x <= -WIDTH//2:
            self.x = -self.x
    def heading(self):
        return self.angle

    def get_bounding_circle(self):
        return self.x, self.y, 30
        
class Sun(engine.GameObject):
    def __init__(self):
        makeSunShape()
        super().__init__(0, HEIGHT//2 -70, 0, 0, 'cercle', 'yellow')
    def get_pos(self):
        return (self.x, self.get_radius()+self.y)
    def get_radius(self):
        return 300
    def get_bounding_circle(self):
        x, y = self.get_pos()
        return x, y, self.get_radius()
    def isoob(self):
        return False
    def heading(self):
        return 90

class Ground(engine.GameObject):
    points = None
    def __init__(self, points):
        self.points = points
        makeGroundShape(self.points)
        super().__init__(0, -HEIGHT/2, 0, 0, 'ground', 'black')

    def heading(self):
        return 90
        """   
   def compute_yminmax(self, xmin, xmax):
        ite = 0
        while not self.points[ite][0] <= xmin <= self.points[ite+1][0]:
            if not self.points[ite][0] <= xmax <= self.points[ite+1][0]:
                ya = 
        x1, y1 = self.points[ite]
        x2, y2 = self.points[ite+1]
        coef = (y2-y2)/(x2-x1)
        xa = 
    """
        
def keyboard_cb(key):
    if key == 'Up':
        rocket.throttleUp()
    if key == 'Right':
        rocket.throttleRight()
    if key == 'Left':
        rocket.throttleLeft()
        
#write the string "s" on the screen
def banner(s):
	turtle.home()
	turtle.color('black')
	turtle.write(s, True, align='center', font=('Arial', 48, 'italic'))
	time.sleep(3)
	turtle.undo()

#define the collision between 2 objets with surounding circles
def colli_circle(obj1, obj2):
    x1, y1, rad1 = obj1.get_bounding_circle()
    x2, y2, rad2 = obj2.get_bounding_circle()
    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return d < (rad1 + rad2)
#define what to do if a collision occurs
def collision_LR(obj1, obj2):
    if colli_circle(obj1, obj2):
        banner("Burn!")
        sleep(3)
        rocket.delete()
def collision_RL(obj1, obj2):
    collision_LR(obj2, obj1)

    
if __name__ == '__main__':
    engine.init_screen(WIDTH, HEIGHT)
    engine.init_engine()
    engine.set_keyboard_handler(keyboard_cb)
    
    global rocket
    rocket = Rocket()
    sun = Sun()
    ground = Ground(ground1)
    engine.register_collision(Rocket, Sun, collision_LR)
    engine.register_collision(Rocket, Sun, collision_RL)
    engine.add_obj(rocket)
    engine.add_obj(sun)
    engine.add_obj(ground)
    engine.engine()

