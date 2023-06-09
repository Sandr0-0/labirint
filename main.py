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
        self.direction = "left"
        self.image_l = self.image
        self.image_r = pygame.transform.flip(self.image, True, False)

    def update(self):
        if self.speed_x < 0 and self.rect.left > 0 or self.speed_x > 0 and self.rect.right < WIN_WIDTH:
            self.rect.x += self.speed_x
        if self.speed_y < 0 and self.rect.top > 0 or self.speed_y > 0 and self.rect.bottom < WIN_HEIGHT:
            self.rect.y += self.speed_y




player = Player(5, 5, 60, 80, r"image\vs2.png", 0, 0)
enemy1 = GameSprite(200, 60 , 60, 60, r"image\huskar.jpg")
goal = GameSprite(500, 60, 80, 80, r"image\tron.jpg")


walls = pygame.sprite.Group()
wall1 = GameSprite(100, 100, 20, 400, r"image\WALL.png")
walls.add(wall1)
wall2 = GameSprite(300, 600, 300, 20, r"image\WALL.png")
walls.add(wall2)


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
        goal.show()
    clock.tick(FPS)
    pygame.display.update()