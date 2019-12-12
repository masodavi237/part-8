import pygame, random

# Define some colors, you may want to add more
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
pygame.init()
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
# Loop until the user clicks the close button.
done = False

# Stored the location of each snowflake
snow_list = []

# Populates lists with location, soze and color
for i in range(100):
    x = random.randrange(0, 700)
    y = random.randrange(0, 500)
    snow_list.append([x, y])

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop

    # --- All events are detected here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here
    #  Here, we clear the screen to white.
    screen.fill(BLACK)

    for i in range(len(snow_list)):
        # Draw the snow flake
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        # Move the snow flake down by one pixel
        snow_list[i][1] += 1

        # detects when a flake leaves the bottom of the window
        if snow_list[i][1] > 500:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 700)
            snow_list[i][0] = x

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()