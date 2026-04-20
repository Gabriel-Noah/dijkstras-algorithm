import pygame
from sys import exit
import math
import random
import networkx as nx

# Pygame initalization
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Dijkstra's Algorithm")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 14)

# Constants
NODE_RADIUS = 5
NODE_COLOR = (0, 0, 255)    # Blue
EDGE_COLOR = (0, 0, 0)      # Black
EDGE_WIDTH = 3
TEXT_COLOR = (0, 0, 0)      # Black
BG_COLOR = (255, 255, 255)  # White

def get_midpoint(start, end):
    return ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)

def distance(start, end):
    return math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)

def draw_node(node):
    pygame.draw.circle(screen, NODE_COLOR, node, NODE_RADIUS)

def draw_line(start, end):
    pygame.draw.aaline(screen, EDGE_COLOR, start, end, EDGE_WIDTH)

# Draws the weight centered at the middle of an edge between 2 points
def draw_weight(start, end, weight):
    text = font.render(f"{weight}", True, TEXT_COLOR, BG_COLOR)
    midpoint = get_midpoint(start, end)
    screen.blit(text, (midpoint[0] - text.get_width() / 2, midpoint[1] - text.get_height() / 2))

def draw_graph(graph, layout):
    # Draws Edges, Then edge weights, then nodes
    for edge in graph.edges:
        p1 = layout[edge[0]]
        p2 = layout[edge[1]]
        draw_line(p1, p2)

    for edge in graph.edges:
        p1 = layout[edge[0]]
        p2 = layout[edge[1]]
        draw_weight(p1, p2, graph.edges[edge]["weight"])

    for node in layout:
        draw_node(layout[node])

def generate_weights(graph, min, max):
    for edge in graph.edges:
        rand = random.randint(min, max)
        graph.edges[edge]["weight"] = rand

def generate_graph(n, m, min_weight, max_weight):
    graph = nx.barabasi_albert_graph(n, m)
    generate_weights(graph, min_weight, max_weight)
    layout = nx.spring_layout(graph, center=[250, 250], scale=240, k=1)
    return graph, layout

# Randomly generates a graph
# Graph contains the nodes, edges, and edge weights. Layout contains the position of the nodes
graph, layout = generate_graph(10, 2, 1, 10)

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                pygame.quit()
                exit()
            if event.key == pygame.K_r:
                # Generates a new graph
                graph, layout = generate_graph(10, 2, 1, 10)

    screen.fill(BG_COLOR)
    draw_graph(graph, layout)

    pygame.display.flip()
    clock.tick(60)
