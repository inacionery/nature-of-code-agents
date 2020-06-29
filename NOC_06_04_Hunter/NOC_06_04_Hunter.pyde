# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

# Implements Craig Reynold's autonomous steering behaviors
# One vehicle "seeks"
# See: http://www.red3d.com/cwr/

from random import randint #######################################################################################

from Vehicle import Vehicle
from Food import Food

#adiciona uma nova comida no array de foods
def acrecetar_comida():
    foods.append(Food(random(width),random(height), PVector(0,0)))
        

def setup():
    global agente, foods, food1
    size(640, 360)
    velocity = PVector(0, 0)
    agente = Vehicle(width / 2, height / 2, velocity)

    quantidade = randint(0, 20)
    print(quantidade) ############################################################################################
    foods = [Food(random(width),random(height), PVector(0,0)) for x in range(quantidade)] ########################

def draw():
    background(255)
    
    #pontuação
    textSize(25)
    text('Pontos {}'.format(agente.hunted), 10, 30)
    fill(0, 0, 0)
    
    if (len(foods)>0):
        agente.hunt(foods[0])

        agente.display_food(foods[0]) #########################################################################
    agente.update()
    agente.display()
    
    if (len(foods)>0 and not foods[0].is_alive):
        foods.pop(0)
        
  
def keyTyped():
    #caso a tecla '+' precionada, chama a função acrecetar_comida()
    if key == '+':
        acrecetar_comida()
    