import pygame
from src import controller

def main():
    pygame.init()
    game = controller.Controller()
    game.mainloop()
    
main()