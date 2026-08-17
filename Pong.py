import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

clock = pygame.time.Clock()
FPS = 60
font = pygame.font.SysFont("Arial", 40)

ORANGE = (255, 165, 0)
CYAN = (64, 224, 208)
PINK = (255, 105, 180)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 20, 60)

paddle_width = 100
paddle_height = 10
paddle_speed = 10

paddle_a_x = WIDTH // 2 - paddle_width // 2
paddle_a_y = HEIGHT - 30

paddle_b_x = WIDTH // 2 - paddle_width // 2
paddle_b_y = 20

ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 7
ball_speed_y = 7

score_a = 0
score_b = 0


def reset_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y

    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2

    ball_speed_x = 7
    ball_speed_y = 7


running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and paddle_a_x > 0:
        paddle_a_x -= paddle_speed

    if keys[pygame.K_RIGHT] and paddle_a_x < WIDTH - paddle_width:
        paddle_a_x += paddle_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x <= 0 or ball_x >= WIDTH:
        ball_speed_x *= -1

    if ball_y <= 0:
        score_a += 1
        reset_ball()

    if ball_y >= HEIGHT:
        score_b += 1
        reset_ball()

    paddle_b_x = ball_x - paddle_width // 2

    if paddle_b_x < 0:
        paddle_b_x = 0

    if paddle_b_x > WIDTH - paddle_width:
        paddle_b_x = WIDTH - paddle_width

    ball_rect = pygame.Rect(
        ball_x - 10,
        ball_y - 10,
        20,
        20
    )

    paddle_a_rect = pygame.Rect(
        paddle_a_x,
        paddle_a_y,
        paddle_width,
        paddle_height
    )

    paddle_b_rect = pygame.Rect(
        paddle_b_x,
        paddle_b_y,
        paddle_width,
        paddle_height
    )

    if ball_rect.colliderect(paddle_a_rect) and ball_speed_y > 0:
        ball_speed_y *= -1

    if ball_rect.colliderect(paddle_b_rect) and ball_speed_y < 0:
        ball_speed_y *= -1

    if score_a >= 5 or score_b >= 5:

        screen.fill(BLACK)

        winner = "Player A" if score_a >= 5 else "Player B"

        winner_text = font.render(
            f"{winner} Wins!",
            True,
            RED
        )

        score_text = font.render(
            f"Score: {score_a} - {score_b}",
            True,
            WHITE
        )

        screen.blit(
            winner_text,
            winner_text.get_rect(
                center=(WIDTH // 2, HEIGHT // 2 - 50)
            )
        )

        screen.blit(
            score_text,
            score_text.get_rect(
                center=(WIDTH // 2, HEIGHT // 2 + 20)
            )
        )

        pygame.display.flip()

        pygame.time.wait(2500)

        score_a = 0
        score_b = 0
        paddle_a_x = WIDTH // 2 - paddle_width // 2
        reset_ball()

    screen.fill(ORANGE)


    pygame.draw.rect(
        screen,
        CYAN,
        (
            paddle_a_x,
            paddle_a_y,
            paddle_width,
            paddle_height
        )
    )

   
    pygame.draw.rect(
        screen,
        PINK,
        (
            paddle_b_x,
            paddle_b_y,
            paddle_width,
            paddle_height
        )
    )

    # Draw ball
    pygame.draw.circle(
        screen,
        YELLOW,
        (int(ball_x), int(ball_y)),
        10
    )

    # Draw score
    score_text = font.render(
        f"{score_a} - {score_b}",
        True,
        GOLD
    )

    screen.blit(
        score_text,
        score_text.get_rect(
            center=(WIDTH // 2, 40)
        )
    )

    pygame.display.flip()

    clock.tick(FPS)


pygame.quit()
sys.exit()