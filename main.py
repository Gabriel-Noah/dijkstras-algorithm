import pygame
from sys import exit
import math
from collections import namedtuple
import random

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

def draw_graph(graph):
    for index, node in enumerate(graph):
        for neighbor_index, weight in node.neighbors:
            # Checks that the line between them hasn't already been drawn
            if neighbor_index > index:
                draw_line(node.pos, graph[neighbor_index].pos)
                draw_weight(node.pos, graph[neighbor_index].pos, weight)
        draw_node(node.pos)

# Generates a random weighted graph by randomly generating points then for each point adding an edge
# with the 2 closest points it doesn't already have an edge with. Weight is the distance between the points
def generate_graph(count, x_min, x_max, y_min, y_max):
    graph = []

    # Generates points
    for _ in range(count):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)
        graph.append(Node((x, y), []))

    for i, node in enumerate(graph):
        # Gets the 2 Closest nodes that aren't already connected to this node
        connected = [x[0] for x in node.neighbors]
        min_dist1 = min_dist2 = 10000
        min_node1 = min_node2 = 100

        for j, other in enumerate(graph):
            if j == i or j in connected:
                continue
            dist = distance(node.pos, other.pos)
            if dist < min_dist1:
                min_dist2 = min_dist1
                min_node2 = min_node1
                min_dist1 = dist
                min_node1 = j
            elif dist < min_dist2:
                min_dist2 = dist
                min_node2 = j

        # Adds an edge between the 2 closest nodes
        if min_node1 < count:
            node.neighbors.append((min_node1, min_dist1))
            graph[min_node1].neighbors.append((i, min_dist1))
        if min_node2 < count:
            node.neighbors.append((min_node2, min_dist2))
            graph[min_node2].neighbors.append((i, min_dist2))

    return graph

Node = namedtuple("Node", ["pos", "neighbors"])

# Stored as an adjacency list
graph = generate_graph(10, 10, 490, 10, 490)
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
                graph = generate_graph(10, 10, 490, 10, 490)

    screen.fill(BG_COLOR)
    draw_graph(graph)

    pygame.display.flip()
    clock.tick(60)
