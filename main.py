import OpenGL.GL as GL
import OpenGL.GLUT as GLUT
import glfw
import random
import sys

# Bubble class
class Bubble:
    def __init__(self):
        self.x = random.uniform(-1.0, 1.0)
        self.y = random.uniform(-1.0, 1.0)
        self.z = random.uniform(-1.0, -10.0)  # Depth in 3D space
        self.radius = random.uniform(0.05, 0.2)
        self.color = (random.random(), random.random(), random.random(), 0.5)  # Random transparent color

    def draw(self):
        GL.glPushMatrix()
        GL.glTranslatef(self.x, self.y, self.z)
        GL.glColor4f(1.0, 1.0, 1.0, 0.5)  # Transparent color
        GLUT.glutSolidSphere(self.radius, 20, 20)
        GL.glPopMatrix()

# Initialize OpenGL
def initialize():
    if not glfw.init():
        return
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    window = glfw.create_window(800, 600, b"Transparent 3D Bubble Screensaver", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)  
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glEnable(GL.GL_BLEND)
    GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)
    return window

# Display function
def display(window, bubbles):
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    GL.glLoadIdentity()

    for bubble in bubbles:
        bubble.draw()

    glfw.swap_buffers(window)

# Create bubbles
bubbles = [Bubble() for _ in range(50)]

if __name__ == '__main__':
    windows =initialize()

    if not windows:
        sys.exit()

    while not glfw.window_should_close(windows):
        display(windows, bubbles)
        glfw.poll_events()

    glfw.terminate()