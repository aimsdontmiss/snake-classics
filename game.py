import pygame; 
import random;


pygame.init()

# Create the screen
WIDTH, HEIGHT = 480, 480;
GRID_SIZE = 20;
GRID_WIDTH, GRID_HEIGHT = WIDTH / GRID_SIZE, HEIGHT / GRID_SIZE;

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32);

pygame.display.set_caption("snake")


'''            <----------------------- CONSTANTS ----------------------->            ''' 


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
GREY_1 = (128, 128, 128)
GREY_2 = (170, 170, 170)
RED = (200, 0, 0)

FPS = 60

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


'''            <----------------------- CLASSES ----------------------->            ''' 


# Snake class
class Snake:
    def __init__(self):
        self.color = GREEN
        self.length = 1
        self.position = [(int(WIDTH / 2), int(HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def head_position(self):
        return self.position[0]
    
    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def reset(self):
        self.length = 1
        self.position = [(int(WIDTH / 2), int(HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def move(self):
        current = self.head_position()
        x, y = self.direction
        new = (((current[0] + (x * GRID_SIZE)) % WIDTH), ((current[1] + (y * GRID_SIZE)) % HEIGHT))
        if len(self.position) > 2 and new in self.position[2:]:
            self.reset()
        else:
            self.position.insert(0, new)
            if len(self.position) > self.length:
                self.position.pop()

    def draw(self, surface):
        for p in self.position:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, BLACK, r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)

                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
        
        self.move()
        self.draw(screen)
        pygame.display.update()


# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

    def draw(self, screen):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.color, r)
        pygame.draw.rect(screen, BLACK, r, 1)


                

'''            <----------------------- GAME FUNCTIONS ----------------------->            ''' 

# Draw grid
def draw_grid(screen):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if ((x + y) % 2) == 0:
                white = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(screen, GREY_1, white)
            else:
                black = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(screen, GREY_2, black)


'''            <----------------------- GAME ----------------------->            ''' 


# Main loop
def main():
    run = True
    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()

    draw_grid(screen)


    while run:
        # Start game
        clock.tick(10)
        draw_grid(screen)
        snake.draw(screen)
        food.draw(screen)

        pygame.display.update()

        # Handle keys
        snake.handle_keys()

        # Check for snake collision with food   
        if snake.head_position() == food.position:
            snake.length += 1
            food.randomize_position()

        pygame.display.update()



main();