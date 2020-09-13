import pygame

class Camion(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.Santee = 100
        self.SanteeMax = 100
        self.Velocite = 5
        self.VitesseBraq = 1
        self.image = pygame.image.load('Assets/Sprites/CamionClean.png')
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 420

    def Accelere(self):
        self.rect.x += self.Velocite

    def Ralentit(self):
        self.rect.x -= self.Velocite

    def aGauche(self):
        self.rect.y -= self.VitesseBraq

    def aDroite(self):
        self.rect.y += self.VitesseBraq

