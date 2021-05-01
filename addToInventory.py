import xml.etree.ElementTree as ET
from io import BytesIO
import os


def placeItem(difficulty: float, path: str):
    item = None

    if difficulty == 0.0:
        item = 'key'
    elif difficulty == 0.25:
        item = 'door_key'
    elif difficulty == 0.5:
        item = 'life_potion'
    elif difficulty == 0.75:
        item = 'vigor_potion'
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
