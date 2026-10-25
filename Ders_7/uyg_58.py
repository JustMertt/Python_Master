import pygame

pygame.init()

sound_file= 'merhaba.mp3'

sound=pygame.mixer.Sound(sound_file)
sound.play()
pygame.time.wait(3000)