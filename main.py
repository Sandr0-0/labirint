import pygame
import os 
pygame.init()

def file_path(file_name):
    folder = os.path.abspath(__file__ + "/..")
    path = os.path.join(folder, file_name)
    return path
    
WIN_WIDTH = 900
WIN_HEIGHT = 800
FPS = 40

BLACK = (0, 0, 0)
GRAY = (140, 143, 140)
LIGHT_GREEN = (203, 242, 203)
WHITE = (255, 255, 255)
DARK = (77, 79, 77)

pygame.mixer.music.load(file_path(r"music\bfacb78306248c8.mp3"))
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

music_shoot = pygame.mixer.Sound(file_path(r"image\odinochnyiy-pistoletnyiy-vyistrel.ogg"))

fon = pygame.image.load(file_path(r"image\fon.jpg"))
fon = pygame.transform.scale(fon, (WIN_WIDTH, WIN_HEIGHT))

image_win = pygame.image.load(file_path(r"image\tron.jpg"))
image_win = pygame.transform.scale(image_win, (WIN_WIDTH, WIN_HEIGHT))

image_lose = pygame.image.load(file_path(r"image\tron.jpg"))
image_lose = pygame.transform.scale(image_win,(WIN_WIDTH, WIN_HEIGHT))


window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()



class Button():
    def __init__(self, x, y, width, height, color1, color2, text, text_color, text_x, text_y):
        self.rect = pygame.Rect(x, y, width, height)
        self.color1 = color1
        self.color2 = color2
        self.color = color1
        shrift = pygame.font.SysFont("Comix Sans MS", 80)
        self.text = shrift.render(text, True, text_color)
        self.text_x = text_x
        self.text_y = text_y

    def show(self):
        pygame.draw.rect(window, self.color, self.rect)
        window.blit(self.text, (self.rect.x + self.text_x, self.rect.y + self.text_y ))




class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load(file_path(image))
        self.image = pygame.transform.scale(self.image, (width, height))

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, x, y, width, height, image, speed_x, speed_y ):
        super().__init__(x, y, width, height, image)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.direction = "right"
        self.image_r = self.image
        self.image_l = pygame.transform.flip(self.image, True, False)
    

    def shoot(self):
        if self.direction == "right":
            bullet = Bullet(self.rect.right, self.rect.centery, 20, 20, r"image\bullet.png", 8)
        elif self.direction == "left":
            bullet = Bullet(self.rect.left - 20, self.rect.centery, 20, 20, r"image\bullet.png", -8)
            bullet.image = pygame.transform.flip(bullet.image, True, False)
        bullets.add(bullet)


    def update(self):
        if self.speed_x < 0 and self.rect.left > 0 or self.speed_x > 0 and self.rect.right < WIN_WIDTH:
            self.rect.x += self.speed_x
        walls_touched = pygame.sprite.spritecollide(self, walls, False)
        if self.speed_x > 0:
            for wall in walls_touched:
               self.rect.right = min(self.rect.right, wall.rect.left) 
        if self.speed_x < 0:
            for wall in walls_touched:
               self.rect.left = max(self.rect.left, wall.rect.right)

        if self.speed_y < 0 and self.rect.top > 0 or self.speed_y > 0 and self.rect.bottom < WIN_HEIGHT:
            self.rect.y += self.speed_y

        walls_touched = pygame.sprite.spritecollide(self, walls, False)
        if self.speed_y < 0:
            for wall in walls_touched:
                self.rect.top = max(self.rect.top, wall.rect.bottom)
        if self.speed_y > 0:
            for wall in walls_touched:
                self.rect.bottom = min(self.rect.bottom, wall.rect.top)
        

class Bullet(GameSprite):
    def __init__(self, x, y, width, height, image, speed):
        super().__init__(x, y, width, height, image)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.right >= WIN_WIDTH or self.rect.left <= 0:
            self.kill()






class Enemy(GameSprite):
    def __init__(self, x, y, width, height, image, direction, min_coord, max_coord, speed):
        super().__init__(x, y, width, height, image)
        self.direction = direction
        self.min_coord = min_coord
        self.max_coord = max_coord
        self.speed = speed

        if self.direction == "right":
            self.image_r = self.image
            self.image_l = pygame.transform.flip(self.image, True, False)
        
        elif self.direction == "left":
            self.image_l = self.image
            self.image_r = pygame.transform.flip(self.image, True, False)



    def update(self):
        if self.direction == "left" or self.direction == "right":
            if self.direction == "left":
                self.rect.x -= self.speed

            elif self.direction == "right":
                self.rect.x += self.speed


            if self.rect.right >= self.max_coord:
                self.direction = "left"
                self.image = self.image_l
            if self.rect.right <=  self.min_coord:
                self.direction = "right"
                self.image = self.image_r

        elif self.direction == "up" or self.direction == "down":
            if self.direction == "up":
                self.rect.y -= self.speed
            elif self.direction == "down":
                self.rect.y += self.speed

            if self.rect.top <= self.min_coord:
                self.direction = "down"
            if self.rect.bottom >= self.max_coord:
                self.direction = "up"







player = Player(5, 5, 60, 70, r"image\pudge(6).png", 0, 0)
enemy1 = Enemy(620, 200 , 100, 150, r"image\huskar2(2).png", "down", 100, 500, 5)
enemy2 = Enemy(600, 10, 100, 100, r"image\rasta(1).png", "left", 600, 900, 5)
goal = GameSprite(820, 1, 80, 80, r"image\tron2.png")
portal1 = GameSprite(220, 140, 60, 60, r"image\portal1 — копия.png")
portal2 = GameSprite(840, 220, 60, 60, r"image\portal2 — копия.png")
item1 = GameSprite(840, 720, 60, 60, r"image\aghanim.png")
item2 = GameSprite(730, 220, 70, 70, r"image\bkb.png")

