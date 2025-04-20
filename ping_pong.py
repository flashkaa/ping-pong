from pygame import *


class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed


        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

    def fire(self):
        bullet = Bullet(img_bullet,self.rect.centerx,self.rect.top,15,20,-15)
        bullets.add(bullet)



back = 'stol.png'
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(back),(win_width,win_height))

game = True
finish = False
clock= time.Clock()
FPS = 60


racket1 = Player('raketka.png', 480,200,60,80,4)
racket2 = Player('raketka2.png', 80,200,60,80,4)
ball = GameSprite('ball.png', 200,200,40,40,4)

font.init()
font = font.Font(None,35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180,0,0))
lose2 = font.render('PLAYER 2 LOSE!', True,(180,0,0))



speed_x =3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish !=True:
        window.blit(background,(0,0))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y


    if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
        speed_x*= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200,200))
        game_over = True

    if ball.rect.x >win_width:
        finish = True
        window.blit(lose2, (200,200))
        game_over = True


    racket1.reset()
    racket2.reset()
    ball.reset()


    display.update()
    clock.tick(FPS)