from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

a = 0
cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def prisma(raioInferior,raioSuperior,H,N):
    pontosBaseSuperior = []
    pontosBaseInferior = []
    angulo = (2*math.pi)/N

    glPushMatrix()
    glRotatef(a,0.0,1.0,0.0)
    glRotatef(-110,1.0,0.0,0.0)
    glColor3fv(cores[0])

    # BASE INFERIOR
    glBegin(GL_POLYGON)
    for i in range(0,N):
        x = raioInferior * math.cos(i*angulo)
        y = raioInferior * math.sin(i*angulo)
        pontosBaseInferior += [ (x,y) ]
        glVertex3f(x,y,0.0)
    glEnd()

    # BASE SUPERIOR
    glBegin(GL_POLYGON)
    for i in range(0,N):
        x = raioSuperior * math.cos(i*angulo)
        y = raioSuperior * math.sin(i*angulo)
        pontosBaseSuperior += [ (x,y) ]
        glVertex3f(x,y,H)
    glEnd()

    # LATERAIS
    for i in range(0,N):
        glBegin(GL_QUADS)
        glColor3fv(cores[(i+1)%len(cores)])
        glVertex3f(pontosBaseInferior[i][0],pontosBaseInferior[i][1],0.0)
        glVertex3f(pontosBaseInferior[(i+1)%N][0],pontosBaseInferior[(i+1)%N][1],0.0)
        glVertex3f(pontosBaseSuperior[(i+1)%N][0],pontosBaseSuperior[(i+1)%N][1],H)
        glVertex3f(pontosBaseSuperior[i][0],pontosBaseSuperior[i][1],H)
        glEnd()
    glPopMatrix()

def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Tronco da Esquerda
    glPushMatrix()
    glTranslatef(-2,0,0)
    glRotatef(a,0,1,0)
    prisma(2,1,3,6) 
    glPopMatrix()
    
    # Cilindro da Direita
    glPushMatrix()
    glTranslatef(2,0,0)
    glRotatef(a,0,1,0)
    prisma(1,1,3,140)
    glPopMatrix()
    a+=1
    glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(20,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PRISMA")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0,0,0,1)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-10)
glutTimerFunc(20,timer,1)
glutMainLoop()