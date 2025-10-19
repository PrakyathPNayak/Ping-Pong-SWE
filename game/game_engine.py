import pygame
from .paddle import Paddle
from .ball import Ball

# Game Engine

WHITE = (255, 255, 255)

class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.paddle_width = 10
        self.paddle_height = 100

        self.player = Paddle(10, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ai = Paddle(width - 20, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ball = Ball(width // 2, height // 2, 7, 7, width, height)

        self.player_score = 0
        self.ai_score = 0
        self.font = pygame.font.SysFont("Arial", 30)
        self.winning_score = 5
        self.game_over = False
        self.paddle_hit_sound = pygame.mixer.Sound("assets/paddle_hit.wav")
        self.wall_bounce_sound = pygame.mixer.Sound("assets/wall_bounce.wav")
        self.score_sound = pygame.mixer.Sound("assets/score.wav")


    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move(-10, self.height)
        if keys[pygame.K_s]:
            self.player.move(10, self.height)

    def update(self):
        if self.game_over:
            return

        self.ball.move(self.player, self.ai, self.paddle_hit_sound, self.wall_bounce_sound)

        if self.ball.x <= 0:
            self.ai_score += 1
            if self.score_sound: self.score_sound.play()
            self.ball.reset()
        elif self.ball.x >= self.width:
            self.player_score += 1
            if self.score_sound: self.score_sound.play()
            self.ball.reset()

        self.ai.auto_track(self.ball, self.height)


    def render(self, screen):
        # Draw paddles and ball
        pygame.draw.rect(screen, WHITE, self.player.rect())
        pygame.draw.rect(screen, WHITE, self.ai.rect())
        pygame.draw.ellipse(screen, WHITE, self.ball.rect())
        pygame.draw.aaline(screen, WHITE, (self.width//2, 0), (self.width//2, self.height))

        # Draw score
        player_text = self.font.render(str(self.player_score), True, WHITE)
        ai_text = self.font.render(str(self.ai_score), True, WHITE)
        screen.blit(player_text, (self.width//4, 20))
        screen.blit(ai_text, (self.width * 3//4, 20))
        self.check_game_over(screen)

    def check_game_over(self, screen):
        if self.player_score >= self.winning_score:
            self.display_message(screen, "Player Wins!")
            self.game_over = True
        elif self.ai_score >= self.winning_score:
            self.display_message(screen, "AI Wins!")
            self.game_over = True

    def display_message(self, screen, message):
        text = self.font.render(message, True, (255, 255, 255))
        rect = text.get_rect(center=(self.width // 2, self.height // 2))
        screen.blit(text, rect)
        pygame.display.flip()
        pygame.time.delay(2000)

