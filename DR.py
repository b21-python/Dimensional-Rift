import pygame
pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True




while running:
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    


    screen.fill('orange')
    pygame.draw.line(screen, "blue", [0,0],(640,480),6)

    pygame.draw.rect(screen, "pink", (20,40,25,100))
    pygame.draw.circle(screen, 'purple', [200,200],60)
    pygame.draw.ellipse(screen, (0,200,255), (0,400,300,80))
    pygame.draw.arc(screen, (25,125,225), (0,0,400,100),0, 4)
    
    
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()



