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

# Surfaces
ui_surf = pygame.Surface((screen.get_width(), screen.get_height() / 10))  # Banner that goes across the screen and takes 10% of the screen height
main_surf = pygame.Surface((screen.get_width(), screen.get_height() - ui_surf.get_height()))
ui_rect = ui_surf.get_rect()
main_rect = main_surf.get_rect().move(0, ui_surf.get_height())

# Constants
NODE_RADIUS = 5
NODE_COLOR = (0, 0, 255)              # Blue
NODE_HOVER_COLOR = (66, 255, 66)      # Green
EDGE_COLOR = (0, 0, 0)                # Black
EDGE_WIDTH = 3
FG_COLOR = (0, 0, 0)                  # Black
BG_COLOR = (255, 255, 255)            # White
BUTTON_HOVER_COLOR = (200, 200, 200)  # Gray
SELECT_RADIUS = NODE_RADIUS * 1.5

def get_midpoint(start, end):
    return ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)

def distance(start, end):
    return math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)

def draw_node(surf, node, color):
    pygame.draw.circle(surf, color, node, NODE_RADIUS)

def draw_line(surf, start, end):
    pygame.draw.aaline(surf, EDGE_COLOR, start, end, EDGE_WIDTH)

# Draws the weight centered at the middle of an edge between 2 points
def draw_weight(surf, start, end, weight):
    text = font.render(f"{weight}", True, FG_COLOR, BG_COLOR)
    midpoint = get_midpoint(start, end)
    surf.blit(text, (midpoint[0] - text.get_width() / 2, midpoint[1] - text.get_height() / 2))

def draw_graph(graph, layout):
    main_surf.fill(BG_COLOR)
    # Draws Edges, Then edge weights, then nodes
    for edge in graph.edges:
        p1 = layout[edge[0]]
        p2 = layout[edge[1]]
        draw_line(main_surf, p1, p2)

    for edge in graph.edges:
        p1 = layout[edge[0]]
        p2 = layout[edge[1]]
        draw_weight(main_surf, p1, p2, graph.edges[edge]["weight"])

    for node in layout:
        if "hovered" in graph.nodes[node] and graph.nodes[node]["hovered"]:
            draw_node(main_surf, layout[node], NODE_HOVER_COLOR)
        else:
            draw_node(main_surf, layout[node], NODE_COLOR)

# UI Buttons
regen_button = pygame.Rect(0, 0, 150, 25)
regen_button.midright = (ui_surf.get_width() - 10, ui_surf.get_height() / 2)
restart_button = pygame.Rect(0, 0, 150, 25)
restart_button.midright = (regen_button.left - 10, ui_surf.get_height() / 2)
hovered_button = None

def draw_ui(state):
    ui_surf.fill(FG_COLOR)

    if state == 1:
        instructions = "Select Starting Point"
    elif state == 2:
        instructions = "Select Ending Point"
    elif state == 3:
        instructions = "Running Algorithm"
    else:
        instructions = "Algorithm Finished"

    # Background and Foreground are flipped because the colors in the ui are inverted
    text = font.render(instructions, True, BG_COLOR, FG_COLOR)
    ui_surf.blit(text, (10, (ui_surf.get_height() - text.get_height()) / 2))

    pygame.draw.rect(ui_surf, BG_COLOR, regen_button)
    pygame.draw.rect(ui_surf, BG_COLOR, restart_button)

    # If either button is hovered then draws over them with a tinted version
    if hovered_button == "regen":
        pygame.draw.rect(ui_surf, BUTTON_HOVER_COLOR, regen_button)
    elif hovered_button == "restart":
        pygame.draw.rect(ui_surf, BUTTON_HOVER_COLOR, restart_button)

    regen_text = font.render("Ṟegenerate Graph", True, FG_COLOR)  # R is underlined to show shortcut
    restart_text = font.render("Restart Algorithm", True, FG_COLOR)

    # Draws text centered in each button
    ui_surf.blit(regen_text,
                 (regen_button.centerx - regen_text.get_width() / 2,
                  regen_button.centery - regen_text.get_height() / 2))
    ui_surf.blit(restart_text,
                 (restart_button.centerx - restart_text.get_width() / 2,
                  restart_button.centery - restart_text.get_height() / 2))

def generate_weights(graph, min, max):
    for edge in graph.edges:
        rand = random.randint(min, max)
        graph.edges[edge]["weight"] = rand

def generate_graph(n, m, min_weight, max_weight):
    graph = nx.barabasi_albert_graph(n, m)
    generate_weights(graph, min_weight, max_weight)

    c = [main_surf.get_width() / 2, main_surf.get_height() / 2]
    s = main_surf.get_height() / 2 - 10
    layout = nx.spring_layout(graph, center=c, scale=s, k=1)
    return graph, layout

# Handles mouse for the main screen
def update_main(pos, click):
    global state, start, end

    # Doesn't need to update anything if the algorithm is running
    if state > 2:
        return

    # Gets mouse position relative to the main screen
    pos = (pos[0] - main_rect.left, pos[1] - main_rect.top)
    for node in layout:
        # Checks if node is being hovered over
        if distance(layout[node], pos) < SELECT_RADIUS:
            if click:
                if state == 1:
                    start = node
                elif state == 2:
                    end = node
                state += 1
                # We don't want clicked nodes to be hovered
                graph.nodes[node]["hovered"] = False
            else:
                graph.nodes[node]["hovered"] = True
        else:
            graph.nodes[node]["hovered"] = False

# Handles mouse for the ui screen
def update_ui(pos, click):
    global hovered_button, graph, layout, state, start, end

    # Gets mouse position relative to the ui screen
    pos = (pos[0] - ui_rect.left, pos[1] - ui_rect.top)
    if regen_button.collidepoint(pos):
        hovered_button = "regen"
        if click:
            graph, layout = generate_graph(10, 2, 1, 10)
            state = 1
            start = end = None
    elif restart_button.collidepoint(pos):
        hovered_button = "restart"
        if click:
            state = 1
            start = end = None
    else:
        hovered_button = None

def update_mouse():
    pos = pygame.mouse.get_pos()
    # Checks if the left mouse button was just pressed this frame
    click = pygame.mouse.get_just_pressed()[0]

    # Checks which screen the mouse is in
    if main_rect.collidepoint(pos):
        update_main(pos, click)
    elif ui_rect.collidepoint(pos):
        update_ui(pos, click)

# Randomly generates a graph
# Graph contains the nodes, edges, and edge weights. Layout contains the position of the nodes
graph, layout = generate_graph(10, 2, 1, 10)

# Tracks the state the program is in, 1: User needs to pick first point, 2: User needs to pick second point, 3: Algorithm is running, 4: Algorithm Finished
state = 1
start = end = None

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
                state = 1
                start = end = None

    update_mouse()

    draw_graph(graph, layout)
    draw_ui(state)

    screen.blit(ui_surf, ui_rect)
    screen.blit(main_surf, main_rect)

    pygame.display.flip()
    clock.tick(60)
