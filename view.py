import pygame

def make_window(title):
  pygame.init()

  width = 1600
  height = 900
  display = pygame.display.set_mode((width, height))

  clock = pygame.time.Clock()  # To set the frame rate

  pygame.display.update()
  clock.tick()
