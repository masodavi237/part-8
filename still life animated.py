import pygame
import math

PI = 3.141596

#   Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
DARK_GREEN = (0, 153, 0)
LIGHT_BLUE = (153, 204, 255)
PALE_GREEN = (102, 255, 102)
BRICK = (203, 65, 84)
MORTAR = (86, 80, 81)
OAK = (120, 81, 45)
DOOR = (0, 87, 174)
GLASS = (198, 226, 227)
NAVY = (0, 69, 138)
GREY = (240, 240, 255)
pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
indented = False
pygame.display.set_caption("My Game")

# Loop until the user clicks the close bton.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def draw_cloud(screen, x):
    pygame.draw.ellipse(screen, WHITE, [x , 60, 60, 30], 0)
    pygame.draw.ellipse(screen, WHITE, [x + 40, 60 + 15, 60, 30], 0)
    pygame.draw.ellipse(screen, GREY, [x + 50, 60 - 5, 60, 30], 0)


cloud_change_x = 2
cloud_x = 0

clouds = []
clouds.append(200)
clouds.append(550)
clouds.append(100)



# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(LIGHT_BLUE)

    # --- Drawing code should go here

    pygame.draw.circle(screen, YELLOW, [45, 45], 90, 90)

    for cloud in range(len(clouds)):
        draw_cloud(screen, clouds[cloud])

        clouds[cloud] = clouds[cloud] + cloud_change_x

        if clouds[cloud] >= 700:
            clouds[cloud] = -100

    # for i in range(len(clouds)):
    #     draw_cloud(screen, clouds[i][0])



    pygame.draw.rect(screen, PALE_GREEN, [0, 334, 700, 166])  # --- GRASS HORIZON
    pygame.draw.rect(screen, BRICK, [300, 90, 275, 300])  # --- BRICK

    # --- DRAW HORIZONTAL MORTAR
    for i in range(95, 390, 10):
        pygame.draw.rect(screen, MORTAR, [300, i, 275, 2])
        # --- DRAWS VERTICAL LINES
        for j in range(320, 570, 15):
            if not indented:
                pygame.draw.line(screen, MORTAR, [j, i - 10], [j, i])
                indented = True
            else:
                pygame.draw.line(screen, MORTAR, [j, i], [j, i])
                indented = False

    pygame.draw.polygon(screen, BLACK, [(280, 90), (595, 90), (438, 20)])

    pygame.draw.polygon(screen, WHITE, [(394, 280), (447, 247), (500, 280)])

    for i in range(404, 471, 66):
        pygame.draw.rect(screen, WHITE, [i, 280, 20, 110])

    pygame.draw.rect(screen, DOOR, [414, 300, 66, 90])
    pygame.draw.arc(screen, GLASS, [414, 301 - (66 / 2), 66, 66], 0, PI, 33)
    pygame.draw.arc(screen, WHITE, [414, 301 - (66 / 2), 66, 66], 0, PI, 5)
    pygame.draw.arc(screen, WHITE, [437, 290, 20, 20], 0, PI, 10)
    pygame.draw.arc(screen, BLACK, [414, 301 - (66 / 2), 66, 66], 0, PI, 3)
    pygame.draw.rect(screen, NAVY, [419, 305, 25, 15], 1)
    pygame.draw.rect(screen, NAVY, [447 + 3, 305, 25, 15], 1)
    pygame.draw.rect(screen, NAVY, [419, 323, 25, 30], 1)
    pygame.draw.rect(screen, NAVY, [419, 358, 25, 25], 1)
    pygame.draw.rect(screen, NAVY, [451, 323, 25, 30], 1)
    pygame.draw.rect(screen, NAVY, [451, 358, 25, 25], 1)
    pygame.draw.rect(screen, BLACK, [425, 347, 5, 2])






    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
