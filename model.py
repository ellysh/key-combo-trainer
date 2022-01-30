import random


_KEY_SYMBOLS = "123aqwerdf"
_KEY_LENGTH_MIN = 2
_KEY_LENGTH_MAX = 4


KEY_INDEX = 0
KEY_COMBO = ""
#_KEY_COMBO = "weq"


def generate_key_combo(symbols, length_min, length_max):
  return ''.join(random.sample(symbols, \
                 k = random.randrange(length_min, length_max)))


def update_key_combo():
  global KEY_COMBO

  KEY_COMBO = generate_key_combo(_KEY_SYMBOLS, _KEY_LENGTH_MIN, _KEY_LENGTH_MAX)


def is_combo_pressed(key, target, is_mouse_on_target):
  global KEY_INDEX

  if key == ord(KEY_COMBO[KEY_INDEX]) \
     and is_mouse_on_target(target):

    if KEY_INDEX+1 == len(KEY_COMBO):
      KEY_INDEX = 0
      return True

    elif KEY_INDEX+1 < len(KEY_COMBO):
      KEY_INDEX += 1
      return False

  else:
    KEY_INDEX = 0
    return False
