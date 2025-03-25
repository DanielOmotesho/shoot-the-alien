import pgzrun
import random 

WIDTH=500
HEIGHT=500
TITLE="OUTPUTWINDOW"

message=""
alien=Actor("alien.png")

def draw():
    screen.clear()
    #screen.fill("blue")
    screen.blit("bg.png",(0,0))
    alien.draw()
    screen.draw.text(message,center=(300,10),fontsize=35)

def position():
    alien.x=random.randint(50,450)
    alien.y=random.randint(50,450)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message="GOOD SHOT"
        position()
    else:
        message="BAD SHOT"

position()
pgzrun.go()

    


