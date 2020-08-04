import pygame
import os

img_path = os.path.join('paddle.png')

class paddle(object):
  def __init__(self):
      pygame.sprite.Sprite.__init__(self)

      paddle.image = pygame.image.load("paddle.png")
      self.image = paddle.image
      self.image = pygame.transform.scale(self.image,(25,150))

      self.x = 60
      self.y = 60
      self.hitbox = (self.x,self.y,34, 34)




  def draw(self, surface):
    surface.blit(self.image,(self.x,self.y))
    #self.image = paddle.image

 

  def movement(self):
    keys = pygame.key.get_pressed()

    if event.type == pygame.KEYDOWN:
      self.y -=1

    if event.type == pygame.KEYUP:
      self.y +=1

class wallObj(object):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    wallObj.image = pygame.image.load("wall.png")

    self.x = 50
    self.y  =50

  def draw(self, surface, width, height, x,y):
    surface.blit(self.image, (self.x, self.y))
    self.image = pygame.transform.scale(self.image,600,600)
    self.x = x
    self.y = y
    self.hitbox = (width/2,height/2, width+5, height,+5)





pygame.init()
screen_width =600
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

  sprite.movement()

  sprite.draw(screen)

  wall1.draw(screen)

  pygame.display.update()