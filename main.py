import pygame
import os

img_path = os.path.join('paddle.png')

class paddle(object):
  def __init__(self):
      pygame.sprite.Sprite.__init__(self)

      paddle.image = pygame.image.load("paddle.png")
      self.image = paddle.image
      self.image = pygame.transform.scale(self.image,(25,150))

      self.x = 700
      self.y = 60
      self.hitbox = (self.x,self.y,34, 34)

  def draw(self, surface):
    surface.blit(self.image,(self.x,self.y))
    #self.image = paddle.image

  def movement(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN]:
      self.y +=1

    if keys[pygame.K_UP]:
      self.y -=1

class wallObj(object):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    wallObj.image = pygame.image.load("wall.png")
    self.image = wallObj.image
    self.image = pygame.transform.scale(self.image,(12,600))

    self.x = 50
    self.y  =50

  def draw(self, surface, width, height, x,y):
    surface.blit(self.image, (self.x, self.y))

    self.x = x
    self.y = y
    self.hitbox = (width/2,height/2, width+5, height,+5)

class ball(object):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    ball.image = pygame.image.load("ball.png")
    self.image = ball.image
    self.image = pygame.trasform.scale(self.image,(12,12))

    self.x = 20
    self.y = 30

  def draw(self, surface):
    surface.blit(self.image,(self.x, self.y,))

  def bounce(self,screen_wdth,screen_height, collider):
    self.x += self.x_velocity
    self.y += self.y_velocity

    if(self.y <-0):
      self.y_velocity = 2
    if(self.y >= screen_height-50):
      self.y_velocity = -2





pygame.init()
screen_width =800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

sprite= paddle()
wall1= wallObj()

running= True


while running:
  for event in pygame.event.get():
    if event.type== pygame.QUIT:
      pygame.quit()
      running= False

  screen.fill((255,255,255))

  wall1.draw(screen,600,1,790,0)

  sprite.movement()

  sprite.draw(screen)

  pygame.display.update()