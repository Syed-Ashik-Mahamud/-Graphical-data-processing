from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_points(x, y):
    glPointSize(3)
    glBegin(GL_POINTS)
    glColor3f(1, 0, 0)
    glVertex2f(x, y)
    glEnd()

def find_zone(dx, dy):
    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            return 0
        elif dx <= 0 and dy >=0:
            return 3
        elif dx >= 0 and dy <= 0:
            return 7
        elif dx <= 0 and dy <= 0:
            return 4
    elif abs(dx) < abs(dy):
        if dx >= 0 and dy >= 0:
            return 1
        elif dx <= 0 and dy >=0:
            return 2
        elif dx >= 0 and dy <= 0:
            return 6
        elif dx <= 0 and dy <= 0:
            return 5


def convert_to_zero(z, x, y):
    if z == 0:
        return x, y
    elif z == 1:
        return y, x
    elif z == 2:
        return y, -x
    elif z == 3:
        return -x, y
    elif z == 4:
        return -x, -y
    elif z == 5:
        return -y, -x
    elif z == 6:
        return -y, x
    elif z == 7:
        return x, -y

def convert_to_original_zone(z, x, y):
    if z == 0:
        return x, y
    elif z == 1:
        return y, x
    elif z == 2:
        return -y, x
    elif z == 3:
        return -x, y
    elif z == 4:
        return -x, -y
    elif z == 5:
        return -y, -x
    elif z == 6:
        return y, -x
    elif z == 7:
        return x, -y

def mid_point_line(x1, y1, x2, y2, z):
    dx = x2 - x1
    dy = y2 - y1

    d = (2 * dy) - dx
    dE = 2 * dy
    dNE = 2 * (dy - dx)

    x = x1
    y = y1

    while x < x2:
        cx, cy = convert_to_original_zone(z, x, y)
        draw_points(cx, cy)
        if d < 0:
            x += 1
            d += dE
        else:
            x += 1
            y += 1
            d += dNE


def draw_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    zone = find_zone(dx, dy)

    nx1, ny1 = convert_to_zero(zone, x1, y1) 
    nx2, ny2 = convert_to_zero(zone, x2, y2)

    mid_point_line(nx1, ny1, nx2, ny2, zone)

# Drawing line
def task_one():

    draw_line(100, 300, 200, 300)
    draw_line(200, 300, 200, 200)
    draw_line(100, 200, 200, 200)
    draw_line(100, 200, 100, 100)
    draw_line(200, 100, 100, 100)
    
    draw_line(300, 300, 300, 200)
    draw_line(300, 200, 400, 200)
    draw_line(400, 200, 400, 300)
    draw_line(400, 200, 400, 100)
    

    

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
   
    task_one()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"20301124-Task1") 
glutDisplayFunc(showScreen)

glutMainLoop()