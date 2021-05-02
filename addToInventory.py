import xml.etree.ElementTree as ET
import numpy as np
from io import BytesIO
import os


def placeItem(difficulty: float, path: str):
    potion_list = ['life_potion', 'super_life_potion', 'hyper_life_potion', 'ultra_life_potion']
    lvl_000_weights = [0.5, 0.3, 0.15, 0.05]
    lvl_025_weights = [0.2, 0.5, 0.2, 0.1]
    lvl_050_weights = [0.2, 0.2, 0.4, 0.2]
    lvl_075_weights = [0.05, 0.15, 0.5, 0.3]
    item = None
    if difficulty == 0.0:
        item = np.random.choice(potion_list, p=lvl_000_weights)
    elif difficulty == 0.25:
        item = np.random.choice(potion_list, p=lvl_025_weights)
    elif difficulty == 0.5:
        item = np.random.choice(potion_list, p=lvl_050_weights)
    elif difficulty == 0.75:
        item = np.random.choice(potion_list, p=lvl_075_weights)
    else:
        print('Invalid difficulty.')
        exit()
    tree = ET.parse(path)
    tree.find('.//inventory/item').text = item
    tree.write(path)


if __name__ == '__main__':
    CUR_DIR = os.getcwd()
    CHARACTER_SHEET = CUR_DIR + '/data/characters.xml'
    placeItem(0.75, CHARACTER_SHEET)
