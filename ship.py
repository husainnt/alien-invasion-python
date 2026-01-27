import pygame
class Ship:
    '''A class to manage the ship'''
    def __init__(self,ai_game):
        '''initialising the ship and setting its starting position'''
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()

        # start each new ship at bottom center of the screen
        self.rect.midbottom=self.screen_rect.midbottom

        def blitime(self):
            '''Draw the ship and its current loc'''
            self.screen.blit(self.image,self.rect)
            