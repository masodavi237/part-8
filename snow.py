import random, pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snowflakes")
done = False

sf_list = []

# Populates lists with location, size and color
for i in range(120):
    x = random.randrange(0, 700)
    y = random.randrange(0, 500)
    sf_list.append([x, y])

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
    for j in range(len(sf_list)):
        pygame.draw.circle(screen, WHITE, sf_list[j], 2)
        sf_list[j][1] += 1

        if sf_list[j][1] > 500:
            y = random.randrange(-50, -10)
            sf_list[j][1] = y
            x = random.randrange(0, 700)
            sf_list[j][0] = x

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()