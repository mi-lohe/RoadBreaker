import pygame
import random

class Route(pygame.sprite.Sprite):

    def __init__(self,Jeu):
        super().__init__()
        self.Vitesse = 10
        self.Jeu = Jeu
        self.nImage = random.randint(0,3)
        
        if   self.nImage == 0:
            self.image = pygame.image.load('Assets/Sprites/Route/Route0.png')
        elif self.nImage == 1: 
            self.image = pygame.image.load('Assets/Sprites/Route/Route1.png')
        elif self.nImage == 2:
            self.image = pygame.image.load('Assets/Sprites/Route/Route2.png')
        elif self.nImage == 3:
            self.image = pygame.image.load('Assets/Sprites/Route/Route3.png')
        
        self.rect = self.image.get_rect()
        self.rect.x = 1280
        self.rect.y = 387
    
    def defile(self):
        self.rect.x -= self.Vitesse
        
        if self.rect.x < -self.rect.width:
            self.Jeu.TouteRoute.remove(self)

        