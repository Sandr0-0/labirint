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


player = GameSprite(5, 5, 60, 80, r"image\vs2.png")
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
        window.blit(fon, (0, 0))
        walls.draw(window)
        player.show()
        enemy1.show()
        goal.show()
    clock.tick(FPS)
    pygame.display.update()