import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import random

def drawLine(x1 ,y1 ,x2 ,y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def randomWidth():
    glLineWidth(random.randint(1,10))


def main():
    if not glfw.init():
        return
    window = glfw.create_window(640, 480, "ラララ", None, None)
    if not window:
        glfw.terminate()
        return

    #init
    glfw.make_context_current(window)


    # loop
    while not glfw.window_should_close(window):

        glClear(GL_COLOR_BUFFER_BIT)
        randomWidth()
    
        drawLine(100.0, 400.0, 200.0, 400.0)
        drawLine(440.0, 400.0, 540.0, 400.0)
        drawLine(320.0, 350.0, 320.0, 330.0)
        drawLine(100.0, 400.0, 200.0, 400.0)
        drawLine(300.0, 200.0, 340.0, 200.0)
        
        glfw.swap_buffers(window)
        glfw.poll_events()
        glfw.swap_interval(2)
    glfw.terminate()

if __name__ == "__main__":
    main()