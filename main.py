from pygame import *
font.init()
clock = time.Clock()

amount_1_n = 0
amount_2_n = 0

window = display.set_mode((700, 500))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('image.jpg'), (700, 500))
font1 = font.Font(None, 70)
font2 = font.Font(None, 25)
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
        if keys_pressed[K_DOWN] and self.rect.y != 400:
            self.rect.y += 5
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y != 0:
            self.rect.y -= 5
        if keys_pressed[K_s] and self.rect.y != 400:
            self.rect.y += 5

class Ball(GameSprite):
    def __init__(self, player_image, player_speed, coor_x, coor_y, size_x, size_y):
        super().__init__(player_image, player_speed, coor_x, coor_y, size_x, size_y)
        self.size1 = 'down'
        self.size2 = 'right'
        self.amount1 = 0
        self.amount2 = 0
    def update(self):
        # global amount_1_n
        # global amount_2_n
        if sprite.collide_rect(self, player_2):
            self.size2 = 'left'
            self.amount2 += 1
            # amount_2_n += 1
        if sprite.collide_rect(self, player_1):
            self.size2 = 'right'
            self.amount1 += 1
            # amount_1_n += 1
        if self.rect.y <= 0:
            self.size1 = 'down'
        if self.rect.y >= 400:
            self.size1 = 'up'

        if self.size1 == 'down':
            self.rect.y += self.speed
            if self.size2 == 'right':
                self.rect.x += self.speed
            else:
                self.rect.x -= self.speed

        if self.size1 == 'up':
            self.rect.y -= self.speed
            if self.size2 == 'right':
                self.rect.x += self.speed
            else:
                self.rect.x -= self.speed

        if self.size2 == 'right':
            self.rect.x += self.speed
            if self.size1 == 'up':
                self.rect.y -= self.speed
            else:
                self.rect.y += self.speed

        if self.size2 == 'left':
            self.rect.x -= self.speed
            if self.size1 == 'up':
                self.rect.y -= self.speed
            else:
                self.rect.y += self.speed


player_1 = Player('player_1.png', 3, 10, 0, 90, 110)
player_2 = Player('player_2.png', 3, 600, 0, 90, 110)
ball = Ball('ball.png', 2, 200, 100, 50, 50)

amount_1 = font2.render('Счёт первого игрока:  ' + str(ball.amount1), True, (255,255,255))
amount_2 = font2.render('Счёт второго игрока:  ' + str(ball.amount2), True, (255,255,255))

win_1 = font1.render('Победил игрок 1', True, (255,255,255))
win_2 = font1.render('Победил игрок 2', True, (255,255,255))

lose = font1.render('Игра окончена!', True, (0,0,0))
total = font1.render('СЧЁТ', True, (255,255,255))
total_n = font1.render(str(ball.amount1) + '/' + str(ball.amount2), True, (255,255,255))

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
        ball.reset()
        ball.update()
        window.blit(amount_1, (10,10))
        window.blit(amount_2, (10,30))
        # if sprite.collide_rect(ball, player_2):
        #     amount_2_n += 1
        # if sprite.collide_rect(ball, player_1):
        #     amount_1_n += 1
        if ball.amount1 == 5:
            finish = True
            window.blit(win_1, (200,200))
            window.blit(total, (300,270))
            window.blit(total_n, (330,340))
        if ball.amount2 == 5:
            finish = True
            window.blit(win_2, (200,200))
            window.blit(total, (300,270))
            window.blit(total_n, (330,340))

        if ball.rect.x >= 600 or ball.rect.x <= 0:
            finish = True
            window.blit(lose, (200,200))
            window.blit(total, (300,270))
            window.blit(total_n, (330,340))

    display.update()
    clock.tick(60)
