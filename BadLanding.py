import pygame

pygame.init()

startscreenbackground = pygame.image.load('menubackground.png')
screen = pygame.display.set_mode((600,400),0,0,0,0)
screen.blit(startscreenbackground,(0,0))
           
pygame.display.flip()
    
clock = pygame.time.Clock()

font = pygame.font.Font(None,size=35)
litolfont = pygame.font.Font(None, size=20)
titlefont = pygame.font.Font(None,size=50)
#places
ship = "The ship is toast and there's no sign of your team not even a sign of struggle. There is a bioscanner and a small unloaded pistol in its holster attached to the pilots seat"
woodsleft = "The forest has a slight humm it appears to be living in more and different ways than you can comprehend"
print("This game plays like a classic text adventure and will respond to basic commands such as check, and use. These are not all of the possible commands so get creative. Have Fun!")

replacementrect = (50,360,500,35)
def clear_screen():
    screen.fill('Black')
    pygame.display.flip()
    input_color = (255,255,255)
    input_rect = pygame.Rect(50, 360, 500, 35)
    text_surface = font.render('', True, input_color)
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    pygame.draw.ellipse(screen,(0,0,139),(0,350,600,50),0)
    pygame.draw.rect(screen,(1,50,32),(400,0,200,200),0)
    pygame.display.flip()
def commands(command):
    clearscreen()
    
    command = command.lower()
    command.split()
    if command[0:10] == 'look ship' or command[0:10] == 'check ship':
        input_rect = pygame.Rect(50, 360, 500, 35)
        ship1 = font.render("The ship is toast and there's no sign of your team not even a sign of struggle.",True,(255,255,255))
        ship2 = font.render("There is a bioscanner and a small unloaded pistol in its holster attached to the pilots seat",True,(255,255,255))
        screen.blit(ship1,(50,360))
        pygame.display.flip()
        pygame.time.delay(3000)
        ship1.fill(color(0,0,0,0))
        screen.blit(ship2,(50,360))
        pygame.display.flip()
        pygame.time.delay(3000)
        ship2.fill(color(0,0,0,0))
        gamestart(screen)
        return user_text
def gamestart(screen):
    screen.fill('Black')
    pygame.display.flip()
    pygame.key.start_text_input()
    input_active = True
    user_text = ""
    input_color = (255,255,255)
    input_rect = pygame.Rect(50, 360, 500, 35)
    pygame.draw.ellipse(screen,(0,0,139),(0,350,600,50),0)
    pygame.draw.rect(screen,(1,50,32),(400,0,200,200),0)
    pygame.display.flip()
    currentplace = ship
    bline1 = litolfont.render("Message from Admiral Kent:",True,(255,255,255))
    bline2 = litolfont.render("Today marks the beginning",True,(255,255,255))
    bline3 = litolfont.render("of a new dawn of the human ",True,(255,255,255))
    bline4 = litolfont.render("empire.The United Navy has",True,(255,255,255))
    bline5 = litolfont.render("discovered a new habitable",True,(255,255,255))
    bline6 = litolfont.render("planet and your team will",True,(255,255,255))
    bline7 = litolfont.render("be the first to touchdown.",True,(255,255,255))
    bline8 = litolfont.render("The main objective is recon",True,(255,255,255))
    bline9 = litolfont.render("Good Luck marine!",True,(255,255,255))
    screen.blit(bline1,(400,0))
    pygame.display.flip()
    screen.blit(bline2,(400,10))
    pygame.display.flip()
    screen.blit(bline3,(400,20))
    pygame.display.flip()
    screen.blit(bline4,(400,30))
    pygame.display.flip()
    screen.blit(bline5,(400,40))
    pygame.display.flip()
    screen.blit(bline6,(400,50))
    pygame.display.flip()
    screen.blit(bline7,(400,60))
    pygame.display.flip()
    screen.blit(bline8,(400,70))
    pygame.display.flip()
    screen.blit(bline9,(400,80))
    pygame.display.flip()
    pygame.time.delay(10000)
    pygame.draw.rect(screen,(1,50,32),(400,0,200,200),0)
    
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    command = user_text
                    user_text = ""
                    commands(command)
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

       
        pygame.draw.ellipse(screen,(0,0,139),(0,350,600,50),0)

        text_surface = font.render(user_text, True, input_color)
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        pygame.draw.rect(screen, input_color, input_rect, 2)
    
    return currentplace

    
        
def mainmenu():
    startscreenbackground = pygame.image.load('menubackground.png')
    screen = pygame.display.set_mode((600,400),0,0,0,0)
    screen.blit(startscreenbackground,(0,0))
    white = (255,255,255)
    startbutton = pygame.draw.rect(screen,'Green',(225,150,150,50),0)
    fullscrnbutton = pygame.draw.rect(screen,'Green',(225,225,150,50),0)
    quitbutton = pygame.draw.rect(screen,'Green',(225,300,150,50),0)

    
    quittext = font.render('Quit',True,white)
    starttext = font.render('Start',True,white)
    fullscrntext = font.render('Fullscreen',True,white)
    Title = titlefont.render('Bad Landing',True,'Green')
    pygame.mouse.set_visible(True)
    screen.blit(starttext,(275,150))
    screen.blit(fullscrntext,(225,225))
    screen.blit(quittext,(275,300))
    screen.blit(Title,(200,100))
    pygame.display.flip()
    pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_CROSSHAIR))
    menu = True
    while menu:
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                if 225 <= mousepos[0] <= 375 and 150 <= mousepos[1] <= 200:
                    gamestart(screen)
    pygame.display.flip()
    
mainmenu()
