#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from pathlib import Path

import xml.etree.ElementTree as ET
import os
import random
from src.game_entities.foe import Foe


CUR_DIR = os.getcwd()
CUR_DIR = Path(CUR_DIR)
# print(CUR_DIR / Path('asd/abc'))


def f(lvl: float, x, y):
    sprites_folder = CUR_DIR/'imgs'/'dungeon_crawl'/'monster'
    tree = ET.parse(f'data/foes/foes{lvl}.xml')
    root = tree.getroot()
    all_foe_tags = [foe.tag for foe in root]
    n_foes = int(6 * lvl + 7)
    selected_foes_tags = random.choices(all_foe_tags, k=n_foes)
    foes = []
    for foe_tag in selected_foes_tags:
        foe_info = root.find(foe_tag)
        if foe_info.find('reach') is None:
            reach = []
        else:
            reach = [int(i) for i in foe_info.find('reach').text.strip().split(',')]

        if foe_info.find('keywords') is None:
            keywords = []
        else:
            keywords = [i for i in foe_info.find('keywords').text.strip().split(',')]
        sprite_path = str(sprites_folder / Path(foe_info.find('sprite').text.strip()))
        print(sprite_path)
        foe = Foe(foe_info.tag,
                  (x, y),
                  sprite_path,
                  int(foe_info.find('hp').text),
                  int(foe_info.find('defense').text),
                  int(foe_info.find('resistance').text),
                  int(foe_info.find('move').text),
                  int(foe_info.find('strength').text),
                  foe_info.find('attack_kind').text.strip(),
                  foe_info.find('strategy').text.strip(),
                  reach,
                  int(foe_info.find('xp_gain').text),
                  [],
                  keywords
                  )
        foes.append(foe)

    return foes

f(0.5, 1, 1)

