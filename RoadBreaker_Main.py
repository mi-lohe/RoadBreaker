import pygame

pygame.init()

pygame.display.set_caption("RoadBreaker")
pygame.display.set_mode((1920,1080))


isRunning = True

while isRunning :

    #
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            isRunning == False
            pygame.quit()
            print("Fermeture")
    
