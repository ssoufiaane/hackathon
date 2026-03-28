import pygame
pygame.init()

#creation de la fenetre du jeu 
pygame.display.set_mode((1200, 700))
pygame.display.set_caption("breaking-good")

# la boucle du jeu
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()