import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
black = (0, 0, 0)
done = True
x = 200
y = 150
while done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        done = False
                pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            if x < 350:
                x += 20
        if pressed[pygame.K_LEFT]:
            if x > 50:
                x -= 20
        if pressed[pygame.K_UP]:
            if y > 50:
                y -= 20
        if pressed[pygame.K_DOWN]:
            if y < 250:
                y += 20
        screen.fill(black)
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
        pygame.display.flip()

        pygame.time.Clock().tick(60)