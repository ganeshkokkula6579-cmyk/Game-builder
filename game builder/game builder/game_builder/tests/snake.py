import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
SPEED = 10
BLOCK_SIZE = 20

# Set up some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the snake
snake = [(200, 200), (220, 200), (240, 200)]
direction = (1, 0)

# Set up the food
food = (
    random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
    random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
)

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    # Move the snake
    head = snake[0]
    new_head = (
        head[0] + direction[0] * BLOCK_SIZE,
        head[1] + direction[1] * BLOCK_SIZE,
    )
    snake.insert(0, new_head)

    # Check for collision with food
    if snake[0] == food:
        food = (
            random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
            random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
        )
    else:
        snake.pop()

    # Check for collision with walls or itself
    if (
        snake[0][0] < 0
        or snake[0][0] >= WIDTH
        or snake[0][1] < 0
        or snake[0][1] >= HEIGHT
        or snake[0] in snake[1:]
    ):
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(BLACK)
    for pos in snake:
        pygame.draw.rect(screen, WHITE, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    text = font.render("Score: " + str(len(snake)), True, WHITE)
    screen.blit(text, (10, 10))
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(1000 // SPEED)
