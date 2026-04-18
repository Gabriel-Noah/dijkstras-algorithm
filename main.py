import pygame
from sys import exit
import math
from collections import namedtuple

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

# Draws the weight centered at the middle of an edge between 2 points
def draw_weight(start, end, weight):
    text = font.render(f"{weight:.0f}", True, TEXT_COLOR, BG_COLOR)
    midpoint = get_midpoint(start, end)
    screen.blit(text, (midpoint[0] - text.get_width() / 2, midpoint[1] - text.get_height() / 2))

def draw_graph(graph):
    for index, node in enumerate(graph):
        for neighbor_index, weight in node.neighbors:
            # Checks that the line between them hasn't already been drawn
            if neighbor_index > index:
                draw_line(node.pos, graph[neighbor_index].pos)
                draw_weight(node.pos, graph[neighbor_index].pos, weight)
        draw_node(node.pos)

Node = namedtuple("Node", ["pos", "neighbors"])

# Stored as an adjacency list
graph = [
    Node((200, 250), [(1, 5), (2, 7)]),  # Node 0 Neighbors Node 1 with an edge weight of 5
    Node((300, 250), [(0, 5), (2, 6)]),
    Node((400, 150), [(0, 7), (1, 6)])
]

while True:
    # Event handling
    for event in pygame.event.get():
        # Quits if the window is closed or if the user presses escape or q
        if (event.type == pygame.QUIT
                or (event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_q))):
            pygame.quit()
            exit()

    screen.fill(BG_COLOR)
    draw_graph(graph)

    pygame.display.flip()
    clock.tick(60)
