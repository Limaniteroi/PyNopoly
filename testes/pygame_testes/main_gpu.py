import pygame
import random
# The CORRECT import for the experimental video modules
from pygame._sdl2.video import Window, Renderer, Texture

# --- Constants ---
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
NUM_CIRCLES = 1000
CIRCLE_MAX_RADIUS = 30

# --- Pygame-CE Initialization ---
pygame.init()

# --- Create Window and Renderer ---
try:
    # We now create a Window and Renderer instance directly
    window = Window("Corrected Pygame-CE GPU Circles", size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    renderer = Renderer(window)
except Exception as e:
    print(f"Error creating window or renderer: {e}")
    pygame.quit()
    exit()

def create_circle_texture(renderer: Renderer, radius: int, color: tuple) -> Texture:
    """
    Creates a GPU texture of a circle.
    """
    diameter = radius * 2
    surface = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
    pygame.draw.circle(surface, color, (radius, radius), radius)
    
    # We now create a Texture instance directly
    texture = Texture.from_surface(renderer, surface)
    return texture

# Create one white circle texture to be tinted later
white_circle_texture = create_circle_texture(renderer, CIRCLE_MAX_RADIUS, (255, 255, 255, 255))

# --- Generate Circle Data ---
circles = []
for _ in range(NUM_CIRCLES):
    circles.append({
        'pos': pygame.Vector2(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)),
        'radius': random.randint(5, CIRCLE_MAX_RADIUS),
        'color': (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)),
        'velocity': pygame.Vector2(random.uniform(-2, 2), random.uniform(-2, 2))
    })

# --- Main Game Loop ---
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    for circle in circles:
        circle['pos'] += circle['velocity']
        if not (circle['radius'] < circle['pos'].x < SCREEN_WIDTH - circle['radius']):
            circle['velocity'].x *= -1
        if not (circle['radius'] < circle['pos'].y < SCREEN_HEIGHT - circle['radius']):
            circle['velocity'].y *= -1

    # --- Drawing with the GPU Renderer ---
    renderer.draw_color = (10, 20, 40, 255)
    renderer.clear()

    for circle in circles:
        white_circle_texture.color = circle['color']
        diameter = circle['radius'] * 2
        dest_rect = pygame.Rect(
            circle['pos'].x - circle['radius'],
            circle['pos'].y - circle['radius'],
            diameter,
            diameter
        )
        white_circle_texture.draw(dstrect=dest_rect)

    renderer.present()

    clock.tick()
    window.title = f"Pygame-CE _sdl2.video | {NUM_CIRCLES} GPU Circles | FPS: {clock.get_fps():.1f}"

pygame.quit()