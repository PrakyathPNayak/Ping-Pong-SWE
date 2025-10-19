import pygame
import random

class Ball:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.original_x = x
        self.original_y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.velocity_x = random.choice([-5, 5])
        self.velocity_y = random.choice([-3, 3])
        

    def move(self, player, ai, paddle_hit_sound=None, wall_bounce_sound=None):
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Wall collision (top/bottom)
        if self.y <= 0 or self.y + self.height >= self.screen_height:
            self.velocity_y *= -1
            if wall_bounce_sound:
                wall_bounce_sound.play()

        # Paddle collision check
        if self.rect().colliderect(player.rect()):
            self.x = player.x + player.width  # prevent sticking
            self.velocity_x = abs(self.velocity_x)
            if paddle_hit_sound:
                paddle_hit_sound.play()
        elif self.rect().colliderect(ai.rect()):
            self.x = ai.x - self.width
            self.velocity_x = -abs(self.velocity_x)
            if paddle_hit_sound:
                paddle_hit_sound.play()


    def check_collision(self, player, ai):
        if self.rect().colliderect(player.rect()) or self.rect().colliderect(ai.rect()):
            self.velocity_x *= -1

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.velocity_x *= -1
        self.velocity_y = random.choice([-3, 3])

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
