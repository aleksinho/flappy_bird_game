import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Acceleration and Deceleration")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Object properties
x, y = WIDTH // 2, HEIGHT // 2  # Start position in the center
width, height = 50, 50  # Dimensions of the object
velocity_x, velocity_y = 0, 0  # Initial velocity
acceleration = 0.5  # Rate of acceleration
max_speed = 10  # Maximum speed
friction = 0.1  # Rate of deceleration

# Main loop
running = True
while running:
    clock.tick(60)  # 60 FPS
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Acceleration logic
    if keys[pygame.K_LEFT]:
        velocity_x -= acceleration
    if keys[pygame.K_RIGHT]:
        velocity_x += acceleration
    if keys[pygame.K_UP]:
        velocity_y -= acceleration
    if keys[pygame.K_DOWN]:
        velocity_y += acceleration

    # Apply friction (deceleration)
    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        if velocity_x > 0:
            velocity_x -= friction
        if velocity_x < 0:
            velocity_x += friction

    if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
        if velocity_y > 0:
            velocity_y -= friction
        if velocity_y < 0:
            velocity_y += friction

    # Limit the maximum speed
    if velocity_x > max_speed:
        velocity_x = max_speed
    if velocity_x < -max_speed:
        velocity_x = -max_speed
    if velocity_y > max_speed:
        velocity_y = max_speed
    if velocity_y < -max_speed:
        velocity_y = -max_speed

    # Update position
    x += velocity_x
    y += velocity_y

    # Boundary conditions
    if x < 0:
        x = 0
        velocity_x = 0
    if x > WIDTH - width:
        x = WIDTH - width
        velocity_x = 0
    if y < 0:
        y = 0
        velocity_y = 0
    if y > HEIGHT - height:
        y = HEIGHT - height
        velocity_y = 0

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the object
    pygame.draw.rect(screen, RED, (x, y, width, height))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
