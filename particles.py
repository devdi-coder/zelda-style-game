# pyright: reportMissingImports=false
import pygame
import os
from support import import_folder
from random import choice

class AnimationPlayer:
    def __init__(self):
        import os

        base_path = os.path.join(os.path.dirname(__file__), 'graphics', 'particles')


        self.frames = {
            'flame': import_folder(os.path.join(base_path, 'flame','frames')),
            'aura': import_folder(os.path.join(base_path, 'aura')),
            'heal': import_folder(os.path.join(base_path, 'heal','frames')),

    # attacks
            'claw': import_folder(os.path.join(base_path, 'claw')),
            'slash': import_folder(os.path.join(base_path, 'slash')),
            'sparkle': import_folder(os.path.join(base_path, 'sparkle')),
            'leaf_attack': import_folder(os.path.join(base_path, 'leaf_attack')),
            'thunder': import_folder(os.path.join(base_path, 'thunder')),

    # monster deaths
            'squid': import_folder(os.path.join(base_path, 'smoke_orange')),
            'raccoon': import_folder(os.path.join(base_path, 'raccoon')),
            'spirit': import_folder(os.path.join(base_path, 'nova')),
            'bamboo': import_folder(os.path.join(base_path, 'bamboo')),

            'leaf': (
                import_folder(os.path.join(base_path, 'leaf1')),
                import_folder(os.path.join(base_path, 'leaf2')),
                import_folder(os.path.join(base_path, 'leaf3')),
                import_folder(os.path.join(base_path, 'leaf4')),
                import_folder(os.path.join(base_path, 'leaf5')),
                import_folder(os.path.join(base_path, 'leaf6')),

                self.reflect_images(import_folder(os.path.join(base_path, 'leaf1'))),
                self.reflect_images(import_folder(os.path.join(base_path, 'leaf2'))),
                self.reflect_images(import_folder(os.path.join(base_path, 'leaf3'))),
                self.reflect_images(import_folder(os.path.join(base_path, 'leaf4'))),
                self.reflect_images(import_folder(os.path.join(base_path, 'leaf5'))),
                self.reflect_images(import_folder(os.path.join(base_path, 'leaf6')))
                )
        }


    def reflect_images(self,frames):
        if not frames:
            print("No frames to reflect.")
            return []
        new_frames = []

        for frame in frames:
            flipped_frame = pygame.transform.flip(frame,True,False)
            new_frames.append(flipped_frame)
        return new_frames
    
    def create_grass_particles(self,pos,groups):
        animation_frames = choice(self.frames['leaf'])
        Particles(pos,animation_frames,groups)

    def create_particles(self,animation_type,pos,groups):
        animation_frames = self.frames[animation_type]
        Particles(pos,animation_frames,groups)

class Particles(pygame.sprite.Sprite):
    def __init__(self,pos,animation_frames,groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index] 
        self.rect = self.image.get_rect(center = pos)

        self.sprite_type = "magic"


    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    
    def update(self):
        self.animate()
