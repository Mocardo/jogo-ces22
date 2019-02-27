import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #classe que exprime alien

    def __init__(self, ai_settings, screen):
        #inicializar alien e configurar sua posicao inicial
        super(Alien, self).__init__()
