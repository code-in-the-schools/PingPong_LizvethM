import pygame
import os

img_path = os.path.join('paddle.png')

class paddle(object):
  def __int__(self):
    paddle.image = pygame.image.load("paddle.png")
    self.image = paddle.image
#    self.image = pygame.transform.scale(self.image(50,50))

    self.x = 50
    self.y = 50
    self.hitbox = (self.x,self.y,55, 55)

  def draw(self, surface):
    surface.blit(self.image,(self.x,self.y))

  def movement(self):
    key = pygame.key.get_pressed()

    if key[pygame.k_DOWN]:
      self.y -= 1
    if key[pygame.k_UP]:
      self.y += 2



running= True
paddle= paddle()

while running:

  color = (555,555,555)
  pygame.init()
  screen_width =600
  screen_height = 600
  screen = pygame.display.set_mode((screen_width,screen_height))

  pygame.display.update()