import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Heroe(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.imagenes = [util.cargar_imagen('dino1.png'),
                                        util.cargar_imagen('dino2.png'),
                                        util.cargar_imagen('dino3.png'),
                                        util.cargar_imagen('dino4.png')]
        self.cont = 0
        self.image = self.imagenes[self.cont]
        self.rect = self.image.get_rect()
        self.rect.move_ip(10, 200)
        self.vel = [2,3]
        self.estado = 1
		
        
    def update(self,size):
        if self.estado == 1:
            self.rect.y = size[1]-128
            teclas = pygame.key.get_pressed()
            if teclas[K_RIGHT]:
                self.vel[0] +=1
            if teclas[K_LEFT] and self.vel[0] >1:
                self.vel[0] -=1
            self.rect.x = (self.rect.x + self.vel[0]) % size[0]
            self.cont = (self.cont + 1) % 4
            self.image = self.imagenes[self.cont]
        else:
            self.image = util.cargar_imagen('dino8.png')
        self.image = pygame.transform.scale(self.image,(128,128))
        self.rect.size = (128,128)
        self.rect.y = size[1] - 128
            
