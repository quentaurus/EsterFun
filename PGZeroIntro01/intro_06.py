#######################################################################
# From https://pygame-zero.readthedocs.io/en/stable/introduction.html #
#######################################################################
import pgzrun

WIDTH = 500
HEIGHT = 500

alien1 = Actor('alien')
alien1.topleft = 10, 10

alien2 = Actor('alien')
alien2.topleft = 20, 50

dx1 = 3
dy1 = 2

dx2 = 2
dy2 = 3

def draw():
    screen.clear()
    alien1.draw()
    alien2.draw()

def update(dt): # dt is ellapsed time in seconds since last update
    global dx1, dy1, dx2, dy2
    # print("Ellapsed time: " + str(1/dt))
    alien1.left += dx1
    alien1.top += dy1
    alien2.left += dx2
    alien2.top += dy2

    if (alien1.right > WIDTH) | (alien1.left < 0):
        dx1 = -dx1

    if (alien1.bottom > HEIGHT) | (alien1.top < 0):
        dy1 = -dy1

    if (alien2.right > WIDTH) | (alien2.left < 0):
        dx2 = -dx2

    if (alien2.bottom > HEIGHT) | (alien2.top < 0):
        dy2 = -dy2

def on_mouse_down(pos):
    if alien1.collidepoint(pos):
        set_alien1_hurt()

    if alien2.collidepoint(pos):
        set_alien2_hurt()

def set_alien1_hurt():
    alien1.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien1_normal, 0.5)

def set_alien2_hurt():
    alien2.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien2_normal, 0.5)

def set_alien1_normal():
    alien1.image = 'alien'

def set_alien2_normal():
    alien2.image = 'alien'

pgzrun.go()