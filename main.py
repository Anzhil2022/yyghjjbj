import pygame
screen_height = 600
screen_width = 600
screen = pygame.display.set_mode((screen_width, screen_height))
player_x = 100
player_y = 100

pygame.display.set_caption("Gun strike")
player_spite = pygame.image.load(p1.png)
player_spite = pygame.transform.scale(player_spite, (200, 200))

player_move_animation = [pygame.image.load()
                        pygame.image.load()
                        pygame.image.load(







































                            pygame.event.get():

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
               exit()
        elif event.type == pygame. KEYDOWN:
                if event.key == pygame.K_a:
                    player_x -= 5
                if event.key == pygame.K_a:
                    player_x += 5
    x, y = pygame.mouse.get_pos()
    pygame.display.update()























