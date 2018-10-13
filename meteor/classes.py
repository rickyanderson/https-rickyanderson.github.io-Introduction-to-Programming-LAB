#Ricky Anderson Ricco
#Commenting the program
from pygame import * #to import some files of pygame
from pygame.sprite import * #to import some files of pygame

class Jet(Sprite): #define Jet as a class
    """initialize the jet"""

    def __init__(self, screen): #to get the things that needed in the class
        Sprite.__init__(self)
        """initialize the Jet"""
        self.image = image.load("battlejet.png") #to set the image as what we want in this case use the (battlejet.png)
        self.image = pygame.transform.scale(self.image, (90, 50)) #to customize the image size
        self.rect = self.image.get_rect() #to set the place
        self.rect.x = 10 #to set the coordinate
        self.rect.y = 50 #to set the coordinate
        self.screen = screen #to set the screen
        self.move_speed = 6 #to move the screen
        """bullet"""
        self.firerates = 2 #to move the bullet

    def moveleft(self):
        self.rect.x -= self.move_speed #to move the ship by the movement of the keyboard inthis case move left by 1 which use minus to decrease the coordinate
        display.flip()

    def moveright(self):
        self.rect.x += self.move_speed #to move the ship by the movement of the keyboard in this case move right by 1 which use plu to add the coordinate
        display.flip()

    def moveup(self):
        self.rect.y -= self.move_speed
        display.flip()

    def movedown(self):
        self.rect.y += self.move_speed
        display.flip()





class Star_bg:
    #resourse of the backgound setting
    def __init__(self,background):
        self.background=image.load(background) #to set the background image
        self.background=pygame.transform.scale(self.background,(800,600)) #to set the scale of the background
        self.background_size=self.background.get_size() #to apply the size
        self.background_rect=self.background.get_rect() #to get the background
        self.width,self.height=self.background_size #to set the background height and width
    def draw(self,screen,x,y):
        screen.blit(self.background,(x,y)) #to use the background size

class Bullet(Sprite):
    def __init__(self,screen, startx, starty):
        Sprite. __init__(self)
        self.startx = startx #to set the bullets right in the middle of the ship
        self.starty = starty #to set the bullets right in the middle of the ship

        self.speedx = 20 #to set the speed of the bullet

        self.image = pygame.image.load("bullets.png") #to set the image of the bullet
        self.image = pygame.transform.scale(self.image,(40,40)) #to set the size of the bullet
        self.rect=self.image.get_rect() #to set the image
        self.rect.left = startx
        self.rect.top = starty
        self.rect.center = (startx,starty)
        self.screen = screen 3to set the screen
    def movement(self):
        self.screen.blit(self.image,[self.startx,self.starty]) #to use the bullet so start in the ship
        self.rect.left += self.speedx #to move the bullet to the right

class Asteroid(Sprite):
    """initialize the Asteroid"""
    def __init__(self, screen, width, height, speedx, startx, starty):
        Sprite.__init__(self)
        self.startx = startx #to set the asteroid
        self.starty = starty

        self.speedx = speedx #to set the movement speed of the asteroid

        self.image = pygame.image.load("meteor.png") #to set the image of the asteroid
        self.image = pygame.transform.scale(self.image, (width, height)) #to set the image scale of the asteroid
        self.rect = self.image.get_rect() #to set the image rect of the asteroid
        self.rect.left = startx #to set the rect start of the asteroid
        self.rect.top = starty
        self.screen = screen #to set the screen

    def movement(self):
        """method to move the Asteoid"""
        self.rect.left -= self.speedx #to move the asteroid to the left


class Button(Sprite):
    """initialize the button"""
    def __init__(self,image):
        Sprite. __init__(self)
        self.button=pygame.image.load(image)
        self.button=pygame.transform.scale(self.button,(300,150))
