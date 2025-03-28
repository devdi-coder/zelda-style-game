import os

WIDTH = 1280
HEIGHT = 720 
FPS = 60  
TILESIZE = 64

HITBOX_OFFSET = {
    'player': -26,
    'object': -40,
    'grass': -10,
    'invisible': 0,
}

BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UI_FONT = os.path.join(BASE_DIR, 'graphics', 'font', 'joystix.ttf')
UI_FONT_SIZE = 18

WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

HEALTH_COLOR = 'red'
ENERGY_COLOR = 'green'
UI_BORDER_COLOR_ACTIVE = 'white'

TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic': os.path.join(BASE_DIR, 'graphics', 'weapons', 'sword', 'full.png')},
    'axe': {'cooldown': 400, 'damage': 30, 'graphic': os.path.join(BASE_DIR, 'graphics', 'weapons', 'axe', 'full.png')},
    'rapier': {'cooldown': 300, 'damage': 20, 'graphic': os.path.join(BASE_DIR, 'graphics', 'weapons', 'rapier', 'full.png')},
    'sai': {'cooldown': 50, 'damage': 8, 'graphic': os.path.join(BASE_DIR, 'graphics', 'weapons', 'sai', 'full.png')},
    'lance': {'cooldown': 80, 'damage': 10, 'graphic': os.path.join(BASE_DIR, 'graphics', 'weapons', 'lance', 'full.png')},
}

magic_data = {
    'flame': {'strength': 5, 'cost': 20, 'graphic': os.path.join(BASE_DIR, 'graphics', 'particles', 'flame', 'fire.png')},
    'heal': {'strength': 20, 'cost': 10, 'graphic': os.path.join(BASE_DIR, 'graphics', 'particles', 'heal', 'heal.png')},
}

monster_data = {
    'squid': {'health': 100, 'exp': 100, 'damage': 20, 'attack_type': 'slash', 'attack_sound': os.path.join(BASE_DIR, 'audio', 'attack', 'slash.wav'), 'speed':2, 'resistance':3, 'attack_radius':80, 'notice_radius':360},
    'raccoon': {'health': 300, 'exp': 250, 'damage': 40, 'attack_type': 'claw', 'attack_sound': os.path.join(BASE_DIR, 'audio', 'attack', 'claw.wav'),'speed':1, 'resistance':2, 'attack_radius':100, 'notice_radius':400},
    'spirit': {'health': 100, 'exp': 110, 'damage': 8, 'attack_type': 'thunder', 'attack_sound': os.path.join(BASE_DIR, 'audio', 'attack', 'fireball.wav'),'speed':3, 'resistance':3, 'attack_radius':60, 'notice_radius':360},
    'bamboo': {'health': 70, 'exp': 120, 'damage': 6, 'attack_type': 'leaf_attack', 'attack_sound': os.path.join(BASE_DIR, 'audio', 'attack', 'slash.wav'), 'speed':2, 'resistance':3, 'attack_radius':55, 'notice_radius':350}
}