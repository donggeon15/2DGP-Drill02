from pico2d import *
import math

open_canvas()
 
# fill here
grass = load_image('grass.png')
character = load_image('character.png')


x = 0
y = 80
set = 0
r = 200
x2 = 400
y2 = 300
d = 0
count = 0
xx = 0
yy = 0
while (True):
    clear_canvas_now()
    grass.draw_now(400,30)

    if (set == 0): 
        if (y == 80):
            if (x < 780):
                character.draw_now(x,y)
                x = x + 20

        if (x == 780):
            if (y < 540):
                character.draw_now(x,y)
                y = y + 20

        if (y == 540):
            if (x >= 0):
                character.draw_now(x,y)
                x = x - 20

        if (x == 0):
            if (y > 80):
                character.draw_now(x,y)
                y = y - 20

        if (x == 0):
            if (y == 80):
                set = 1


    if (set == 1):
        xx = x2 + (r * math.cos(d))
        yy = y2 + (r * math.sin(d))
        character.draw_now(xx, yy)
        d = d + ((1/60)*math.pi)
        count = count + 1
        
        if (count == 120):
            set = 0
            d = 0
            count = 0
        

    
    delay(0.001)


close_canvas()
