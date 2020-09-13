import pygame

class Route(pygame.sprite.Sprite):

    def __init__(self,Jeu):
        super().__init__()
        self.Vitesse = 10
        self.Jeu = Jeu
        self.image = pygame.image.load('Assets/Sprites/Route/Route0.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1280
        self.rect.y = 387
    
    def defile(self):
        self.rect.x -= self.Vitesse
        
        if self.rect.x < -200:
            self.Jeu.TouteRoute.remove(self)