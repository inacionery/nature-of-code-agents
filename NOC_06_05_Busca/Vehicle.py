# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# The "Vehicle" class

class Vehicle():

    def __init__(self, x, y, vel, w):
        self.acceleration = PVector(0, 0)
        self.velocity = vel
        self.position = PVector(x, y)
        self.r = 5
        self.maxspeed = 5
        self.maxforce = 0.2
        self.hunted = 0
        self.scl = w #Escala para o grid

    # Method to update location
    def update(self):
        # Update velocity
        self.velocity.add(self.acceleration)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        # Reset accelerationelertion to 0 each cycle
        self.acceleration.mult(0)

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

    # A method that calculates a steering force towards a target
    # STEER = DESIRED MINUS VELOCITY
    
    def seek(self, target):

        # A vector pointing from the location to the target
        desired = target - self.position

        # Scale to maximum speed
        desired.setMag(self.maxspeed)

        steer = desired - self.velocity
        steer.limit(self.maxforce)  # Limit to maximum steering force

        self.applyForce(steer)
        
    #Metodo para cacar um o alvo
    def hunt(self, target):
        
        #adicao um atributo on the Fly
        self.alvo = target
        
        # A vector pointing from the location to the target
        desired = self.alvo.position - self.position
        d = desired.mag()
        # Scale with arbitrary damping within 100 pixels
        if ((d > 1)and(d < 100)):
            m = map(d, 0, 100,1, self.maxspeed)
            desired.setMag(m)
        else:
            desired.setMag(self.maxspeed)

        # Steering = Desired minus velocity
        steer = desired - self.velocity
        steer.limit(self.maxforce)  # Limit to maximum steering force
        self.applyForce(steer)
        
        #teste de contato com o alvo
        if(d < 1):
            print(d)
            self.comer_alvo()
            steer.limit(self.maxforce)
            self.velocity=(PVector(0,0))            
    
    #Metodo para 'Comer' outro objeto
    def comer_alvo(self):
        self.alvo.dead()
        del self.alvo
        self.hunted += 1

    def display(self):
        # Draw a triangle rotated in the direction of velocity
        theta = self.velocity.heading() + PI / 2
        fill(51)
        #noStroke()
        #strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rect(0, 0, self.scl, self.scl)
            # rotate(theta)
            # beginShape()
            # vertex(0, -self.r * 2)
            # vertex(-self.r, self.r * 2)
            # vertex(self.r, self.r * 2)
            # endShape(CLOSE)

    def display_food(self, target):
        #adicao um atributo on the Fly
        self.alvo = target
       # Draw a triangle rotated in the direction of velocity
        theta = self.velocity.heading() + PI / 2
        fill(127)
        #noStroke()
    #    strokeWeight(1)
        with pushMatrix():
            translate(self.alvo.position.x, self.alvo.position.y)
            rect(0, 0, self.scl, self.scl)  # A comida esta do tamanho de 1 espaco do grid
