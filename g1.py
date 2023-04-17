import pygame

pygame.init()
#window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#window = pygame.display.set_mode((640,480))

window = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    pygame.display.update()      

pygame.quit()