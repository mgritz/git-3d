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

nodes = dict()

class YggPosition :
    def __init__(self, p) :
        self.x = p[0]
        self.y = p[1]
        self.z = p[2]

    def toTuple(self) :
        return (self.x, self.y, self.z)

class YggCommit :
    def __init__(self, commit) :
        self.c = commit
        self.color = (.5,.5,.5)
        self.hasPosition = False

    def __hex2rgb(self, h) :
        h = h.lstrip('#')
        return tuple(int(h[i:i+2], 16) / 256 for i in (0, 2, 4))

    def setColorFromString(self, colorstring) :
        self.color = self.__hex2rgb(colorstring)

    def draw(self) :
        assert self.position.__class__ == YggPosition
        assert self.hasPosition
        draw_diamond(self.position.toTuple(), 0.2, self.color)

    def setPosition(self, p) :
        self.position = YggPosition(p)
        self.hasPosition = True

    def placeTree(self, head, level, parallel) :
        if self.hasPosition :
            return
        self.setPosition((head, parallel, level))
        par = parallel
        for p in self.c.parents :
            nodes[str(p)].placeTree(head, level + 1, par)
            par = par + 1
