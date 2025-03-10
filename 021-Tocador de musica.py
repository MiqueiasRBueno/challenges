# Faça um programa que reproduza o audio de um arquivo mp3

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()