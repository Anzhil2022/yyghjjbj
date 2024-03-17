import pygame
screen_width = 600
screen_height = 600
player_x = 100
player_y = 100
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gun strike")
bullet_sprite = pygame.image.load("пуля.png")

player_move_animation = [pygame.image.load("player_walk_1.png"),
                         pygame.image.load("player_walk_2.png"),
                         pygame.image.load("player_walk_3.png")]
bullet_list = [] # список всех пулек на экране

clock = pygame.time.Clock()
current_sprite = 0
player_on_platform = False
def spawn_bullet(): # cоздоёт новою пулю на экране
    bullet_list.append([player_x, player_y, "right"]) # добавления пули в список
def bullet_control(): # контролирует передвижения и попадание в цели
    for bullet in bullet_list:
        if bullet[2] == "right":
            bullet[0] += 5
        if bullet[2] == "left":
            bullet[0] -= 5



def move_char():
    global player_x
    global player_y
    if pressed_key == "d":
        player_x += 1.5 # скорость передвижения персонажа
    if pressed_key == "a":
        player_x -= 1.5 # скорость передвежения персонажа

def draw_scren (): # создания функций рисования экрана
    global current_sprite, player_x, player_y
    screen.fill("#2A6FE5")
    screen.blit(player_move_animation[current_sprite], (player_x, player_y))
    for bullet in bullet_list:
        screen.blit(bullet_sprite, (bullet[0], bullet[1]))
    pygame.display.update()
def walk_anim():  # Функция, воспроизводящая анимацию спрайта
    global current_sprite
    if pressed_key != None:
        current_sprite += +1
        if len(player_move_animation) < current_sprite+1:
            current_sprite = 0


def jump():
    global up_speed, player_y
    up_speed = 20
    player_y -= 5

def physics_connrol():
    global player_y, up_speed
    player_y -= up_speed
    up_speed -= 1
    if player_y+85 > screen_height-20:
        up_speed = 0
        player_y = screen_height-85

pressed_key = None # отслеживает нажата ли клавиша движения
i_count = 0 # счетчик для анимации
up_speed = 0
while True:
    i_count += 1
    move_char()
    physics_connrol()
    for event in pygame.event.get(): # Перебор всех событий (нажатия клавиш)
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: # персанаж идёт в влево
                pressed_key = "a"
            if event.key == pygame.K_d: # персонаж идёт в право
                pressed_key = "d"
            if event.key == pygame.K_w: # персонаж идёт в вверх
                pressed_key = "w"
            if event.key == pygame.K_s: # персонаж идёт в вниз
                pressed_key = "s"
            if event.key == pygame.K_SPACE: # персонаж прыгает
                jump()

        elif event.type == pygame.KEYUP:
            pressed_key = None

    if i_count%8 == 0:
        walk_anim()
    bullet_control()
    draw_scren()
    clock.tick(60)



