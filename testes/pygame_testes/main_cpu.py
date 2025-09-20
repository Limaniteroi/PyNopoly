import pygame
import random

# --- Constants ---
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
NUM_CIRCLES = 1000
CIRCLE_MAX_RADIUS = 30

# --- Pygame-CE Initialization ---
pygame.init()

# --- Create Window ---
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame-CE CPU Circles")

def create_circle_surface(radius: int, color: tuple) -> pygame.Surface:
    """
    Creates a surface with a circle.
    """
    diameter = radius * 2
    surface = pygame.Surface((diameter, diameter), pygame.SRCALPHA)
    pygame.draw.circle(surface, color, (radius, radius), radius)
    return surface

# Create one white circle surface to be tinted later
white_circle_surface = create_circle_surface(CIRCLE_MAX_RADIUS, (255, 255, 255))

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

    # --- Drawing with the CPU ---
    screen.fill((10, 20, 40))

    for circle in circles:
        diameter = circle['radius'] * 2
        # Create a new surface for each circle to tint it
        temp_surface = white_circle_surface.copy()
        temp_surface.fill(circle['color'], special_flags=pygame.BLEND_RGB_MULT)
        
        # Scale the surface to the circle's radius
        scaled_surface = pygame.transform.smoothscale(temp_surface, (diameter, diameter))

        dest_rect = scaled_surface.get_rect(center=circle['pos'])
        screen.blit(scaled_surface, dest_rect)

    pygame.display.flip()

    clock.tick()
    pygame.display.set_caption(f"Pygame-CE CPU | {NUM_CIRCLES} CPU Circles | FPS: {clock.get_fps():.1f}")

pygame.quit()