import pygame
pygame.init()


pygame.display.set_caption("RoadBreaker")
screen = pygame.display.set_mode((1080,720))

background = pygame.image.load('Assets/Images/Fond_Jour.png')

isRunning = True

while isRunning :
   
    screen.blit(background, (0, 0))

    pygame.display.flip()

    
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            isRunning == False
            pygame.quit()
            print("Fermeture du jeu")
    
