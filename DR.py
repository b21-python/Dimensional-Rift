import pygame
pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True

# player_pos is essentially:
# player_pos.x -> horizontal pos | player_.pos.y -> vertical pos
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
print(player_pos)
while running:
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
       # update player position based on keys pressed     
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 10
    if keys[pygame.K_s]:
        player_pos.y += 10
    if keys[pygame.K_a]:
        player_pos.x -= 10
    if keys[pygame.K_d]:
        player_pos.x += 10       

    


    screen.fill('orange')
    pygame.draw.line(screen, "blue", [0,0],(640,480),6)
    pygame.draw.circle(screen,"black",[player_pos.x,player_pos.y],10)
    pygame.draw.ellipse(screen, (0,200,255), (0,400,300,80))
    pygame.draw.arc(screen, (25,125,225), (0,0,400,100),0, 4)
    
    
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()



