import pygame
import controller

def main():
    pygame.init()
    game = controller.Controller()
    game.game()
main()