import pygame # import de la librairire
from Jeu import Jeu
from Jeu import Route
pygame.init() # initialisation de  pygame
# Creacton de la classe Camion


pygame.display.set_caption("RoadBreaker")   #Ouverture de la fenêtre
screen = pygame.display.set_mode((1280,720)) #Ouverture de a surface

background = pygame.image.load('Assets/Images/Fond_Jour.png') #Appel de l'image de fond, stockage de l'image dans background

jeu = Jeu()

isRunning = True #Initalisation de la condition de boucle principale

compteurR=0


while isRunning :    #boucle principale
   
    screen.blit(background, (0, 0)) #Ajout de l'image de fond sur la surface. 
    
    if compteurR > 318:
        jeu.LaunchRoute()
        compteurR = 0    
    compteurR += 5
    
    print(jeu.Joueur.Santee)
    
    jeu.TouteRoute.draw(screen)
    
    for Route in jeu.TouteRoute:
        Route.defile()

    screen.blit(jeu.Joueur.image,jeu.Joueur.rect)

    

    if jeu.isPressed.get(pygame.K_RIGHT) and (jeu.Joueur.rect.x + jeu.Joueur.rect.width <= screen.get_width()):       
        print("Vite",jeu.Joueur.rect.x)
        jeu.Joueur.Accelere()
    elif jeu.isPressed.get(pygame.K_LEFT) and jeu.Joueur.rect.x > 5 :
        print("Stop",jeu.Joueur.rect.x)
        jeu.Joueur.Ralentit()
    
    if jeu.isPressed.get(pygame.K_UP) and (jeu.Joueur.rect.y + jeu.Joueur.rect.height) > 550:        
        print("a Gauche",jeu.Joueur.rect.y + jeu.Joueur.rect.height)
        jeu.Joueur.aGauche()
    elif jeu.isPressed.get(pygame.K_DOWN) and (jeu.Joueur.rect.y + jeu.Joueur.rect.height) < 630:
        print("a Droite",jeu.Joueur.rect.y + jeu.Joueur.rect.height)
        jeu.Joueur.aDroite()
    

    pygame.display.flip() #Actualisation de l'affichage

    for event in pygame.event.get(): #On attend un evenement
    
        if event.type == pygame.QUIT:  #Si l'evennement est un arrêt de la fenêtre :
            isRunning == False #On stope la boucle
            pygame.quit()  #on désactive pygame
            print("Fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            jeu.isPressed[event.key] = True
            if event.key == pygame.K_SPACE:
                jeu.LaunchRoute()
        elif event.type == pygame.KEYUP:
            jeu.isPressed[event.key] = False
