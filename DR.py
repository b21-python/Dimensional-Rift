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
    [(0,477),(230,477)],#BOTTOM LEFT
    [(480,477),(644,477)],#BOTTOM RIGHT #1 Y AND #2 X 
    [(640,477),(640,340)],#BOTTOM X RIGHT 
    [(0,360),(0,480)], #TOP Y WALL MIDDLE
    [(640,180),(640,0)],#1 X and #2 Y top RIGHT
    ]
                                                                




# player_pos is essentially:
# player_pos.x -> horizontal pos | player_.pos.y -> vertical pos
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
enemy_pos = pygame.Vector2(screen.get_width()/4, screen.get_height()/4)
enemy_hits_wall = False
player_firing = False
gun_pos = pygame.Vector2((screen.get_width()/2)+5, screen.get_height()/2)


while running:
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running=False


            
       # update player position based on keys pressed     
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 5
    if keys[pygame.K_s]:
        player_pos.y += 5 # player speed
    if keys[pygame.K_a]:
        player_pos.x -= 5
    if keys[pygame.K_d]:
        player_pos.x += 5
    if enemy_hits_wall == False:   
        if player_pos.x > enemy_pos.x:
            enemy_pos.x +=1
        if player_pos.x < enemy_pos.x:
            enemy_pos.x -=1
        if player_pos.y > enemy_pos.y:
            enemy_pos.y +=1
        if player_pos.y < enemy_pos.y:
            enemy_pos.y -=1
    mouse_pressed=pygame.mouse.get_pressed()
    if mouse_pressed[0]:
        print("firing")
        player_firing = True
   
    
    
    
    
    screen.fill('white')
    player_box = pygame.draw.circle(screen,"black",[player_pos.x,player_pos.y],10)
    gun_box = pygame.draw.circle(screen,"orange",[player_pos.x+5,player_pos.y],3)
    
    enemy_box = pygame.draw.rect(screen,"green" ,[enemy_pos.x,enemy_pos.y,30,30])
    
    if enemy_box.colliderect(player_box):
        GAME_OVER =True
        running = False
    if player_firing == True:
        pygame.draw.line(screen,"orange",[player_pos.x+5,player_pos.y],[player_pos.x+100,player_pos.y+100],10)
    
    
    
    
    for wall in walls:
        wall_box = pygame.draw.line(screen,"blue",wall[0],wall[1],8)
        if wall_box.colliderect(player_box):
            GAME_OVER =True
            running = False
        if wall_box.colliderect(enemy_box):
            enemy_hits_wall = True
            
            
      
    
    pygame.display.flip()
    clock.tick(60)
if GAME_OVER:
    screen.blit(text, textRect)
    print("wall_hit")
    pygame.display.flip()
else:
    pygame.quit()



