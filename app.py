from database.dbManager import *
from database.dbGui import *

game_name = 'mafia'


app = ObjTable(game_name)
for i in range(5):
    app.add_item(game='mafia', obj_name='key1', desc='一个炫酷的按钮', group = 1)

exit()



app=QApplication(sys.argv)
ex = dbWin()
sys.exit(app.exec_())