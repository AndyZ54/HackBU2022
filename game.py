import pygame
import src.controller

def main():
    pygame.init()
    game = src.controller.Controller()
    game.game()
    
main()