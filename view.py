import pygame, sys
from pygame.locals import *

_WINDOW_WIDTH = 750
_WINDOW_HEIGHT = 750
_FPS = 75

def terminate():
    pygame.quit()
    sys.exit()

def make_window(title):
  pygame.init()

  window_surface = pygame.display.set_mode((_WINDOW_WIDTH, _WINDOW_HEIGHT))
  pygame.display.set_caption(title)

  clock = pygame.time.Clock()

  return window_surface, clock

def main_loop(window_surface, clock):
  while True:

    for event in pygame.event.get():
      if event.type == QUIT:
        terminate()
      if event.type == KEYDOWN:
        terminate()

    pygame.display.update()
    clock.tick(_FPS)
