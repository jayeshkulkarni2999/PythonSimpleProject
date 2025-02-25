import pygame
import random
import time  # For tracking confetti duration

pygame.init()

# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

START = pygame.image.load(r"D:\Python\Assets\Dino\DinoStart.png")


RUNNING = [
    pygame.image.load(r"D:\Python\Assets\Dino\DinoRun1.png"),
    pygame.image.load(r"D:\Python\Assets\Dino\DinoRun2.png"),
]

JUMPING = pygame.image.load(r"D:\Python\Assets\Dino\DinoJump.png")

DUCKING = [
    pygame.image.load(r"D:\Python\Assets\Dino\DinoDuck1.png"),
    pygame.image.load(r"D:\Python\Assets\Dino\DinoDuck2.png"),
]

SMALL_CACTUS = [
    pygame.image.load(r"D:\Python\Assets\Cactus\SmallCactus1.png"),
    pygame.image.load(r"D:\Python\Assets\Cactus\SmallCactus2.png"),
    pygame.image.load(r"D:\Python\Assets\Cactus\SmallCactus3.png"),
]

LARGE_CACTUS = [
    pygame.image.load(r"D:\Python\Assets\Cactus\LargeCactus1.png"),
    pygame.image.load(r"D:\Python\Assets\Cactus\LargeCactus2.png"),
    pygame.image.load(r"D:\Python\Assets\Cactus\LargeCactus3.png"),
]

BIRD = [
    pygame.image.load(r"D:\Python\Assets\Bird\Bird1.png"),
    pygame.image.load(r"D:\Python\Assets\Bird\Bird2.png"),
]

CLOUD = pygame.image.load(r"D:\Python\Assets\Other\Cloud.png")

BG = pygame.image.load(r"D:\Python\Assets\Other\Track.png")


class Dinosaur:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        # Get the images of the dinosaur's actions
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING

        # Set the state variables of the dinosaur
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (userInput[pygame.K_DOWN] or self.dino_jump):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        self.image = self.duck_img[self.step_index % 2]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index % 2]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img

        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 5
            self.jump_vel -= 0.8

        if self.jump_vel < -self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1

class Confetti:
    def __init__(self):
        self.particles = []
        self.start_time = None

    def create_confetti(self):
        self.start_time = time.time()  # Set the start time when confetti is triggered
        self.particles = []

        for _ in range(50):  # Number of confetti particles
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT // 2)  # Spawn from the top
            size = random.randint(3, 8)
            color = random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)])
            speed = random.uniform(1, 3)
            self.particles.append([x, y, size, color, speed])

    def update_and_draw(self, screen):
        if self.start_time and time.time() - self.start_time > 1.5:  # Remove confetti after 1.5 secs
            self.particles = []
            self.start_time = None

        if not self.particles:
            return  # Don't render if no confetti
        
        confetti_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT // 2), pygame.SRCALPHA)  # Transparent surface
        for particle in self.particles:
            particle[1] += particle[4]  # Move downward
            particle[0] += random.choice([-1, 0, 1])  # Slight drift
            pygame.draw.circle(confetti_surface, particle[3], (particle[0], int(particle[1])), particle[2])

        screen.blit(confetti_surface, (0, 0))  # Draw confetti only in top half

class TransitionManager:
    def __init__(self):
        self.transition_active = False
        self.start_time = None
        self.target_color = (255, 255, 255)  # Start with white
        self.current_bg = (255, 255, 255)
        self.current_fg = (0, 0, 0)  # Foreground (text, dino, obstacles)
        self.transition_duration = 3  # 3 seconds transition

    def start_transition(self, target_bg, target_fg):
        self.transition_active = True
        self.start_time = time.time()
        self.target_color = target_bg
        self.target_fg = target_fg  # Foreground color switch

    def update(self):
        if not self.transition_active:
            return self.current_bg, self.current_fg  # No transition, return current colors

        elapsed = time.time() - self.start_time
        t = min(1, elapsed / self.transition_duration)  # Normalize time (0 to 1)

        # Interpolate background color
        r = int((1 - t) * self.current_bg[0] + t * self.target_color[0])
        g = int((1 - t) * self.current_bg[1] + t * self.target_color[1])
        b = int((1 - t) * self.current_bg[2] + t * self.target_color[2])
        self.current_bg = (r, g, b)

        # Interpolate foreground color
        r_fg = int((1 - t) * self.current_fg[0] + t * self.target_fg[0])
        g_fg = int((1 - t) * self.current_fg[1] + t * self.target_fg[1])
        b_fg = int((1 - t) * self.current_fg[2] + t * self.target_fg[2])
        self.current_fg = (r_fg, g_fg, b_fg)

        # Stop transition when complete
        if t >= 1:
            self.transition_active = False

        return self.current_bg, self.current_fg


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    confetti = Confetti()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font("freesansbold.ttf", 20)
    obstacles = []
    death_count = 0

    def score():
        global game_speed, points
        points += 1
        if points % 500 == 0:
            game_speed += 1
            confetti.create_confetti()
        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))

        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                death_count += 1
                menu(death_count)

        background()
        confetti.update_and_draw(SCREEN)  # Draw and update confetti
        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(30)
        pygame.display.update()


def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        font = pygame.font.Font("freesansbold.ttf", 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(START, (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()
            elif event.type == pygame.KEYDOWN:
                main()


menu(death_count=0)
