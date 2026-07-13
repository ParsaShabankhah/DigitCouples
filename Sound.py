import pygame
import os

path = "Sounds"
sounds = os.listdir(path)
sound_paths = [os.path.join(path, sound) for sound in sounds]

class Sound:

    def __init__(self):
        self.click_menu_item = pygame.mixer.Sound(sound_paths[0])
        self.select_block_item = pygame.mixer.Sound(sound_paths[4])
        self.the_victory = pygame.mixer.Sound(sound_paths[5])
        self.game_is_over = pygame.mixer.Sound(sound_paths[2])
        self.the_main_item = pygame.mixer.Sound(sound_paths[3])
        self.is_wrong = pygame.mixer.Sound(sound_paths[6])
        self.is_correct = pygame.mixer.Sound(sound_paths[1])

    def click_menu(self):
        self.click_menu_item.play()

    def select_block(self):
        self.select_block_item.play()

    def victory(self):
        self.the_victory.play()

    def game_over(self):
        self.game_is_over.play()

    def main_item(self):
        self.the_main_item.play()

    def wrong(self):
        self.is_wrong.play()

    def correct(self):
        self.is_correct.play()