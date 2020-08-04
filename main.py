import pygame
import os

img_path = os.path.join('paddle.png')

class paddle(object):
  def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      paddle.image = pygame.image.load("paddle.png")

      self.x = 60
      self.y = 60
      self.hitbox = (self.x,self.y,34, 34)



  def draw(self, surface):
    surface.blit(self.image,(self.x,self.y))
    self.image = paddle.image
    #self.paddle = pygame.transform.scale(self.image(32,60))
 
    


  def movement(self):
    key = pygame.key.get_pressed()

    if key[pygame.K_DOWN]:
      self.y -= 1
    if key[pygame.K_UP]:
      self.y += 2

pygame.init()
screen_width =600
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

sprite= paddle()


running= True


while running:
  for event in pygame.event.get():
    if event.type== pygame.QUIT:
      pygame.quit()
      running= False

  screen.fill((255,255,255))

  sprite.movement()

  sprite.draw(screen)

  pygame.display.update()