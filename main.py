#!/usr/bin/env python3

import pygame, random
from snake import *

def draw_field_grid(screen) -> None:
    '''
    draw field grid
    '''

    color = Colors.Gray_1.value
    for i in range (0, Config.HEIGTH * Config.PIXEL_SIZE, Config.PIXEL_SIZE):
        pygame.draw.line(screen, color, (0, i), (Config.WIDTH * Config.PIXEL_SIZE, i))
    for i in range (0, Config.WIDTH * Config.PIXEL_SIZE, Config.PIXEL_SIZE):
        pygame.draw.line(screen, color, (i, 0), (i, Config.HEIGTH * Config.PIXEL_SIZE))

def draw_item(screen, item: Item, color: Colors) -> None:
    '''
    Draw snake item/apple/stones/etc..
    '''

    x = ((item.X - 1) * Config.PIXEL_SIZE + 1) + Config.PIXEL_BORDER_SIZE
    y = ((item.Y - 1) * Config.PIXEL_SIZE + 1) + Config.PIXEL_BORDER_SIZE
    h = Config.PIXEL_SIZE - Config.PIXEL_BORDER_SIZE * 2 - 1
    w = Config.PIXEL_SIZE - Config.PIXEL_BORDER_SIZE * 2 - 1
    pygame.draw.rect(screen, color.value, (x, y, h, w))

def draw_snake(screen, snake: Snake, game_stoped: bool) -> None:
    '''
    draw snake
    '''

    first = True
    for item in snake:
        if game_stoped: color = Colors.Red
        elif first: color = Config.SNAKE_HEAD_COLOR
        else: color = Config.SNAKE_COLOR
        draw_item(screen, item, color)
        first = False

def init_snake_game_data():
    '''
    Prepare snake game data
    '''

    direction = random.choice([x for x in Direction])
    snake = Snake(random.randint(int(Config.WIDTH * 0.2), int(Config.WIDTH - Config.WIDTH * 0.2)),
                  random.randint(int(Config.HEIGTH * 0.2), int(Config.HEIGTH - Config.HEIGTH * 0.2)),
                  direction)

    return direction, snake

def make_apple(snake: Snake) -> Item:
    while True:
        apple_item = Item(random.randint(1, Config.WIDTH),
                          random.randint(1, Config.HEIGTH))
        if apple_item not in snake:
            break
    print(apple_item)
    return apple_item

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Snake on python')
    screen = pygame.display.set_mode([Config.WIDTH * Config.PIXEL_SIZE,
                                      Config.HEIGTH * Config.PIXEL_SIZE])

    direction, snake = init_snake_game_data()
    apple = make_apple(snake)

    speed = Config.FPS
    eated_apple_count = 0

    running = True
    game_stoped = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if game_stoped:
                        direction, snake = init_snake_game_data()
                        speed = Config.FPS
                        game_stoped = False
                    else:
                        running = False

                elif event.key == pygame.K_UP and direction != Direction.Down:
                    direction = Direction.Up
                elif event.key == pygame.K_DOWN and direction != Direction.Up:
                    direction = Direction.Down
                elif event.key == pygame.K_LEFT and direction != Direction.Right:
                    direction = Direction.Left
                elif event.key == pygame.K_RIGHT and direction != Direction.Left:
                    direction = Direction.Right


        screen.fill(Colors.Black.value)
        draw_field_grid(screen)

        try:
            if not game_stoped:
                head, tail = snake.move(direction)
                if head == apple:
                    snake.add(tail)
                    apple = make_apple(snake)
                    eated_apple_count += 1
                    if eated_apple_count % 10 == 0:
                        speed += 2
        except SnakeCrashException:
            game_stoped = True

        draw_snake(screen, snake, game_stoped)
        draw_item(screen, apple, Colors.Yellow)
        pygame.display.flip()
        clock.tick(speed)

    pygame.quit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
