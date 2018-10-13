from pygame import *#to import some files of pygame
import sys #to import the system
import pygame #to import the pygame

def menu_screen(Button,run_game):
    """make the screen for menu"""
    display.set_caption("Jet Mission") #to set the tittle
    screen = pygame.display.set_mode((800, 600)) #to set the screen resolution
    #object button for quit and start
    start_button = Button("New Piskel.png") #to add a button to start the game
    quit_button = Button("quit button.png") #to add a button to quit the game
    #image for the menu's backgound
    bg_image=pygame.image.load("asteroid_wall.jpg") #to add an image of the background
    bg_image=pygame.transform.scale(bg_image, (800, 600)) # to scale the image


    pygame.init()

    while True:
        rect_start= draw.rect(screen, (0, 0, 0), (250, 200, 300, 150)) #to set the rect when the game start
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150)) # to set the rect when the game ends
        screen.blit(bg_image,(0,0)) #to set background image scale

        screen.blit(start_button.button,(250,200)) #to set the start button scale
        screen.blit(quit_button.button,(250,300)) #to set the quit button scale

        ev=event.wait() #to wait until an event done

        if ev.type == MOUSEBUTTONDOWN:
            if rect_start.collidepoint(mouse.get_pos()): #if the mouse click start, run the game
                run_game()
            if rect_quit.collidepoint(mouse.get_pos()): #if the mouse click quit, quit the game
                sys.exit()

        if ev.type == QUIT: #if the mouse click quit, quit the game
            sys.exit()

        display.update()

def pause_menu(Button,run_game): #to set if the game is paused
    """pause_menu"""
    #make the screen display
    display.set_caption("Jet Mission") #to set a text Jet Mission if the game is paused
    screen = pygame.display.set_mode((800, 600)) #to set the scale of the text

    # object button for quit and start
    start_button = Button("quit button.png") #add a quit button
    return_button = Button("pause button.png") #add a return

    # image for the menu's backgound
    bg_image = pygame.image.load("asteroid_wall.jpg") #to set the background image
    bg_image = pygame.transform.scale(bg_image, (800, 600)) #to set the scale of the background


    pygame.init()
    paused=True #pause flag #do this if the pause statement is true
    while paused:
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150)) #to draw the rect size of star
        rect_return = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150)) #to draw the rect size of return
        screen.blit(bg_image, (0, 0)) #to set the background image blit

        screen.blit(start_button.button, (250, 200))
        screen.blit(return_button.button, (250, 300))

        ev = event.wait() #to wait the event

        if ev.type == MOUSEBUTTONDOWN: #if the event is mouse
            if rect_start.collidepoint(mouse.get_pos()): #if it click start
                menu_screen(Button,run_game)
            if rect_return.collidepoint(mouse.get_pos()): #if it click returtn
                paused = False #flag become  False

        if ev.type == QUIT:
            sys.exit()


        display.update()

def lose_menu(Button,run_game,score):
    """make the screen for menu"""
    display.set_caption("Jet Mission") #to desplay caption of Jet Mission
    screen = pygame.display.set_mode((800, 600)) #to set the scale
    font=pygame.font.SysFont("times new roman",100) #to set the font
    text=font.render("Replay?",True,(255,255,255)) #to set if continue or not
    score_text=font.render("score:"+str(score),True,(255,255,255)) #to do the scoring

    # object button for quit and start
    start_button = Button("New Piskel.png") #to add start button
    quit_button = Button("quit button.png") #to add the quit button

    # image for the menu's backgound
    bg_image = pygame.image.load("asteroid_wall.jpg") #to add an image
    bg_image = pygame.transform.scale(bg_image, (800, 600)) #to add scale of the background image

    pygame.init()

    while True:
        rect_start = draw.rect(screen, (0, 0, 0), (250, 200, 300, 150)) #to do the rect if the condition true
        rect_quit = draw.rect(screen, (0, 0, 0), (250, 300, 300, 150))
        screen.blit(bg_image, (0, 0)) #to set screen blit of background
        screen.blit(text,(200,10)) #to set screen blit of text
        screen.blit(start_button.button, (250, 200)) #to set screen blit the start butteon
        screen.blit(quit_button.button, (250, 300)) #to set the screen blit quit button
        screen.blit(score_text,(200,400)) #to set the screeen blit of score number

        ev = event.wait()

        if ev.type == MOUSEBUTTONDOWN: #to do the mouse event
            if rect_start.collidepoint(mouse.get_pos()): #if start, run game
                run_game()
            if rect_quit.collidepoint(mouse.get_pos()): #if quit, exit game
                sys.exit()

        if ev.type == QUIT:
            sys.exit()

        display.update() #to do the event
