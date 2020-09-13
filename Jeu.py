import pygame

from Vehicules import Camion
from Decor import Route

class Jeu:
    
    def __init__(self):
        
        self.Joueur = Camion()
        self.TouteRoute = pygame.sprite.Group()
        
        self.isPressed = {}

    def LaunchRoute(self):
        
        self.TouteRoute.add(Route(self))