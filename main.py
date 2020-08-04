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





pygame.init()
screen_width =800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

sprite= paddle()
wall1= wallObj()
wall2= wallObj()

running= True


while running:
  for event in pygame.event.get():
    if event.type== pygame.QUIT:
      pygame.quit()
      running= False

  screen.fill((255,255,255))

  wall1.draw(screen,600,1,0,0)

  wall2.draw(screen,800,20,800,20)

  sprite.movement()

  sprite.draw(screen)

  pygame.display.update()