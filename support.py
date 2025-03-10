# pyright: reportMissingImports=false
import os
from os import walk
from csv import reader
import pygame


def import_csv_layout(path):
    if not os.path.exists(path):
        print(f"Erro: O arquivo '{path}' não foi encontrado!")
        return
    terrain_map = []
    with open(path, newline='', encoding='utf-8') as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map
    
def import_folder(path):
    surface_list = []

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = os.path.join(path, image)
            try:
                image_surf = pygame.image.load(full_path).convert_alpha()
                surface_list.append(image_surf)
            except Exception as e:
                print(f"Erro ao carregar {full_path}: {e}")

    return surface_list if surface_list else None


