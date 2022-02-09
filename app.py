from database.dbManager import *

game_name = 'mafia'

app1 = MyDB()
app1.create_tab(game_name)

app1.add_item(game_name, id=2, obj_name='a key', desc='一个炫酷的按钮')