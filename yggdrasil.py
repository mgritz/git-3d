from OpenGL.GL import *

def draw_diamond(p, size, color=(1,1,1)) :
    glBegin(GL_TRIANGLE_STRIP)
    glColor3fv(color)
    glVertex3f((p[0] + size/2), (p[1] + size/2), p[2])
    glVertex3f((p[0] - size/2), (p[1] + size/2), p[2])
    glVertex3f(p[0], p[1], p[2] - size)
    glVertex3f((p[0] + size/2), (p[1] - size/2), p[2])
    glVertex3f((p[0] - size/2), (p[1] - size/2), p[2])
    glVertex3f(p[0], p[1], p[2] + size)
    glVertex3f((p[0] + size/2), (p[1] + size/2), p[2])
    glVertex3f((p[0] + size/2), (p[1] - size/2), p[2])
    glVertex3f(p[0], p[1], p[2] - size)
    glVertex3f((p[0] - size/2), (p[1] + size/2), p[2])
    glVertex3f((p[0] - size/2), (p[1] - size/2), p[2])
    glVertex3f(p[0], p[1], p[2] + size)
    glEnd()

class YggCommit :
    def __init__(self, commit) :
        self.c = commit
        self.position = (0,0,0)
        self.color = (.5,.5,.5)

    def __hex2rgb(self, h) :
        h = h.lstrip('#')
        return tuple(int(h[i:i+2], 16) / 256 for i in (0, 2, 4))

    def setColorFromString(self, colorstring) :
        self.color = self.__hex2rgb(colorstring)

    def draw(self) :
        draw_diamond(self.position, 0.2, self.color)