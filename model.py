KEY_INDEX = 0
_KEY_COMBO = "weq"

def is_combo_pressed(key, target, is_mouse_on_target):
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
