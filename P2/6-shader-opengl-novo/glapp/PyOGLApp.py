import os
import pygame
from pygame.locals import *

class PyOGLApp():
    def __init__(self, screen_posX, screen_posY, screen_width, screen_height):
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screen_posX, screen_posY)
        self.screen_width = screen_width
        self.screen_height = screen_height
        pygame.init()
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 32)
        self.screen = pygame.display.set_mode((screen_width, screen_height),32, pygame.OPENGL | pygame.DOUBLEBUF)
        pygame.display.set_caption('Lava é legal')
        self.program_id = None
        self.clock = pygame.time.Clock()

    def mainloop(self):
        done = False
        self.initialize()
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            self.display()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()