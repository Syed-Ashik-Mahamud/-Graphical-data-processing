from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Function to draw a colored rectangle
def draw_colored_rectangle(x, y, width, height, color):
    glColor3f(*color)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

# Function to display the student ID
def display_student_id():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    digit_width = 50
    digit_height = 100
    spacing = 10

    student_id = "20301124"
    digit_colors = [(1.0, 0.0, 0.0),  # Red
                    (0.0, 1.0, 0.0),  # Green
                    (0.0, 0.0, 1.0),  # Blue
                    (1.0, 1.0, 0.0)]  # Yellow

    x = 0.0
    for digit in student_id:
        draw_colored_rectangle(x, 0.0, digit_width, digit_height, digit_colors[int(digit)])
        x += digit_width + spacing

    glFlush()

# Initialize OpenGL
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 100)
glutCreateWindow(b"Student ID")

# Set the clear color
glClearColor(1.0, 1.0, 1.0, 1.0)

# Register the display function
glutDisplayFunc(display_student_id)

# Set the viewport
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0.0, 500, 0.0, 100, -1.0, 1.0)

# Start the main loop
glutMainLoop()
