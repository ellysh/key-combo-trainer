import pygame
import sys
import random
import math
import time

from dataclasses import dataclass
from pygame.locals import *


_COLOR_GREY = (128, 128, 128)
_COLOR_BLUE = (85, 206, 255)
_COLOR_GREEN = (0, 200, 0)

_WINDOW_WIDTH = 750
_WINDOW_HEIGHT = 750
_FPS = 75

FONT = None


KEY_INDEX = 0
_KEY_COMBO = "weq"


LAST_RESULT = 0


@dataclass
class Target:
    x: int
    y: int
    size: int
    time: int


def terminate():
    pygame.quit()
    sys.exit()


def make_window(title):
  global FONT

  pygame.init()

  FONT = pygame.font.SysFont(None, 30)

  window_surface = pygame.display.set_mode((_WINDOW_WIDTH, _WINDOW_HEIGHT))

  pygame.display.set_caption(title)

  clock = pygame.time.Clock()

  return window_surface, clock


def get_current_ms():
    return round(time.time() * 1000)


def draw_target(window_surface):
  target = Target(
    x = random.randint(20, _WINDOW_WIDTH - 20), \
    y = random.randint(50, _WINDOW_HEIGHT - 20), \
    size = random.randint(14, 20),
    time = get_current_ms())

  pygame.draw.circle(window_surface, _COLOR_BLUE, \
                     (target.x, target.y), target.size)

  return target


def is_mouse_on_target(target):
  mouse_x = pygame.mouse.get_pos()[0]
  mouse_y = pygame.mouse.get_pos()[1]

  sqx = (mouse_x - target.x)**2
  sqy = (mouse_y - target.y)**2

  return math.sqrt(sqx + sqy) < target.size


def draw_text(window_surface, text, x, y):
  global FONT

  text_object = FONT.render(text, 1, _COLOR_GREEN)
  text_rectangle = text_object.get_rect()
  text_rectangle.topleft = (x, y)
  window_surface.blit(text_object, text_rectangle)


def is_combo_pressed(key, target):
  global KEY_INDEX

  if key == ord(_KEY_COMBO[KEY_INDEX]) \
     and is_mouse_on_target(target):

    if KEY_INDEX+1 == len(_KEY_COMBO):
      KEY_INDEX = 0
      return True

    elif KEY_INDEX+1 < len(_KEY_COMBO):
      KEY_INDEX += 1
      return False

  else:
    KEY_INDEX = 0
    return False


def update_target(window_surface):
  window_surface.fill(_COLOR_GREY)
  draw_text(window_surface, _KEY_COMBO, 20, 20)
  draw_text(window_surface, "{} ms".format(str(LAST_RESULT)), 20, 50)

  return draw_target(window_surface)


def update_time_result(target):
  global LAST_RESULT

  LAST_RESULT = get_current_ms() - target.time


def main_loop(window_surface, clock):
  target = update_target(window_surface)

  while True:

    for event in pygame.event.get():
      if event.type == QUIT:
        terminate()
      if event.type == KEYDOWN:
        if is_combo_pressed(event.key, target):
          update_time_result(target)
          target = update_target(window_surface)

    pygame.display.update()
    clock.tick(_FPS)
