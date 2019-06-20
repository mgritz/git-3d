import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

campos = list((0,0,-10))
def handle_pygame_events() :
    redraw_required = False
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN :
            camchange = (0,0,0)
            dirchange = (0,0)

            assert event.type == pygame.KEYDOWN
            if event.key == ord('a') :
                camchange = (-1,0,0)
            if event.key == ord('d') :
                camchange = (1,0,0)
            if event.key == ord('w') :
                camchange = (0,1,0)
            if event.key == ord('s') :
                camchange = (0,-1,0)
            if event.key == pygame.K_LCTRL :
                camchange = (0,0,-1)
            if event.key == pygame.K_LSHIFT :
                camchange = (0,0,1)
            if event.key == pygame.K_UP or event.key == ord('k'):
                dirchange = (0,5)
            if event.key == pygame.K_DOWN or event.key == ord('j'):
                dirchange = (0,-5)
            if event.key == pygame.K_LEFT or event.key == ord('h'):
                dirchange = (-5,0)
            if event.key == pygame.K_RIGHT or event.key == ord('l'):
                dirchange = (5,0)

            if camchange != (0,0,0) :
                redraw_required = True
                glTranslatef(camchange[0], camchange[1], camchange[2])
                campos[0] += camchange[0]
                campos[1] += camchange[1]
                campos[2] += camchange[2]
                print(campos)

            if dirchange != (0,0) :
                redraw_required = True
                # get view orientation
                a = (GLfloat * 16)()
                mvm = glGetFloatv(GL_MODELVIEW_MATRIX, a)
                look_v = (a[2], a[6], a[10])
                up_v = (a[1], a[5], a[9])
                right_v = (a[0], a[4], a[8])

                dirchange_v = dirchange[0]
                dirchange_h = dirchange[1]

                glRotatef(dirchange_v, right_v[0], right_v[1], right_v[2])
                glRotatef(dirchange_h, up_v[0], up_v[1], up_v[2])

                mvm = glGetFloatv(GL_MODELVIEW_MATRIX, a)
                look_v = (a[2], a[6], a[10])
                print(look_v)

    return redraw_required
