import pygame
import random

from constants import *


class Bird(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # characteristics
        self.t = 0
        self.color = "yellow"

        # graphics
        self.image = IMG_birds[self.color][1]
        self.rect = self.image.get_rect()

        self.reset()

    def update(self):
        self.movement += self.gravity
        self.rect.y += self.movement
        if self.movement < 0:
            self.image = IMG_birds[self.color][0]
        elif self.movement == 0:
            self.image = IMG_birds[self.color][1]
        else:
            self.image = IMG_birds[self.color][2]

    def reset(self):
        self.gravity = 0.25
        self.movement = 0
        self.score = 0
        self.rect.center = (120, 350)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Pipe(pygame.sprite.Sprite):

    def __init__(self, height, type):
        """
            type € {"up", "down"}
        """
        super().__init__()
        if type == "down":
            self.image = IMG_pipe_up
            self.rect = self.image.get_rect()
            self.rect.midtop = (450, height)
        else:
            self.image = IMG_pipe_down
            self.rect = self.image.get_rect()
            self.rect.midbottom = (450, height - 200)

    def update(self):
        self.rect.x -= 2
        if self.rect.x < -self.rect.width:
            self.kill()


class Floor:

    def __init__(self):
        self.image = IMG_floor
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.pos1 = [0, YLIM]
        self.pos2 = [0 + 400, YLIM]

    def update(self):
        self.pos1[0] -= 2
        self.pos2[0] -= 2
        if self.pos2[0] < 0:
            self.reset()

    def draw(self, screen):
        screen.blit(self.image, self.pos1)
        screen.blit(self.image, self.pos2)


class Game:

    def __init__(self):

        self.floor = Floor()

        self.pipe_heights = [250, 350, 450, 550]
        self.pipes = pygame.sprite.Group()
        self.reset_pipes()

        self.birds = pygame.sprite.Group()

        # Load pause image
        self.pause_img = None
        try:
            self.pause_img = IMG_PAUSE if 'IMG_PAUSE' in globals(
            ) else pygame.image.load(os.path.join("images", "pause.png"))
        except:
            # Create a simple pause text if image isn't available
            font = pygame.font.SysFont("Arial", 36)
            self.pause_img = font.render("PAUSED", True, (255, 255, 0))

    def reset_pipes(self):
        for pipe in self.pipes:
            pipe.kill()
        self.add_pipes()

    def add_pipes(self):
        random_height = random.choice(self.pipe_heights)
        pipe1 = Pipe(random_height, type="up")
        pipe2 = Pipe(random_height, type="down")
        if len(self.pipes) == 0:
            self.actual_pipe_top = pipe1
            self.actual_pipe_bottom = pipe2
        self.pipes.add(pipe1)
        self.pipes.add(pipe2)

    def draw_score(self, score):

        n = score

        if n < 10:
            self.window.blit(IMG_numbers[n], (200-15, 50))
        elif n < 100:
            i1 = str(n)[0]
            i2 = str(n)[1]
            self.window.blit(IMG_numbers[int(i1)], (200-33, 50))
            self.window.blit(IMG_numbers[int(i2)], (200+3, 50))
        else:
            s = str(n)
            for i in range(len(s)):
                num = int(s[i])
                self.window.blit(IMG_numbers[num], (200-60+i*40, 50))

    def update(self, score, die, game_active, paused=False):
        self.window.blit(IMG_backgroung, (0, 0))

        if game_active and not paused:
            # Bird
            self.birds.update()
            # Pipes
            if not die:
                self.pipes.update()
            self.pipes.draw(self.window)
            # Floor
            self.floor.update()
        elif not game_active:
            self.window.blit(IMG_mesage, (50, 50))

        self.birds.draw(self.window)
        self.floor.draw(self.window)

        if die:
            self.window.blit(IMG_game_over, (50, 270))
        if game_active:
            self.draw_score(score)

        # Show pause image when paused
        if paused:
            # Center the pause image
            pause_rect = self.pause_img.get_rect(
                center=(SIZE_window[0]//2, SIZE_window[1]//2))
            self.window.blit(self.pause_img, pause_rect)

        pygame.display.update()

    def play(self, particular_bird=None):

        bird = Bird() if particular_bird == None else particular_bird
        self.birds.add(bird)

        pygame.init()
        self.window = pygame.display.set_mode(SIZE_window)

        score = 0

        clock = pygame.time.Clock()
        die = False
        run = True
        game_active = False
        paused = False
        SPAWNPIPE = False
        self.reset_pipes()

        i = 0
        while run:
            i += 1

            clock.tick(120)

            for event in pygame.event.get():

                # quit display
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                # Añadir detección de ESC
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        pygame.quit()

                if not game_active:
                    # screen : before start the game -> check SPACE to begin
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            game_active = True

                elif game_active and not die:
                    # Toggle pause with P key
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            paused = not paused

                        # Only process space key when not paused
                        if not paused and event.key == pygame.K_SPACE:
                            bird.movement = 0
                            if bird.rect.top > 0:
                                bird.movement -= 5
                elif die:
                    # bird on the floor (end game) -> check SPACE to reset
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.reset_pipes()
                            bird.reset()
                            game_active = False
                            die = False
                            paused = False
                            score = 0

            # Skip updating game state if paused
            if not paused and game_active and not die:
                # Create new pipes
                if SPAWNPIPE:
                    SPAWNPIPE = False
                    self.add_pipes()
                elif len(self.pipes) > 0 and self.pipes.sprites()[-1].rect.x < 450-300:
                    SPAWNPIPE = True

                # update actual pipe
                if self.actual_pipe_bottom.rect.right < bird.rect.centerx:
                    self.actual_pipe_top = self.pipes.sprites()[-2]
                    self.actual_pipe_bottom = self.pipes.sprites()[-1]
                    bird.score += 1
                    score += 1

                # Collides
                if bird.rect.bottom > YLIM:
                    bird.movement = 0
                    bird.gravity = 0
                    die = True
                if pygame.sprite.spritecollide(bird, self.pipes, dokill=False):
                    die = True

            # Update frame
            self.update(score, die, game_active, paused)

        bird.kill()
        pygame.quit()
        bird.kill()
