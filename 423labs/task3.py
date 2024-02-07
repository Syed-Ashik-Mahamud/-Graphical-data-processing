import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

def draw_student_id(student_id):
  """Draws the student ID with different colors."""
  glClearColor(0.0, 0.0, 0.0, 1.0)
  glClear(gl.GL_COLOR_BUFFER_BIT)

  # Set the colors for each digit.
  colors = [
      (1.0, 0.0, 0.0),  # Red
      (0.0, 1.0, 0.0),  # Green
      (0.0, 0.0, 1.0),  # Blue
      (1.0, 1.0, 0.0),  # Yellow
      (0.0, 1.0, 1.0),  # Cyan
      (1.0, 0.0, 1.0),  # Magenta
  ]

  for i, digit in enumerate(student_id):
    glColor3fv(colors[i])
    glutSolidSphere(10, 10, 10)

def main():
  glutInit()
  glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)
  glutInitWindowSize(500, 500)
  glutCreateWindow("Student ID")
  glutDisplayFunc(draw_student_id)
  glutMainLoop()

if __name__ == "__main__":
  main()