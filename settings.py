import os

WIDTH = 1280  
HEIGHT = 720  
FPS = 60  
TILESIZE = 64 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic': os.path.join(BASE_DIR, 'graphics', 'weapons', 'sword', 'full.png')},
    'axe': {'cooldown': 400, 'damage': 30, 'graphic': os.path.join(BASE_DIR, 'graphics', 'weapons', 'axe', 'full.png')},
    'rapier': {'cooldown': 300, 'damage': 20, 'graphic': os.path.join(BASE_DIR, 'graphics', 'weapons', 'rapier', 'full.png')},
    'sai': {'cooldown': 50, 'damage': 8, 'graphic': os.path.join(BASE_DIR, 'graphics', 'weapons', 'sai', 'full.png')},
    'lance': {'cooldown': 80, 'damage': 10, 'graphic': os.path.join(BASE_DIR, 'graphics', 'weapons', 'lance', 'full.png')},
}
