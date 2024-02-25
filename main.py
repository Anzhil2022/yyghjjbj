import pygame
screen_width = 600
screen_height = 600
player_x = 100
player_y = 100
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gun strike")
player_sprite = pygame.image.load("sprites\\player.png")
player_sprite = pygame.transform.scale(player_sprite, (200, 200))
bullet_sprite = pygame.image.load("sprites\\bullet.png")

player_move_animation = [pygame.image.load("sprites\\player_walk_1.png"),
                         pygame.image.load("sprites\\player_walk_2.png"),
                         pygame.image.load("sprites\\player_walk_3.png")]
bullet_list = [] # список всех пулек на экране


current_sprite = 0
def spawn_bullet(): # cоздоёт новою пулю на экране
    bullet_list.append([player_x, player_y]) # добавления пули в список


def move_char():
    global player_x
    global player_y
    if pressed_key == "d":
        player_x += 5 # скорость передвижения персонажа
    if pressed_key == "a":
        player_x -= 5  # скорость передвежения персонажа

def walk_anim():  # Функция, воспроизводящая анимацию спрайта
    global current_sprite
    if pressed_key != None:
        current_sprite += 1
        if len(player_move_animation) < current_sprite+1:
            current_sprite = 0

pressed_key = None #
i_count = 0 # счетчик для анимации
while True:
    i_count += 1
    for event in pygame.event.get(): # Перебор всех событий (нажатия клавиш)
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                pressed_key = "a"
            if event.key == pygame.K_d:
                pressed_key = "d"
        elif event.type == pygame.KEYUP:
            pressed_key = None

    if i_count%60 == 0:
        walk_anim()
    move_char
    screen.fill("#2A6FE5")
    screen.blit(player_move_animation[current_sprite], (player_x, player_y))
    pygame.display.update()