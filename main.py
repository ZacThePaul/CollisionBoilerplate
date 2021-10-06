import pygame
import random

WIDTH = 1400
HEIGHT = 750
FPS = 40

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("<Pokemon>")
clock = pygame.time.Clock()  ## For syncing the FPS

## group all the sprites together for ease of update
all_sprites = pygame.sprite.Group()
pokemon_sprites = pygame.sprite.Group()
wall_sprites = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.direction = None
        self.editor = False

    def handle_keys(self, walls):
        key = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        dist = 10

        if click[0]:
            if self.editor:
                new_wall = Wall(GREEN, mouse[0] - 10, mouse[1] - 10, 20, 20)
                all_sprites.add(new_wall)
                wall_sprites.add(new_wall)

        if key[pygame.K_3]:
            if not self.editor:
                self.editor = True
            elif self.editor:
                self.editor = False

        if key[pygame.K_s]:  # down key
            move = 0
            for wally in walls:
                if wally.rect.colliderect(
                        pygame.Rect(self.rect.x, self.rect.y + dist, self.rect.width, self.rect.height)):
                    move = 1
            if not move:
                self.rect.y += dist
            else:
                pass
        elif key[pygame.K_w]:  # up key
            move = 0
            for wally in walls:
                if wally.rect.colliderect(pygame.Rect(self.rect.x, self.rect.y - dist, self.rect.width, self.rect.height)):
                    move = 1
            if not move:
                self.rect.y -= dist
            else:
                pass
        if key[pygame.K_d]:  # right key
            move = 0
            for wally in walls:
                if wally.rect.colliderect(pygame.Rect(self.rect.x + dist, self.rect.y, self.rect.width, self.rect.height)):
                    move = 1
            if not move:
                self.rect.x += dist
            else:
                pass
        elif key[pygame.K_a]:  # left key
            move = 0
            for wally in walls:
                if wally.rect.colliderect(pygame.Rect(self.rect.x - dist, self.rect.y, self.rect.width, self.rect.height)):
                    move = 1
            if not move:
                self.rect.x -= dist
            else:
                pass


class Pokemon(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = 1
        self.direction = 'right'

    def update(self, *args, **kwargs) -> None:

        if self.direction == 'right' and self.rect.x + self.rect.width > WIDTH:
            self.direction = 'left'
        if self.direction == 'left' and self.rect.x < 0:
            self.direction = 'right'

        if self.direction == 'right':
            self.rect.x += self.speed
        if self.direction == 'left':
            self.rect.x -= self.speed


class Wall(pygame.sprite.Sprite):

    def __init__(self, color, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#
# class Chat:
#
#     def __init__(self):
#         self.font = pygame.font.Font('freesansbold.ttf', 32)
#         self.text = self.font.render('GeeksForGeeks', True, GREEN, BLUE)


player = Player(BLUE, 10, 20)
pokemon1 = Pokemon(RED, 10, 10)
wall = Wall(GREEN, 100, 100, 20, 200)
wall2 = Wall(RED, 100, 300, 400, 20)

all_sprites.add(player)
all_sprites.add(pokemon1)
all_sprites.add(wall)
all_sprites.add(wall2)

pokemon_sprites.add(pokemon1)

wall_sprites.add(wall)
wall_sprites.add(wall2)

## Game loop
running = True
while running:

    # 1 Process input/events
    clock.tick(FPS)  ## will make the loop run at the same speed all the time
    for event in pygame.event.get():  # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False

    # 2 Update
    all_sprites.update()
    pokemon_sprites.update()

    player.handle_keys(wall_sprites)

    # for pokemon in pokemon_sprites:
    #     if player.rect.colliderect(pokemon):
    #         print(vars(pokemon))
    #         pass

    # for wally in wall_sprites:
    #     if player.rect.colliderect(wally):
    #         print(vars(wally))

    # 3 Draw/render
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, (0, HEIGHT - 50, WIDTH, 50))

    font = pygame.font.Font('freesansbold.ttf', 12)
    text = font.render('Pygame wants to develop using this toolkit.', True, BLACK, WHITE)
    text_rect = text.get_rect()
    text_rect.bottom = HEIGHT
    screen.blit(text, text_rect)


    all_sprites.draw(screen)
    ########################

    ### Your code comes here

    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()

pygame.quit()