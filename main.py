import pygame
from sys import exit
import math

# Pygame initalization
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Dijkstra's Algorithm")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)

# Constants
NODE_RADIUS = 5
NODE_COLOR = (0, 0, 255)    # Blue
EDGE_COLOR = (0, 0, 0)      # Black
EDGE_WIDTH = 3
TEXT_COLOR = (0, 0, 0)      # Black
BG_COLOR = (255, 255, 255)  # White

def draw_node(node):
    pygame.draw.circle(screen, NODE_COLOR, node, NODE_RADIUS)

def draw_line(start, end):
    pygame.draw.line(screen, EDGE_COLOR, start, end, EDGE_WIDTH)

def get_midpoint(start, end):
    return ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)

def distance(start, end):
    return math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)

# Draws the weight centered at the middle of an edge between 2 points
def draw_weight(start, end, weight):
    text = font.render(f"{weight:.0f}", True, TEXT_COLOR, BG_COLOR)
    midpoint = get_midpoint(start, end)
    screen.blit(text, (midpoint[0] - text.get_width() / 2, midpoint[1] - text.get_height() / 2))

node1 = (250, 250)
node2 = (250, 250)

while True:
    # Event handling
    for event in pygame.event.get():
        # Quits if the window is closed or if the user presses escape or q
        if (event.type == pygame.QUIT
                or (event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_q))):
            pygame.quit()
            exit()

    node2 = pygame.mouse.get_pos()

    screen.fill(BG_COLOR)
    draw_line(node1, node2)
    draw_node(node1)
    draw_node(node2)
    draw_weight(node1, node2, distance(node1, node2))

    pygame.display.flip()
    clock.tick(60)
