import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Deal or No Deal")

# Create a class for the briefcases
class Briefcase:
    def __init__(self, value):
        self.value = value
        self.is_open = False


# Create a list of briefcases with random values
briefcases = []
for i in range(1, 27):
    value = random.choice([1, 10, 100, 1000, 10000, 100000, 500000, 1000000])
    briefcases.append(Briefcase(value))

# Create a function to draw the briefcases on the screen
def draw_briefcases(player_choice):
    screen.fill((255, 255, 255))
    for i, briefcase in enumerate(briefcases):
        if briefcase.is_open:
            color = (100, 100, 100)
        elif i + 1 == player_choice:
            color = (0, 0, 255)
        else:
            color = (255, 255, 255)

        rect = pygame.Rect(50 + (i % 13) * 50, 50 + (i // 13) * 50, 40, 40)
        pygame.draw.rect(screen, color, rect)
        font = pygame.font.SysFont(None, 24)
        text = font.render(str(briefcase.value), True, (0, 0, 0))
        screen.blit(text, rect.topleft)

# Create a function to handle the player's choice of briefcase
def choose_briefcase():
    mouse_pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        for i, briefcase in enumerate(briefcases):
            rect = pygame.Rect(50 + (i % 13) * 50, 50 + (i // 13) * 50, 40, 40)
            if rect.collidepoint(mouse_pos):
                briefcase.is_open = True
                return i + 1
    return None

# Set up the game loop
clock = pygame.time.Clock()
player_choice = None
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Draw the briefcases
    draw_briefcases(player_choice)
    pygame.display.flip()

    # Handle the player's choice of briefcase
    if player_choice is None:
        player_choice = choose_briefcase()

    # Wait for a short time to make the game feel more natural
    pygame.time.wait(50)

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
