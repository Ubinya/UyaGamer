from database.dbManager import *
from database.dbGui import *

game_name = 'mafia'

app1 = MyDB()
#app1.setup_tab()

app1.add_obj(game='mafia', id=2, obj_name='key1', desc='一个炫酷的按钮', pack = 1)
exit()



app=QApplication(sys.argv)
ex = dbWin()
sys.exit(app.exec_())