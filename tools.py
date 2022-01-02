import os,time
import pyautogui as pag

def cpt_rel(monitor):
    try:
        while True:
            print("Press Ctrl-C to end")
            x, y = pag.position()  # 返回鼠标的坐标
            posStr = "Position:" + str(x).rjust(4) + ',' + str(y).rjust(4)
            print(posStr)  # 打印坐标
            time.sleep(0.2)
            os.system('cls')  # 清楚屏幕
            rel_x, rel_y = monitor.cpt_rel_pos(x, y)
            print("rel_x = {}, and rel_y = {}".format(rel_x, rel_y))
    except  KeyboardInterrupt:
        print('end....')
