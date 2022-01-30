import pygame
import sys
import random
import math
from pygame.locals import *

_COLOR_GREY = (128, 128, 128)
_COLOR_BLUE = (85, 206, 255)
_COLOR_GREEN = (0, 200, 0)

_WINDOW_WIDTH = 750
_WINDOW_HEIGHT = 750
_FPS = 75

_KEY_COMBO = "weq"

FONT = None

def terminate():
    pygame.quit()
    sys.exit()


def make_window(title):
  global FONT

  pygame.init()

  FONT = pygame.font.SysFont(None, 24)

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

  return target_x, target_y, target_size


def is_mouse_on_target(target_x, target_y, target_size):
  mouse_x = pygame.mouse.get_pos()[0]
  mouse_y = pygame.mouse.get_pos()[1]

  sqx = (mouse_x - target_x)**2
  sqy = (mouse_y - target_y)**2

  return math.sqrt(sqx + sqy) < target_size


def draw_text(window_surface, text, x, y):
  global FONT

  text_object = FONT.render(text, 1, _COLOR_GREEN)
  text_rectangle = text_object.get_rect()
  text_rectangle.topleft = (x, y)
  window_surface.blit(text_object, text_rectangle)

KEY_INDEX = 0

def is_combo_pressed(key):
  global KEY_INDEX

  if key == ord(_KEY_COMBO[KEY_INDEX]):

    if KEY_INDEX+1 == len(_KEY_COMBO):
      KEY_INDEX = 0
      return True

    elif KEY_INDEX+1 < len(_KEY_COMBO):
      KEY_INDEX += 1
      return False

  else:
    KEY_INDEX = 0
    return False


def main_loop(window_surface, clock):
  draw_text(window_surface, _KEY_COMBO, 20, 20)
  target_x, target_y, target_size = draw_target(window_surface)

  while True:

    for event in pygame.event.get():
      if event.type == QUIT:
        terminate()
      if event.type == KEYDOWN:
        if is_combo_pressed(event.key) \
           and is_mouse_on_target(target_x, target_y, target_size):

          window_surface.fill(_COLOR_GREY)
          draw_text(window_surface, "weq", 20, 20)
          target_x, target_y, target_size = draw_target(window_surface)

    pygame.display.update()
    clock.tick(_FPS)
