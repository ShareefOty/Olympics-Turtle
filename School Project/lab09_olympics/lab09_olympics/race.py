import turtle
import random
import math

from setup import *


def run_the_race(runner_count):
 
    
    writer = turtle.Turtle()
    writer.hideturtle()
    
    # go to printing text
    writer.pu()
    writer.goto(-100,-150)

    setup_sprinting()


    # Create as many competitors as user indicated.


    competitors=[]
    starter_race=-250
    for i in range (runner_count):
                
        # Making a competitor creates a turtle (and returns it)
        # Create the competitors, then place into a list.
        
        competitors.append(make_competitor(starter_race,starter_row,['black',competitor_info[i][1]]))
        starter_race +=65
        competitors[i].penup()
        




    # Write the name of each competitor below their turtle
    # Left-most turtle (hard-coded above as Daisy)
    starter_2=-275
    for i in range(runner_count):
        writer.pu()
        writer.goto(starter_2,starter_row-50)
        starter_2+=65
        writer.pd()
        writer.write(competitor_info[i][0],font=('Arial',24,'normal'))



    # keep track of how many finished and in what order
    finished = []
    
    # once they have all crossed the finish line, the race is over
    while len(finished) < runner_count:
        

      
        for i in range(runner_count):
            # Move only if not finished the race
            if competitor_info[i][0] not in finished:
                # move forward a random amount
                delta = random.randint(1,9)
                competitors[i].forward(delta)
                # check if they crossed the finish line
                if competitors[i].pos()[1] >= finish_row:
                    finished.append(competitor_info[i][0])
                    

    writer.pu()
    writer.goto(-20,finish_row+50)
    writer.pd()
    writer.write(f'The winner is {finished[0]}!!',False,font=('Arial',24,'normal'))

    return finished

if __name__ == '__main__':
    run_the_race(3)
