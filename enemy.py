# pyright: reportMissingImports=false
import pygame
import os
from support import *
from entity import Entity
from settings import *
from player import *

class Enemy(Entity):
    def __init__(self, monster_name, pos, groups,obstacle_sprites,
                  dmg_player,trigger_death_particles,xp):
        super().__init__(groups)
        self.sprite_type = 'enemy'

        self.import_graphics(monster_name)
        self.status = 'idle'
        self.image = self.animations[self.status][self.frame_index]

        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-10)
        self.obstacle_sprites = obstacle_sprites

        self.monster_name = monster_name
        monster_info = monster_data[self.monster_name]

        self.health = monster_info['health']
        self.exp = monster_info['exp']
        self.speed = monster_info['speed']
        self.attack_damage = monster_info['damage']
        self.resistance = monster_info['resistance']
        self.attack_radius = monster_info['attack_radius']
        self.notice_radius = monster_info['notice_radius']
        self.attack_type = monster_info['attack_type']

        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = 400
        self.dmg_player = dmg_player
        self.trigger_death_particles = trigger_death_particles
        self.xp = xp

        self.vulnerable = True
        self.hit_time = None
        self.invincibility_duration = 300

        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.death_sound = pygame.mixer.Sound(os.path.join(base_dir, 'audio', 'death.wav'))
        self.hit_sound = pygame.mixer.Sound(os.path.join(base_dir, 'audio', 'hit.wav'))
        self.attack_sound = pygame.mixer.Sound(monster_info['attack_sound'])
        self.death_sound.set_volume(0.2)
        self.hit_sound.set_volume(0.2)
        self.attack_sound.set_volume(0.2)
 
    def import_graphics(self, name):
        self.animations = {
            'idle': [], 'move': [], 'attack': [],
        }
        main_path = os.path.join(os.path.dirname(__file__), 'graphics', 'monsters', name)
        
        if os.path.exists(main_path):
            for animation in self.animations.keys():
                animation_path = os.path.join(main_path, animation)
                self.animations[animation] = import_folder(animation_path)

    def player_distance_direction(self,player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance =  (player_vec - enemy_vec).magnitude()

        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()


        return (distance,direction)

    def get_status(self,player):
        distance = self.player_distance_direction(player)[0]

        if distance <= self.attack_radius and self.can_attack:
            if self.status != 'attack':
                self.frame_index = 0
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    def actions(self,player):
        if self.status == 'attack':
            self.attack_time = pygame.time.get_ticks()
            self.dmg_player(self.attack_damage,self.attack_type)
            self.attack_sound.play()
        elif self.status == 'move':
            self.direction = self.player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            if self.status == 'attack':
                self.can_attack = False
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)

        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        
        else:
            self.image.set_alpha(255)

    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if not self.can_attack:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

        if not self.vulnerable:
            if current_time - self.hit_time >= self.invincibility_duration:
                self.vulnerable = True
            
    def get_damage(self,player,attack_type):
        if self.vulnerable:
            self.hit_sound.play()
            self.direction = self.player_distance_direction(player)[1]
            if attack_type == 'weapon':
                self.health -= player.get_full_magic_dmg()
            else:
                self.health -= player.get_full_magic_dmg()
        self.hit_time = pygame.time.get_ticks()
        self.vulnerable = False

    def check_death(self):
        if self.health <= 0:
            self.kill()
            self.trigger_death_particles(self.rect.center,self.monster_name)
            self.xp(self.exp)
            self.death_sound.play()

    def hit_reaction(self):
        if not self.vulnerable:
            self.direction *= -self.resistance

    def update(self):
        self.hit_reaction()
        self.move(self.speed)
        self.animate()
        self.cooldown()
        self.check_death()

    def enemy_update(self,player):
        self.get_status(player)
        self.actions(player)

def import_folder(path):
    surface_list = []
    if os.path.exists(path):
        for filename in os.listdir(path):
            full_path = os.path.join(path, filename)
            if filename.endswith('.png') or filename.endswith('.jpg'):
                try:
                    img = pygame.image.load(full_path).convert_alpha()
                    surface_list.append(img)
                except Exception:
                    pass 
    return surface_list
