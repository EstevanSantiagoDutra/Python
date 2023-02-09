import pygame
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('arquivo.mp3')
#nome do arquivo que será executado ex > "arquivo.mp3"
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

pygame.quit()