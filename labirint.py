import pygame

window = pygame.display.set_mode((1100,700))
pygame.display.set_caption("Лабірит")
bg = pygame.transform.scale(pygame.image.load("fon1.jpg"),(1100,700))
sprite1 = pygame.transform.scale(pygame.image.load("s1.png"),(100,100))
sprite2 = pygame.transform.scale(pygame.image.load("s2.png"),(100,100))
reward = pygame.transform.scale(pygame.image.load("nuts1.png"),(100,100))

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()#підключаємо всі можливості суперкласу
        self.image = player_image
        self.player_speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y#координати рамки
    def reset (self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):#керування
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x>10:
            self.rect.x = self.rect.x - self.player_speed
        if keys[pygame.K_RIGHT] and self.rect.x<1000:
            self.rect.x = self.rect.x + self.player_speed
        if keys[pygame.K_DOWN] and self.rect.y<600:
            self.rect.y = self.rect.y + self.player_speed
        if keys[pygame.K_UP] and self.rect.y>10:
            self.rect.y = self.rect.y - self.player_speed

class Enemy (GameSprite):
    direction = "left"#змінна для напрямку руху
    def update(self):
        if self.rect.x<600:
            self.direction = "right"
        if self.rect.x>1000:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x = self.rect.x - self.player_speed
        else:
            self.rect.x = self.rect.x +self.player_speed

class Enemy2 (GameSprite):
    direction = "left"#змінна для напрямку руху
    def update(self):
        if self.rect.x<50:
            self.direction = "right"
        if self.rect.x>450:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x = self.rect.x - self.player_speed
        else:
            self.rect.x = self.rect.x +self.player_speed

class Wall(pygame.sprite.Sprite):
    def __init__(self,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.color = (145, 5, 186)
        self.wall_x = wall_x
        self.wall_y = wall_y
        self.wall_width = wall_width
        self.wall_height = wall_height
        self.image = pygame.Surface((self.wall_width, self.wall_height))
        self.image.fill((self.color))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

        

game = True
finish = False

hero = Player(sprite1, 400,50,10)
vorog = Enemy(sprite2, 650,200,5)
vorog2 = Enemy2(sprite2, 50, 222, 5)
reward = GameSprite(reward, 800,50,0)
w1 = Wall(0,0,10,1000)
w2 = Wall(550,0,10,395)
w3 = Wall(150,200,400,10)
w4 = Wall(250,385,500,10)
w5 = Wall(350,525,10,300)
w6 = Wall(525,395,10,180)
w7 = Wall(740,525,10,300)
w8 = Wall(0,0,1100,10)
w9 = Wall(0,690,1100,10)
w10 = Wall(1090,0,10,700)

pygame.font.init()#підключаємо font з бібліотеки pygame
font1 = pygame.font.SysFont("Times New Roman", 80)
win = font1.render("YOU WIN!", True,(0,0,0))
lose = font1.render("YOU LOSE!", True,(0,0,0))

clock = pygame.time.Clock()

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game= False

    if finish!=True:
        window.blit(bg,(0,0))#малюємо на екрані фон
        hero.update()
        hero.reset()
        vorog.update()
        vorog.reset()
        vorog2.update()
        vorog2.reset()
        reward.reset()
        w1.reset()
        w2.reset()
        w3.reset()
        w4.reset()
        w5.reset()
        w6.reset()
        w7.reset()
        w8.reset()
        w9.reset()
        w10.reset()
        if pygame.sprite.collide_rect(hero,vorog) or pygame.sprite.collide_rect(hero,vorog2):
            finish = True
            window.blit(lose,(550,350))
        if pygame.sprite.collide_rect(hero,w1) or pygame.sprite.collide_rect(hero,w2) or pygame.sprite.collide_rect(hero,w3) or pygame.sprite.collide_rect(hero,w4) or pygame.sprite.collide_rect(hero,w5) or pygame.sprite.collide_rect(hero,w6) or pygame.sprite.collide_rect(hero,w7):
            hero.rect.x = 100
            hero.rect.y = 50
        if pygame.sprite.collide_rect(hero,reward):
            finish = True
            window.blit(win,(550,350))



    clock.tick(60)
    pygame.display.update()
