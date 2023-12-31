# importing module called random
import random

# Importing constants
from constants import Constants

# Creating a class called Snake:-


class Snake():

  # Constants
  UP = 'up'
  DOWN = 'down'
  LEFT = 'left'
  RIGHT = 'right'
  HEAD = 0

  # Starting co-ordinates
  def __init__(self):
    self.x = random.randint(5, Constants.Cell_width - 6)
    self.y = random.randint(5, Constants.Cell_height - 6)
    self.direction = self.RIGHT

    # This is the SNAKE of the game
    self.wormCoords = [{'x': self.x,     'y': self.y},
                       {'x': self.x - 1,  'y': self.y},
                       {'x': self.x - 2, 'y': self.y}]

  def update(self, apple):
      # check if worm has eaten an apply
      if self.wormCoords[self.HEAD]['x'] == apple.x and self.wormCoords[self.HEAD]['y'] == apple.y:
          apple.setNewLocation()
      else:
          del self.wormCoords[-1]  # remove worm's tail segment

      # move the worm by adding a segment in the direction it is moving
      if self.direction == self.UP:
          newHead = {'x': self.wormCoords[self.HEAD]['x'],
                     'y': self.wormCoords[self.HEAD]['y'] - 1}

      elif self.direction == self.DOWN:
          newHead = {'x': self.wormCoords[self.HEAD]['x'],
                     'y': self.wormCoords[self.HEAD]['y'] + 1}

      elif self.direction == self.LEFT:
          newHead = {'x': self.wormCoords[self.HEAD]
                     ['x'] - 1, 'y': self.wormCoords[self.HEAD]['y']}

      elif self.direction == self.RIGHT:
          newHead = {'x': self.wormCoords[self.HEAD]
                     ['x'] + 1, 'y': self.wormCoords[self.HEAD]['y']}

      self.wormCoords.insert(0, newHead)


# ---------------------------------------------------------------------------------------
# This is the end of Snake.py
