import pygame
import sys
import random
from pygame.locals import *

_COLOR_GREY = (128, 128, 128)
_COLOR_BLUE = (85, 206, 255)

_WINDOW_WIDTH = 750
_WINDOW_HEIGHT = 750
_FPS = 75


def terminate():
    pygame.quit()
    sys.exit()


def make_window(title):
  pygame.init()

  window_surface = pygame.display.set_mode((_WINDOW_WIDTH, _WINDOW_HEIGHT))
  window_surface.fill(_COLOR_GREY)

  pygame.display.set_caption(title)

  clock = pygame.time.Clock()

  return window_surface, clock


def draw_target(window_surface):
  target_x = random.randint(20, _WINDOW_WIDTH - 20)
  target_y = random.randint(20, _WINDOW_HEIGHT - 20)
  target_size = random.randint(14, 20)
  pygame.draw.circle(window_surface, _COLOR_BLUE, \
                     (target_x, target_y), target_size)

def main_loop(window_surface, clock):
  while True:

    for event in pygame.event.get():
      if event.type == QUIT:
        terminate()
      if event.type == KEYDOWN:
        terminate()

    draw_target(window_surface)

    pygame.display.update()
    clock.tick(_FPS)
