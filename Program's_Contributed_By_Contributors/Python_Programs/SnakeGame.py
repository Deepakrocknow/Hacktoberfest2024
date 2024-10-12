import pygame
import time
import random

pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game : ")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Clock and font
clock = pygame.time.Clock()
snake_speed = 15
font = pygame.font.SysFont("bahnschrift", 25)

def display_score(score):
    value = font.render(f"Score: {score}", True, white)
    screen.blit(value, [0, 0])

def game_over_message():
    msg = font.render("Game Over! Press R to Restart or Q to Quit", True, red)
    screen.blit(msg, [width / 6, height / 3])

def game_loop():
    game_over = False
    game_close = False

    x, y = width / 2, height / 2
    dx, dy = 0, 0

    snake_body = []
    snake_length = 1

    food_x = round(random.randrange(0, width - 10) / 10.0) * 10
    food_y = round(random.randrange(0, height - 10) / 10.0) * 10

    while not game_over:
        while game_close:
            screen.fill(black)
            game_over_message()
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -10, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = 10, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -10
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, 10

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += dx
        y += dy
        screen.fill(black)

        pygame.draw.rect(screen, green, [food_x, food_y, 10, 10])
        snake_head = [x, y]
        snake_body.append(snake_head)

        if len(snake_body) > snake_length:
            del snake_body[0]

        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_close = True

        for segment in snake_body:
            pygame.draw.rect(screen, blue, [segment[0], segment[1], 10, 10])

        display_score(snake_length - 1)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - 10) / 10.0) * 10
            food_y = round(random.randrange(0, height - 10) / 10.0) * 10
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
