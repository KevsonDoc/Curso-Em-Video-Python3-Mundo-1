# Faça um programa em python que abra e reproduza o áudio de arquivo MP3.
import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Cut_no_idea_dom_toliver.mp3')
pygame.mixer.music.play()
