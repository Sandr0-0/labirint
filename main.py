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

fon = pygame.image.load(file_path(r"image\fon.jpg"))
fon = pygame.transform.scale(fon, (WIN_WIDTH, WIN_HEIGHT))

image_win = pygame.image.load(file_path(r"image\tron.jpg"))
image_win = pygame.transform.scale(image_win, (WIN_WIDTH, WIN_HEIGHT))

image_lose = pygame.image.load(file_path(r"image\tron.jpg"))
image_win = pygame.transform.scale(image_win,(WIN_WIDTH, WIN_HEIGHT))


window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()

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

    def update(self):
        if self.speed_x < 0 and self.rect.left > 0 or self.speed_x > 0 and self.rect.right < WIN_WIDTH:
            self.rect.x += self.speed_x
        if self.speed_y < 0 and self.rect.top > 0 or self.speed_y > 0 and self.rect.bottom < WIN_HEIGHT:
            self.rect.y += self.speed_y




player = Player(5, 5, 80, 100, r"image\pudge(6).png", 0, 0)
enemy1 = GameSprite(620, 200 , 100, 150, r"image\huskar2(2).png")
enemy2 = GameSprite(600, 10, 100, 100, r"image\rasta(1).png")
goal = GameSprite(820, 40, 80, 80, r"image\tron2.png")
portal1 = GameSprite(220, 140, 60, 60, r"image\portal1 — копия.png")
portal2 = GameSprite(840, 220, 60, 60, r"image\portal2 — копия.png")
item1 = GameSprite(840, 720, 60, 60, r"image\aghanim.png")
item2 = GameSprite(730, 220, 70, 70, r"image\bkb.png")

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

















level = 1
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
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.speed_x = 0
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.speed_x = 0
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.speed_y = 0
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.speed_y = 0

    if level == 1:
        window.blit(fon, (0, 0))
        walls.draw(window)
        player.show()
        player.update()
        enemy1.show()
        enemy2.show()
        goal.show()
        portal2.show()
        portal1.show()
        item1.show()
        item2.show()

        if pygame.sprite.collide_rect(player, goal):
            level = 10

    elif level == 10:
        window.blit(image_win, (0, 0))


    clock.tick(FPS)
    pygame.display.update()