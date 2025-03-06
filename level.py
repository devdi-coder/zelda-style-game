import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
import csv
from pathlib import Path
from random import choice
from weapon import Weapon
from ui import UI



class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.current_attack = None

        self.create_map()

        self.ui = UI()

    def create_map(self):
        def load_csv(file_path):
            with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
                return [row for row in csv.reader(csvfile)]

        base_path = 'E:/piton/zelda-style/graphics/map/'  
        layouts = {
            'boundary': load_csv(base_path + 'map_floorBlocks.csv'),
            'grass': load_csv(base_path + 'map_Grass.csv'),
            'object': load_csv(base_path + 'map_LargeObjects.csv')
        }


        grass_path = os.path.join(os.path.dirname(__file__), 'graphics', 'Grass')
        large_objects_path = os.path.join(os.path.dirname(__file__), 'graphics', 'Objects')


        graphics = {
            'grass': import_folder(grass_path),
            'objects': import_folder(large_objects_path)
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':  
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE

                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')
                        if style == 'grass':
                            random_grass_image = choice(graphics['grass'])
                            Tile((x,y),[self.visible_sprites, self.obstacle_sprites], 'grass', random_grass_image)

                        if style == 'object':
                            surf = graphics['objects'][int(col)]
                            Tile((x,y),[self.visible_sprites, self.obstacle_sprites], 'object',surf)
                                
                    
        self.player = Player(
            (1200, 1200), [self.visible_sprites], self.obstacle_sprites,
              self.create_attack, self.destroy_attack,self.create_magic
              )

    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites]) 

    def create_magic(self,style, strength,cost):
        ...

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def run(self):
        
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.ui.display(self.player)

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_surf = pygame.image.load('graphics/sprites/floor.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft= (0,0))

    def custom_draw(self, player):
        
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)

        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)