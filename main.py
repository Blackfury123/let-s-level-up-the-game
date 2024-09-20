import pygame
import random

screen_width=700
screen_height=700
movement_speed=5
font_size=70

pygame.init()

backgroud_image = pygame.transform.scale(pygame.image.load("./bg.jpg"),(screen_width, screen_height))

font=pygame.font.SysFont("Times New Roman",font_size)
class Sprite(pygame.sprite.Sprite):

  def __init__(self, color, height, width):
    super().__init__()
    self.image = pygame.Surface([width, height])
    self.image.fill(pygame.Color('dodgerblue'))  # Background color of sprite
    pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
    self.rect = self.image.get_rect()

  def move(self,x_change,y_change):
    self.rect.x = max(
        min(self.rect.x + x_change, screen_width - self.rect.width), 0)
    self.rect.y = max(
      min(self.rect.y+y_change,screen_height - self.rect.height),0)
# Setup
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group()

# Create sprites
sprite1 = Sprite(pygame.Color('black'), 20, 30)
sprite1.rect.x = random.randint(0, screen_width - sprite1.rect.width)
sprite1.rect.y =random.randint(0, screen_height - sprite1.rect.height)
all_sprites.add(sprite1)

sprite2=Sprite(pygame.color('red'),20,30)
sprite2.rect.x = random.randint(0,screen_width - sprite2.rect.width)
sprite2.rect.y = random.randint(0,screen_height - sprite2.rect.height)
all_sprites.add(sprite2)

running = True
won = False
clock=pygame.time.Clock()

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.type== pygame.K_x):
        running=False
  if not won:
    keys = pygame.key.get_pressed()
    x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * movement_speed
    y_change = (keys[pygame.K_DOWN] - keys[pygame.k_up]) * movement_speed
    sprite1.move(x_change,y_change)

    if sprite1.rect.colliderect(sprite2.rect):
      all_sprites.remove(sprite2)
      won = True

  screen.blit(backgroud_image,(0,0))
  all_sprites.draw(screen)

  if won:
    win_text= font.render("TOO EASYYYY",True,pygame.Color('black'))
    screen.blit(win_text,((350,350)))

  pygame.display.flip()
  clock.tick(90)

pygame.quit()