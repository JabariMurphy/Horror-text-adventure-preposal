import pygame

pygame.init()

startscreenbackground = pygame.image.load('menubackground.png')
screen = pygame.display.set_mode((600,400),0,0,0,0)
screen.blit(startscreenbackground,(0,0))
           
pygame.display.flip()
    
clock = pygame.time.Clock()

font = pygame.font.Font(None,size=35)
titlefont = pygame.font.Font(None,size=50)

def Tutorial():
    tutorial = """This game plays like a classic text adventure and will respond
          to basic commands such as look, check, and use. These are not
          all of the possible commands so get creative. Have Fun!"""


#def commands(command):
    #if command.lower() == 'tutorial':
        
def gamestart(screen):
    clock.tick_busy_loop(60)
    screen.fill('Black')
    ellipse = (pygame.draw.ellipse(screen,(0,0,139),(0,350,600,50),0))
    pygame.draw.rect(screen,(1,50,32),(300,0,100,200))
    pygame.display.flip()
    pygame.key.start_text_input()
    input_active = True
    user_text = ""
    input_color = (255,255,255)
    bg_color = 'Black'
    input_rect = pygame.Rect(50, 360, 500, 35)
    screen.fill(bg_color)
    pygame.draw.ellipse(screen,(0,0,139),(0,350,600,50),0)
    pygame.display.flip()

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    command = user_text
                    commands(command)
                    user_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        screen.fill(bg_color)
        pygame.draw.ellipse(screen,(0,0,139),(0,350,600,50),0)

        text_surface = font.render(user_text, True, input_color)
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        pygame.draw.rect(screen, input_color, input_rect, 2)
        pygame.display.flip()

    
        
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
