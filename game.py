
# This file is for making the game board...

# Importing class called Constants
from constants import Constants

# Importing class called Snake
from snake import Snake

# Importing class called Food
from food import Food

# Now, this is the interesting part of this file
# Pygame is used for graphics
import pygame

# now, Pygame is just a Framework that we are using to draw graphics to the screen. That's a complicated subject we are gonna let the pygame to handle that thing....

import sys
# And I currently used exit fuction from sys


# Creating the class for Game
class Game():

  # Constructor
  def __init__(self):

    # starting a game
    pygame.init()

    # Window to display
    self.screen = pygame.display.set_mode(
        (Constants.Window_width, Constants.Window_height))

    # Clock
    self.clock = pygame.time.Clock()

    # Caption setting
    self.BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

    # Caption sentence
    pygame.display.set_caption('Wormy')
    self.food = Food()
    self.snake = Snake()

  # Grid function used for drawing vertical and horizontal lines
  def drawGrid(self):
    for x in range(0, Constants.Window_width, Constants.Cell_size):  # draw vertical lines
      pygame.draw.line(self.screen, Constants.DARKGRAY,
                       (x, 0), (x, Constants.Window_height))

    for y in range(0, Constants.Window_height, Constants.Cell_size):  # draw horizontal lines
      pygame.draw.line(self.screen, Constants.DARKGRAY,
                       (0, y), (Constants.Window_width, y))

  # Worm example
  def drawWorm(self):
      for coord in self.snake.wormCoords:

          # This is the snake in the game with colors and etc
          x = coord['x'] * Constants.Cell_size
          y = coord['y'] * Constants.Cell_size
          wormSegmentRect = pygame.Rect(
              x, y, Constants.Cell_size, Constants.Cell_size)
          pygame.draw.rect(self.screen, Constants.DARKGREEN, wormSegmentRect)
          wormInnerSegmentRect = pygame.Rect(
              x + 4, y + 4, Constants.Cell_size - 8, Constants.Cell_size - 8)
          pygame.draw.rect(self.screen, Constants.GREEN, wormInnerSegmentRect)

  # Apple's size with colors
  def drawApple(self):
    x = self.food.x * Constants.Cell_size
    y = self.food.y * Constants.Cell_size
    appleRect = pygame.Rect(
        x, y, Constants.Cell_size, Constants.Cell_size)
    pygame.draw.rect(self.screen, Constants.RED, appleRect)

  # To keep the score position
  def drawScore(self, score):
    scoreSurf = self.BASICFONT.render(
        'Score: %s' % (score), True, Constants.WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (Constants.Window_width - 120, 10)
    self.screen.blit(scoreSurf, scoreRect)

  # Filling the board with Snake, grid, Food, Score
  def draw(self):
    self.screen.fill(Constants.BG_COLOR)
    # in here we'll draw our snake, grid, food, score
    self.drawGrid()
    self.drawWorm()
    self.drawApple()
    self.drawScore(len(self.snake.wormCoords) - 3)
    pygame.display.update()
    self.clock.tick(Constants.FPS)

  # Handling with keys' presses
  def checkForKeyPress(self):
      if len(pygame.event.get(pygame.QUIT)) > 0:
          pygame.quit()

      keyUpEvents = pygame.event.get(pygame.KEYUP)

      if len(keyUpEvents) == 0:
          return None

      if keyUpEvents[0].key == pygame.K_ESCAPE:
          pygame.quit()
          quit()

      return keyUpEvents[0].key

  # Changing the snake direction with key movements
  # This functon is for handling key events

  def handleKeyEvents(self, event):
    if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.snake.direction != self.snake.RIGHT:
        self.snake.direction = self.snake.LEFT
    elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.snake.direction != self.snake.LEFT:
        self.snake.direction = self.snake.RIGHT
    elif (event.key == pygame.K_UP or event.key == pygame.K_w) and self.snake.direction != self.snake.DOWN:
        self.snake.direction = self.snake.UP
    elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.snake.direction != self.snake.UP:
        self.snake.direction = self.snake.DOWN
    elif event.key == pygame.K_ESCAPE:
        pygame.quit()

  # Restoring or reseting the game
  def resetGame(self):
      del self.snake
      del self.food
      self.snake = Snake()
      self.food = Food()

      return True

  # Showing the text with the caption to press any key to continue

  def drawPressKeyMsg(self):
      pressKeySurf = self.BASICFONT.render(
          'Press a key to play.', True, Constants.DARKGRAY)
      pressKeyRect = pressKeySurf.get_rect()
      pressKeyRect.topleft = (Constants.Window_width - 200,
                              Constants.Window_height - 30)
      self.screen.blit(pressKeySurf, pressKeyRect)

  # Checking the game is over or not.
  def isGameOver(self):
      if (self.snake.wormCoords[self.snake.HEAD]['x'] == -1 or
          self.snake.wormCoords[self.snake.HEAD]['x'] == Constants.Cell_width or
          self.snake.wormCoords[self.snake.HEAD]['y'] == -1 or
              self.snake.wormCoords[self.snake.HEAD]['y'] == Constants.Cell_height):
          return self.resetGame()

      for wormBody in self.snake.wormCoords[1:]:
          if wormBody['x'] == self.snake.wormCoords[self.snake.HEAD]['x'] and wormBody['y'] == self.snake.wormCoords[self.snake.HEAD]['y']:
              return self.resetGame()

  # Function for showing Game Over if the Game is over somehow
  def displayGameOver(self):
      gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
      gameSurf = gameOverFont.render('Game', True, Constants.WHITE)
      overSurf = gameOverFont.render('Over', True, Constants.WHITE)
      gameRect = gameSurf.get_rect()
      overRect = overSurf.get_rect()
      gameRect.midtop = (Constants.Window_width / 2, 10)
      overRect.midtop = (Constants.Window_width / 2, gameRect.height + 10 + 25)
      self.screen.blit(gameSurf, gameRect)
      self.screen.blit(overSurf, overRect)

      self.drawPressKeyMsg()
      pygame.display.update()
      pygame.time.wait(500)

      self.checkForKeyPress()  # clear out any key presses in the event queue
      while True:
          if self.checkForKeyPress():
              pygame.event.get()  # clear event queue
              return

  # Customizing the caption
  def showStartScreen(self):
      titleFont = pygame.font.Font('freesansbold.ttf', 100)
      titleSurf1 = titleFont.render(
          'Wormy!', True, Constants.WHITE, Constants.DARKGREEN)
      titleSurf2 = titleFont.render('Wormy!', True, Constants.GREEN)
      degrees1 = 0
      degrees2 = 0

      while True:
          for event in pygame.event.get():
              if event.type == pygame.KEYDOWN:
                  return
          self.screen.fill(Constants.BG_COLOR)
          rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
          rotatedRect1 = rotatedSurf1.get_rect()
          rotatedRect1.center = (Constants.Window_width / 2,
                                 Constants.Window_height / 2)
          self.screen.blit(rotatedSurf1, rotatedRect1)

          rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
          rotatedRect2 = rotatedSurf2.get_rect()
          rotatedRect2.center = (Constants.Window_width / 2,
                                 Constants.Window_height / 2)
          self.screen.blit(rotatedSurf2, rotatedRect2)

          self.drawPressKeyMsg()

          pygame.display.update()
          self.clock.tick(Constants.Menu_FPS)
          degrees1 += 1  # rotate by 3 degrees each frame
          degrees2 += 2  # rotate by 7 degrees each frame

  # Starting the Game

  def run(self):
    self.showStartScreen()

    while True:
      self.gameLoop()
      self.displayGameOver()

  # If any keypress leads to restart after Game over

  def gameLoop(self):
      while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
          elif event.type == pygame.KEYDOWN:
              self.handleKeyEvents(event)

        self.snake.update(self.food)
        self.draw()
        if self.isGameOver():
          break


#
# ---------------------------------
# This is the end of game.py