#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background


class EntityFactory:

    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'level1_bg':
                list_bg=[]
                for i in range(8):
                    list_bg.append(Background(f'level1_bg{i}', (0, 0)))
