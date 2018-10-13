from pygame import * #to import some of the pygame
import menu #to import the menu
import random #to import the random

from classes import * #to import classes




def run_game(): #if game is running do the this
    """game play interface"""
    screen = pygame.display.set_mode((800, 600)) #to set the scale
    display.set_caption("Jet mission") #to add the text Jet Mission


    scores = 0 #to set the scores 0
    theClock = pygame.time.Clock() #to add time
    bg_image = Star_bg("star.gif") #to add an image

    #coordinate of moving background
    x = 0
    y = 0
    x1 = bg_image.width
    y1 = 0

    pygame.init()


    #creating a jet
    jet1 = Jet(screen)
    Jet_sprites = Group(jet1)

    #create asteroid object group
    asteroid_group = Group()

    #create bullets object Group
    bullets = Group()



    Fps = 40 #to set the frame per second
    asteroid_timer = pygame.time.get_ticks() #to set the time ticking
    while True: #while condition true
        theClock.tick(Fps) #to set the fps of the clock
        Fps += 0.01#game phase goes faster after every frame

        """background move"""

        x -= 5 #to make the background move to the left by 5
        x1 -= 5
        bg_image.draw(screen,x,y) #to set the background movement
        bg_image.draw(screen,x1, y1)
        if x < -bg_image.width: #to set the background
            x = 0
        if x1 < 0:
            x1 = bg_image.width

        # create score board
        font=pygame.font.SysFont("Times New Romans",36) #to set the font
        score_board=font.render("score:"+str(scores),True,(255,255,255)) #to set the scores
        # update refered to the word's method
        screen.blit(score_board,(10,550)) #to set screen blit of the score board



        Jet_sprites.draw(screen) #to activate the jet

        bullets.draw(screen) #to acvtivate the bullets

        asteroid_group.draw(screen) #to activate the asteroid
        display.update()#update jet and screen view

        event.get()

        #to do the movement as the key pressed
        key = pygame.key.get_pressed()
        if key[K_LEFT] and jet1.rect.x>0:
            jet1.moveleft()

        if key[K_RIGHT] and jet1.rect.x<=700:
            jet1.moveright()

        if key[K_DOWN] and jet1.rect.y<=500:
            jet1.movedown()

        if key[K_UP] and jet1.rect.y>0:
            jet1.moveup()

        if key[K_SPACE] and len(bullets) <= jet1.firerates+(scores/4000): #to set space as shooting and add score if it hit the target
            bullet = Bullet(screen, jet1.rect.x+50, jet1.rect.y+42) #to set the bullet coordinate
            bullets.add(bullet) #to set the bullet
            pygame.mixer.music.load("LaserBlast.wav") #to set sound of bullet
            pygame.mixer.music.play() #to add soune

        if key[K_ESCAPE]:
            menu.menu_screen(Button,run_game) #to set esc as themenu screen

        if key[K_p]:
            menu.pause_menu(Button,run_game) #to set p as pause button

        if pygame.time.get_ticks() - asteroid_timer >= 200: #to add asteroid randomly as the time flows
            asteroid = Asteroid(screen, 50, 50, random.randint(1,4)*6, 800, (random.randint(1,28) * 20))
            asteroid_group.add(asteroid)
            asteroid_timer = pygame.time.get_ticks()

        for asteroid in asteroid_group:
            asteroid.movement() #to get the movement def
            if asteroid.rect.right <= 0: #to move the asteroid
                asteroid_group.remove(asteroid) #remove after screen
            if groupcollide(Jet_sprites,asteroid_group,dokilla=True,dokillb=True):#collition check
                menu.lose_menu(Button,run_game,scores) #if the asteroid hit then lose

        for bullet in bullets:
            bullet.movement() #to get bullet movement def
            if bullet.rect.left > 800: #if the bullet exceded the map than it gone
                bullets.remove(bullet)
            if groupcollide(bullets,asteroid_group,dokilla=True,dokillb=True):
                scores += 100 #if it hit then add 100 to point

menu.menu_screen(Button,run_game)

#---------------SPECIAL THANKS to Pier,Excel,georgius,William,Nicander,Nicolas,Andy,Guntur,Adrian-----------------------
"""Acknowledgement:
LaserBlast.wav(shooting sound) http://soundbible.com/472-Laser-Blasts.html
"""
