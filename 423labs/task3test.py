from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# This function is used to draw lines.
def draw_lines():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)    
    
    glVertex2f(50, 100)
    glVertex2f(100, 100)

    glVertex2f(50, 200)
    glVertex2f(100, 200)

    glVertex2f(50, 300)
    glVertex2f(100, 300)
    
    glVertex2f(50, 100)
    glVertex2f(50, 200)

    glVertex2f(100, 200)
    glVertex2f(100, 300)

    print("2")


    glColor3f(0.0, 1.0, 0.0)  
    
    glVertex2f(150, 100)
    glVertex2f(200, 100)

    glVertex2f(150, 300)
    glVertex2f(200, 300)
    
    glVertex2f(150, 100)
    glVertex2f(150, 300)

    glVertex2f(200, 100)
    glVertex2f(200, 300)

    print("0")


    glColor3f(0.0, 0.0, 1.0)  
    glVertex2f(250, 100)
    glVertex2f(300, 100)

    glVertex2f(250, 200)
    glVertex2f(300, 200)

    glVertex2f(250, 300)
    glVertex2f(300, 300)
    
    glVertex2f(300, 100)
    glVertex2f(300, 200)

    glVertex2f(300, 200)
    glVertex2f(300, 300)

    print("3")
    

    glColor3f(0.0, 1.0, 0.0)  
   
    glVertex2f(350, 100)
    glVertex2f(400, 100)

    glVertex2f(350, 300)
    glVertex2f(400, 300)
    
    glVertex2f(350, 100)
    glVertex2f(350, 300)

    glVertex2f(400, 100)
    glVertex2f(400, 300)
    
    print("0")


    glColor3f(0.0, 1.0, 1.0)  
    
    glVertex2f(500, 100)
    glVertex2f(500, 300)
   
    glVertex2f(450, 250)
    glVertex2f(500, 300)

    print("1")


    glColor3f(0.0, 1.0, 1.0)  
    
    glVertex2f(600, 100)
    glVertex2f(600, 300)

    glVertex2f(550, 250)
    glVertex2f(600, 300)

    print("1")


    glColor3f(1.0, 0.0, 1.0)  
    
    glVertex2f(650, 100)
    glVertex2f(700, 100)

    glVertex2f(700, 200)
    glVertex2f(650, 200)

    glVertex2f(650, 300)
    glVertex2f(700, 300)
    
    glVertex2f(700, 300)
    glVertex2f(700, 200)
    
    glVertex2f(650, 200)
    glVertex2f(650, 100)

    print("2")


    glColor3f(1.0, 1.0, 0.0)  
    
    glVertex2f(800, 100)
    glVertex2f(800, 300)
    
    glVertex2f(800, 300)
    glVertex2f(750, 200)
    
    glVertex2f(750, 200)
    glVertex2f(800, 200)

    print("4")

    glEnd()


def iterate():
    glViewport(0, 0, 900, 400)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 900, 0.0, 400, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    
    draw_lines()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)


glutInitWindowSize(900, 400)
glutInitWindowPosition(0, 0)


wind = glutCreateWindow(b"Task03: Student ID")

glutDisplayFunc(showScreen)

glutMainLoop()