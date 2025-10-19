import pygame
from game.game_engine import GameEngine

# Initialize pygame/Start application
pygame.init()
pygame.mixer.init()


# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong - Pygame Version")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Game loop
engine = GameEngine(WIDTH, HEIGHT)

def show_replay_menu(screen):
    font = pygame.font.SysFont("Arial", 30)
    options = [
        ("3 - Best of 3", 3),
        ("5 - Best of 5", 5),
        ("7 - Best of 7", 7),
        ("ESC - Exit", "exit")
    ]

    while True:
        screen.fill((0, 0, 0))
        for i, (text, _) in enumerate(options):
            render = font.render(text, True, (255, 255, 255))
            rect = render.get_rect(center=(400, 200 + i * 50))
            screen.blit(render, rect)

        pygame.display.flip()

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3: return 3
                if event.key == pygame.K_5: return 5
                if event.key == pygame.K_7: return 7
                if event.key == pygame.K_ESCAPE: return "exit"


def main():
    running = True
    while running:
        SCREEN.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not engine.game_over:
            engine.handle_input()
            engine.update()
            engine.render(SCREEN)
        else:
            replay_choice = show_replay_menu(SCREEN)
            if replay_choice == "exit":
                running = False
            else:
                engine.winning_score = replay_choice
                engine.player_score = 0
                engine.ai_score = 0
                engine.ball.reset()
                engine.game_over = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
