
# Creating a Food(Apple) class:
# Using class will take all the different data types (for short)

# Importing a module called Random
import random

# Importing our Dimensions from Constants.py
from constants import Constants


class Food():

  # Constructor
  def __init__(self):

    # Setting with positions
    self.setNewLocation()

  # Function for setting the food in the random place
  def setNewLocation(self):

      # This is the APPLE in the game
      self.x = random.randint(0, Constants.Cell_width - 1)
      self.y = random.randint(0, Constants.Cell_height - 1)


# ---------------------------------------------------------------------------------------
# This is the end of Food.py
