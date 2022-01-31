#!/usr/bin/env python3

from view import make_window
from view import main_loop

_VERSION = "0.1.0"

def main():
  window_surface, clock = make_window("League of Legends Combos Trainer " + _VERSION)

  main_loop(window_surface, clock)

if __name__ == '__main__':
    main()

