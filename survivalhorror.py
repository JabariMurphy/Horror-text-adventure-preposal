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
    print("""This game plays like a classic text adventure and will respond
          to basic commands such as look, check, and use. These are not
          all of the possible commands so get creative. Have Fun!""")


def gamestart():
    screen.fill('Black')
    pygame.draw.ellipse(screen,(0,0,139),(0,350,600,50),0)
    running = True
    while running:
        for ev in pygame.event.get():
            if ev.type == pygame.TEXTINPUT:
                inputtext = font.render(pygame.event.get(pygame.TEXTINPUT),True,white)
                screen.blit(inputtext,(50,375))
        
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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
                    gamestart()
    pygame.display.flip()
    
mainmenu()
