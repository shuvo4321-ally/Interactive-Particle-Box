from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width, W_Height = 500, 500
points = []
speeds = []
directions = []
colors = []
blink_states = []
frozen = False
increment = 0.01
background_color = [0, 0, 0]

class Point:
    def __init__(self, x, y, dx, dy, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color

def draw_points(point, size):
    glPointSize(size)
    glBegin(GL_POINTS)
    glColor3f(*point.color)
    glVertex2f(point.x, point.y)
    glEnd()

def update_points():
    for point in points:
        point.x += point.dx
        point.y += point.dy
        if point.x >= W_Width/2 or point.x <= -W_Width/2:
            point.dx *= -1
        if point.y >= W_Height/2 or point.y <= -W_Height/2:
            point.dy *= -1

def increase_speed():
    for point in points:
        point.dx *= 2
        point.dy *= 2

def decrease_speed():
    for point in points:
        point.dx /= 2
        point.dy /= 2

def blink_points():
    for i, point in enumerate(points):
        if blink_states[i]:
            point.color = [0, 0, 0]  # Background color for blinking effect
        else:
            point.color = colors[i]
        blink_states[i] = not blink_states[i]

def generate_point(x, y):
    dx = random.choice([-0.05, 0.05])
    dy = random.choice([-0.05, 0.05])
    color = [random.random() for _ in range(3)]
    point = Point(x, y, dx, dy, color)
    points.append(point)
    speeds.append((dx, dy))
    colors.append(color)
    blink_states.append(False)

def convert_coordinate(x, y):
    a = x - (W_Width / 2)
    b = (W_Height / 2) - y
    return a, b

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(*background_color, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)

    for point in points:
        draw_points(point, 5)

    glutSwapBuffers()

def update_background_color(direction):
    global background_color, increment
    if direction == 'lighten':
        for i in range(3):
            if background_color[i] < 1.0:
                background_color[i] += increment
        if all(color >= 1.0 for color in background_color):
            glutIdleFunc(None)  # Stop updating when fully light
    elif direction == 'darken':
        for i in range(3):
            if background_color[i] > 0.0:
                background_color[i] -= increment
        if all(color <= 0.0 for color in background_color):
            glutIdleFunc(None)  # Stop updating when fully dark

def init():
    glClearColor(*background_color, 1)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104, 1, 1, 1000.0)

def keyboard(key, x, y):
    global frozen
   
    if key == b' ':  # Spacebar to freeze/unfreeze
        frozen = not frozen

def special(key, x, y):
    if not frozen:
        if key == GLUT_KEY_UP:
            increase_speed()
        elif key == GLUT_KEY_DOWN:
            decrease_speed()

def mouse(button, state, x, y):
    global frozen
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN and not frozen:
        c_X, c_Y = convert_coordinate(x, y)
        generate_point(c_X, c_Y)
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN and not frozen:
        blink_points()

def timer(value):
    if not frozen:
        update_points()
        glutPostRedisplay()
    glutTimerFunc(16, timer, 0)

glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
wind = glutCreateWindow(b"OpenGL Moving Points")
init()
glutDisplayFunc(display)
glutIdleFunc(update_points)
glutKeyboardFunc(keyboard)
glutSpecialFunc(special)
glutMouseFunc(mouse)
glutTimerFunc(0, timer, 0)
glutMainLoop()
