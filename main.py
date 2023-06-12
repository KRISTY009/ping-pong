from pygame import *
font.init()
clock = time.Clock()

window = display.set_mode((700, 500))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('image.jpg'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, coor_x, coor_y, size_x, size_y):
        super().__init__()
        self.width = size_x
        self.length = size_y
        self.image = transform.scale(image.load(player_image), (self.width, self.length))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = coor_x
        self.rect.y = coor_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_speed, coor_x, coor_y, size_x, size_y):
        super().__init__(player_image, player_speed, coor_x, coor_y, size_x, size_y)
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y != 0:
            self.rect.y -= 5
        if keys_pressed[K_DOWN] and self.rect.y != 410:
            self.rect.y += 5
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y != 0:
            self.rect.y -= 5
        if keys_pressed[K_s] and self.rect.y != 410:
            self.rect.y += 5

# class Ball(GameSprite):
#     def __init__(self, player_image, player_speed, coor_x, coor_y, size_x, size_y):
#         super().__init__(player_image, player_speed, coor_x, coor_y, size_x, size_y)
#     def update(self):
#         if self.rect.x >= 600 or sprite.collide_rect(self, player_2) and self.rect.x > 0:
#             self.size = 'left'
#         if self.rect.x <= 0 or sprite.collide_rect(self, player_1) and self.rect.x < 600:
#             self.size = 'right'
#         if self.rect.y <= 0:

#         if self.rect.y >= 600:
#             self.rect.y -= self.speed

#             self.rect.y += self.speed
#             self.rect.x -= self.speed
#             self.rect.x += self.speed
player_1 = Player('player_1.png', 3, 10, 0, 90, 110)
player_2 = Player('player_2.png', 3, 600, 0, 90, 110)
# ball = Ball('ball.png', 3, 250, 250, 50, 50)


finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        player_1.reset()
        player_1.update_l()
        player_2.reset()
        player_2.update_r()
        # ball.reset()
        # ball.update()
        # if ball.rect.x >= 600 or sprite.collide_rect(ball, player_2):
        #     ball.rect.x -= ball.speed
        # if ball.rect.x <= 0 or sprite.collide_rect(ball, player_1):
        #     ball.rect.x += ball.speed
        
    display.update()
    clock.tick(60)
