import pygame
import random
import time
from random import randrange
import DataBaseConnect
import MainMenu


def updateStats(userID: int, score: int):
    print(str(userID) + " : " + str(score))
    DataBaseConnect.updateUserScore(userID, score)
    DataBaseConnect.updateWood(userID, score)
    DataBaseConnect.updateMoney(userID, score*2)


def Game1():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("darkgrey")

        pygame.draw.circle(screen, "green", player_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()


def Game2(userID: int, userName: str):
    pygame.init()

    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    dis_width = 600
    dis_height = 400

    dis = pygame.display.set_mode((dis_width, dis_height))

    clock = pygame.time.Clock()

    snake_block = 10
    snake_speed = 15

    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)

    def Your_score(score):
        value = score_font.render("Your Score: " + str(score), True, red)
        dis.blit(value, [0, 0])

    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])

    def gameLoop():
        game_over = False
        game_close = False

        x1 = dis_width / 2
        y1 = dis_height / 2

        x1_change = 0
        y1_change = 0

        snake_List = []
        Length_of_snake = 1


        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        while not game_over:

            while game_close == True:
                dis.fill(blue)
                message("You Lost! Press C-Play Again or Q-Quit", red)
                Your_score(Length_of_snake - 1)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            updateStats(userID, Length_of_snake - 1)
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            updateStats(userID, Length_of_snake - 1)
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(green)
            pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1

            clock.tick(snake_speed)

        pygame.quit()
        menu = MainMenu.MainMenu(UserName=userName, UserID=userID)
        menu.MenuPage()
        quit()
    gameLoop()


def Game3():

    def Your_score(score):
        value = score_font.render("Your Score: " + str(score), True, 'black')
        screen.blit(value, [0, 0])

    pygame.init()
    window = 1000
    tile_size = 50
    range = (tile_size // 2, window - tile_size // 2, tile_size)
    get_random_position = lambda: [randrange(*range), randrange(*range)]
    snake = pygame.rect.Rect(0, 0, tile_size - 2, tile_size - 2)
    snake.center = get_random_position()
    length = 1
    segments = [snake.copy()]
    snake_dir = (0, 0)
    time, time_step = 0, 110
    food = snake.copy()
    food.center = get_random_position()
    score = 0
    screen = pygame.display.set_mode([window] * 2)
    clock = pygame.time.Clock()
    score_font = pygame.font.SysFont("ariel", 35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            Your_score(length - 1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    snake_dir = (0, -tile_size)
                if event.key == pygame.K_s:
                    snake_dir = (0, +tile_size)
                if event.key == pygame.K_a:
                    snake_dir = (-tile_size, 0)
                if event.key == pygame.K_d:
                    snake_dir = (+tile_size, 0)


        screen.fill("darkgrey")
        self_eating = pygame.Rect.collidelist(snake, segments[:-1]) != -1

        if snake.left < 0 or snake.right > window or snake.top < 0 or snake.bottom > window or self_eating:
            snake.center, food.center = get_random_position(), get_random_position()
            length, snake_dir, score = 1, (0, 0), 0
            segments = [snake.copy()]

        if snake.center == food.center:
            food.center = get_random_position()
            length += 1
            score += 1


        pygame.draw.rect(screen, 'red', food)
        [pygame.draw.rect(screen, 'green', segment) for segment in segments]
        time_now = pygame.time.get_ticks()
        if time_now - time > time_step:
            time = time_now
            snake.move_ip(snake_dir)
            segments.append(snake.copy())
            segments = segments[-length:]
        pygame.display.flip()
        clock.tick(60)
