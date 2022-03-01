from enum import Enum
import json
import os

class ObjGroup(Enum):
    DEFAULT = 0
    BUTTON = 1
    ICON = 2
    BUFF = 3
    CARD = 4


class ObjTable(object):
    def __init__(self, game):
        self.game = game#存储游戏名称字符串，作为数据库名称
        if os.path.exists(self.game+'.json'):# 如果数据库json存在就直接读入
            with open(self.game + '.json', 'r', encoding='utf-8') as f:
                self.objs = json.load(f)
            print('数据库{}读入完成'.format(self.game))
        else:
            self.reset_db()
            print('数据库{}不存在，创建完成'.format(self.game))

    # 以及这里建立后就把数据库读入内存，其实实际使用时可以根据运行的游戏只读取一个数据库



    def reset_db(self):
        with open(self.game+'.json','w', encoding='utf-8') as f:
            save = [
                {
                    'id':-1,
                    'obj_name':'init',
                    'desc':'init desc',
                    'group':0
                }]
            json_str = json.dumps(save,indent=4,ensure_ascii=False)
            f.write(json_str)
        self.objs = save
        print('数据库{}重置完成'.format(self.game))

    def add_item(self, **kwargs):

        self.objs.sort(key=self.item_id)
        new_id = self.objs[-1]['id'] + 1
        new_item = {
            'id': new_id,
            'obj_name': kwargs['obj_name'],
            'desc': kwargs['desc'],
            'group': kwargs['group']
        }
        self.objs.append(new_item)
        with open(self.game+'.json','w', encoding='utf-8') as f:
            json_str = json.dumps(self.objs, indent=4, ensure_ascii=False)
            f.write(json_str)
        print('数据库{}插入新条目完成 id：{}'.format(self.game, new_id))

    def item_id(self, elem):
        return elem['id']



class MyDB(object):
    def __init__(self):
        self.games = {}

    def add_game(self, game):
        new_game = ObjTable(game)
        self.games[game] = new_game
        print('新数据库{}添加完成'.format(game))

    def add_obj(self, **kwargs):
        game = kwargs['game']
        self.games[game].add_item(**kwargs)