bullets = pygame.sprite.Group()



enemies = pygame.sprite.Group()
enemies.add(enemy1)
enemies.add(enemy2)

walls = pygame.sprite.Group()
wall1 = GameSprite(90, 0, 10, 650, r"image\WALL.png")
walls.add(wall1)

wall2 = GameSprite(90, 800, 10, 0, r"image\WALL.png")
walls.add(wall2)

wall3 = GameSprite(90, 650, 100, 10, r"image\WALL.png")
walls.add(wall3)

wall4 = GameSprite(90, 0, 810, 10, r"image\WALL.png")
walls.add(wall4)

wall5 = GameSprite(90, 780, 810, 10, r"image\WALL.png")
walls.add(wall5)

wall6 = GameSprite(0, 00, 0, 0, r"image\WALL.png")
walls.add(wall6)

wall7 = GameSprite(300, 540, 10, 240, r"image\WALL.png")
walls.add(wall7)

wall8 = GameSprite(0, 0, 0, 0, r"image\WALL.png")
walls.add(wall8)

wall9 = GameSprite(90, 400, 650, 10, r"image\WALL.png")
walls.add(wall9)

wall10 = GameSprite(200, 540, 100, 10, r"image\WALL.png")
walls.add(wall10)


wall11 = GameSprite(450, 400, 10, 250, r"image\WALL.png")
walls.add(wall11)

wall12= GameSprite(600, 540, 10, 240, r"image\WALL.png")
walls.add(wall12)

wall13 = GameSprite(730, 400, 10, 200, r"image\WALL.png")
walls.add(wall13)

wall14 = GameSprite(780, 700, 10, 90, r"image\WALL.png")
walls.add(wall14)

wall15 = GameSprite(600, 250, 10, 150, r"image\WALL.png")
walls.add(wall15)

wall16 = GameSprite(470, 120, 500, 10, r"image\WALL.png")
walls.add(wall16)

wall17 =  GameSprite(720, 120, 10, 170, r"image\WALL.png")
walls.add(wall17)

wall18 =  GameSprite(720, 290, 180, 10, r"image\WALL.png")
walls.add(wall18)

wall19 =  GameSprite(470, 120, 10, 190, r"image\WALL.png")
walls.add(wall19)

wall20 =  GameSprite(300, 310, 181, 10, r"image\WALL.png")
walls.add(wall20)

wall21 =  GameSprite(200, 100, 10, 210, r"image\WALL.png")
walls.add(wall21)

wall22 =  GameSprite(300, 10, 10, 200, r"image\WALL.png")
walls.add(wall22)

wall23 =  GameSprite(200, 210, 110, 10, r"image\WALL.png")
walls.add(wall23)




btn_start = Button(300, 200, 300, 100, GRAY, DARK, "S T A R T", WHITE, 30, 25)
btn_exit = Button(300, 500, 300, 100, GRAY, DARK, "E X I T", WHITE, 65, 25)
game_name = pygame.font.SysFont("Tahoma", 60, 1, 1).render("P u d g e   E s c a p e", True, WHITE)










level = 0
game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if level == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.speed_x = -5
                    player.direction = "left"
                    player.image = player.image_l
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.speed_x = 5
                    player.direction = "right"
                    player.image = player.image_r
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.speed_y = -5
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.speed_y = 5
                if event.key == pygame.K_SPACE:
                    player.shoot()
                    music_shoot.play()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.speed_x = 0
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.speed_x = 0
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.speed_y = 0
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.speed_y = 0

        elif level == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if btn_start.rect.collidepoint(x, y):
                    level = 1
                    pygame.mixer.music.load(file_path(r"music\26eb2b766b3ccf2.mp3"))
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.music.play(-1)
                elif btn_exit.rect.collidepoint(x, y):
                    game = False
            
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if btn_start.rect.collidepoint(x, y):
                    btn_start.color = btn_start.color2

                elif btn_exit.rect.collidepoint(x, y):
                    btn_exit.color = btn_exit.color2

                else:
                    btn_exit.color = btn_exit.color1
                    btn_start.color = btn_start.color1

    if level == 1:
        window.blit(fon, (0, 0))
        walls.draw(window)
        player.show()
        player.update()
        enemies.draw(window)
        enemies.update()
        goal.show()
        portal2.show()
        portal1.show()
        item1.show()
        item2.show()
        bullets.draw(window)
        bullets.update()
        if pygame.sprite.collide_rect(player, goal):
            level = 10
            pygame.mixer.music.stop()
            pygame.mixer.music.load(file_path(r"music\a5230bf64dffcb6.mp3"))
            pygame.mixer.music.play(-1)

        if pygame.sprite.spritecollide(player, enemies, False):
            level = 11
            pygame.mixer.music.stop()
            pygame.mixer.music.load(file_path(r"music\bfacb78306248c8.mp3"))
            pygame.mixer.music.play(-1)

        pygame.sprite.groupcollide(bullets, walls, True, False)
        pygame.sprite.groupcollide(bullets, enemies, True, True)


    elif level == 0:
        window.fill(BLACK)
        btn_start.show()
        btn_exit.show()
        window.blit(game_name, (100, 30))

    elif level == 10:
        window.blit(image_win, (0, 0))

    elif level == 11:
        window.blit(image_lose, (0, 0))
    clock.tick(FPS)
    pygame.display.update()