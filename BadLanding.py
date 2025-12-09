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
def commands(command,currentplace):
    clear_screen()
    
    command = command.lower()
    command.split()
    if command[0:10] == 'look ship' or command[0:10] == 'check ship':
        input_rect = pygame.Rect(50, 360, 500, 35)
        ship1 = font.render("The ship is toast and there's no sign of your",True,(255,255,255))
        ship2 = font.render("team not even a sign of struggle.",True,(255,255,255))
        ship3 = font.render("There is a bioscanner and a small unloaded",True,(255,255,255))
        ship4 = font.render("pistol in its holster attached to the pilots seat",True,(255,255,255))
        screen.blit(ship1,(50,360))
        pygame.display.flip()
        pygame.time.delay(3000)
        clear_screen()
        screen.blit(ship2,(50,360))
        pygame.display.flip()
        pygame.time.delay(3000)
        clear_screen()
        screen.blit(ship3,(50,360))
        pygame.display.flip()
        pygame.time.delay(3000)
        clear_screen()
        screen.blit(ship4,(50,360))
        pygame.display.flip()
        pygame.time.delay(3000)
        clear_screen()
       
    if command == 'take' or command == 'add to inventory':
        if currentplace == ship:
            take1 = font.render("bioscanner and empty pistol added to inventory",True,(255,255,255))
            screen.blit(take1,(50,360))
            pygame.display.flip()
            pygame.time.delay(3000)
        
def gamestart(screen):
    screen.fill('Black')
    input_color = (255,255,255)
    input_rect = pygame.Rect(50, 360, 500, 35)
    pygame.draw.ellipse(screen,(0,0,139),(0,350,600,50),0)
    pygame.draw.rect(screen,(1,50,32),(400,0,200,200),0)

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
    lines = [bline1, bline2, bline3, bline4, bline5, bline6, bline7, bline8, bline9]
    y = 0
    for line in lines:
        screen.blit(line, (400, y))
        y += 10
    pygame.display.flip()
    pygame.time.delay(10000)  

    # Begin input loop
    input_active = True
    user_text = ""
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                input_active = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    commands(user_text,currentplace)
                    user_text = ""  # Clear text after submitting
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    # Ensure only printable characters
                    if event.unicode.isprintable():
                        user_text += event.unicode

        # Redraw everything
        screen.fill('Black')
        pygame.draw.ellipse(screen,(0,0,139),(0,350,600,50),0)
        pygame.draw.rect(screen,(1,50,32),(400,0,200,200),0)
        text_surface = font.render(user_text, True, input_color)
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        pygame.draw.rect(screen, input_color, input_rect, 2)
        pygame.display.flip()

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
