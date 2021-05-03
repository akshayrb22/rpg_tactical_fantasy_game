# -*- coding: utf-8 -*-
"""
Created on Mon May  3 16:10:21 2021

@author: Tejan
"""
from pathlib import Path

import xml.etree.ElementTree as ET
import os
import random
from src.game_entities.character import Character
#from src.game_entities.foe import Foe


CUR_DIR = os.getcwd()
CUR_DIR = Path(CUR_DIR)
sprites_folder = CUR_DIR/'imgs'/'dungeon_crawl'/'player'/'base'

def load_character_xml(level):
    level = str(level)
    tree = ET.parse(f'data/characters/level{level}.xml')

    #filepath = CUR_DIR+'/data/characters/'+'level_0_'+level+'.xml'
    #tree = ET.parse(filepath)
    root = tree.getroot()
    #variable file contains the data from xml file
    #return file if you want to see xml file as well
    #with open(filepath, 'r') as f:
       # file = f.read()
    return root

root1 = load_character_xml(0.1)
all_char_tags = [protagonist.tag for protagonist in root1]
n_protagonists  = int(6 * 2 + 7)#02 represents level
selected_protagonists_tags= random.choices(all_char_tags, k = n_protagonists)

def select_protagonists(level, x,y):
    level = str(level)
    tree = ET.parse(f'data/characters/level{level}.xml')
    root1 = tree.getroot()
    all_char_tags = [protagonist.tag for protagonist in root1]
    n_protagonists  = int(6 * 2 + 7)#02 represents level
    selected_protagonists_tags= random.choices(all_char_tags, k = n_protagonists)


    protagonists = []
    for prot_tag in selected_protagonists_tags:
        prot_info = root1.find(prot_tag)
        if prot_info.find('reach') is None:
            reach = []
        else:
            
            reach = [int(i) for i in prot_info.find('keywords').text.strip().split(',')]
        if prot_info.find('keywords') is None:
            
             keywords = []
        else:
            keywords = [int(i) for i in prot_info.find('keywords').text.strip().split(',')]

        sprite_path = str(sprites_folder / Path(prot_info.find('sprite').text.strip()))
        #print(sprite_path)
        prot = Character(prot_info.tag,
                     (x,y),
                     sprite_path,
                     int(prot_info.find('sprite').text),
                     int(prot_info.find('hp').text),
                     int(prot_info.find('defense').text),
                     int(prot_info.find('res').text),
                     int(prot_info.find('strength').text),
                     int(prot_info.find('strength').text),
                     reach,
                     [],
                     keywords
                     )
        protagonists.append(prot)
    return protagonists