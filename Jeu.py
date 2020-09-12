import pygame

from Vehicules import Camion

class Jeu:
    
    def __init__(self):
        
        self.Joueur = Camion()
        self.isPressed = {}
