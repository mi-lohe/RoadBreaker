import pygame

class Camion(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.Santee = 100
        self.SanteeMax = 100
        self.Velocite = 15
        self.image = pygame.image.load('Assets/Sprites/CamionClean.png')
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 420

    def RouleDroite(self):
        self.rect.x += self.Velocite

    def RouleGauche(self):
        self.rect.x -= self.Velocite

