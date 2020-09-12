import pygame # import de la librairire
from Jeu import Jeu
pygame.init() # initialisation de  pygame
# Creacton de la classe Camion


pygame.display.set_caption("RoadBreaker")   #Ouverture de la fenêtre
screen = pygame.display.set_mode((1280,720)) #Ouverture de a surface

background = pygame.image.load('Assets/Images/Fond_Jour.png') #Appel de l'image de fond, stockage de l'image dans background

jeu = Jeu()

isRunning = True #Initalisation de la condition de boucle principale

while isRunning :    #boucle principale
   
    screen.blit(background, (0, 0)) #Ajout de l'image de fond sur la surface. 

    screen.blit(jeu.Joueur.image,jeu.Joueur.rect)

    if jeu.isPressed.get(pygame.K_RIGHT):       
        print("go for it")
        jeu.Joueur.RouleDroite()
    elif jeu.isPressed.get(pygame.K_LEFT):
        print("boi")
        jeu.Joueur.RouleGauche()
    

    pygame.display.flip() #Actualisation de l'affichage

    for event in pygame.event.get(): #On attend un evenement
    
        if event.type == pygame.QUIT:  #Si l'evennement est un arrêt de la fenêtre :
            isRunning == False #On stope la boucle
            pygame.quit()  #on désactive pygame
            print("Fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            jeu.isPressed[event.key] = True
        elif event.type == pygame.KEYUP:
            jeu.isPressed[event.key] = False
