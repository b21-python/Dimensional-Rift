import pygame
pygame.init()
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
running = True

font = pygame.font.SysFont('free',32) 
text = font.render('GAME OVER', True,"red","black")
textRect = text.get_rect()


GAME_OVER = False

walls = [
    [(0,0), (230,0)], # X
    [(0,0), (0,180)],#Y TOP LEFT
    [(100, 100), (460, 100)], #TOP MIDDLE
    [(380,0), (640,0)],#TOP RIGHT 
    [(0,477),(230,477)]#BOTTTOM LEFT
#     [(100,477),
    ]
                                                                




# player_pos is essentially:
# player_pos.x -> horizontal pos | player_.pos.y -> vertical pos
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

while running:
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running=False


            
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
            
        

    
    screen.fill('white')
    player_box = pygame.draw.circle(screen,"black",[player_pos.x,player_pos.y],10)
        
    for wall in walls:
        wall_box = pygame.draw.line(screen,"blue",wall[0],wall[1],8)
        if wall_box.colliderect(player_box):
            GAME_OVER =True
            running = False
          
      
    
    pygame.display.flip()
    clock.tick(60)
if GAME_OVER:
    screen.blit(text, textRect)
    print("wall_hit")
    pygame.display.flip()
else:
    pygame.quit()



