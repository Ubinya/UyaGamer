import json
from time import sleep
import sys
sys.path.append("..")
from monitor import *
from matcher import *
import pyautogui

aknt_area_wh = {
    'pub_recruit':(430, 180),
    'skip':(846,25)
}



class aknt_mod(object):
    def __init__(self, cur_handle):
        self.win = win_monitor(cur_handle)
        self.matcher = netvlad()
        print("给狗修金大人请安!! 阿库柰子mod加载了! ")
        self.mod_name = 'aknt'

    def get_anchors(self, name):
        with open(('aknt.json'), 'r') as f:
            info = json.load(f)
        return info[name]

    def click(self,x , y):
        x1, y1 = self.win.cpt_glob_pos(x, y)
        pyautogui.moveTo(x1, y1)
        pyautogui.click()

    def recruit_reload(self, slot):
        x1 = slot[0] + 430 / 2
        y1 = slot[1] + 160
        self.click(x1, y1)
        sleep(2)
        # skip bag
        self.click(846, 25)
        sleep(1)
        # skip operator showing
        self.click(846, 25)
        sleep(2)
        # reload
        self.click(x1, y1)
        sleep(3)
        # time alter
        self.click(308, 204)
        sleep(2)
        # confirm
        self.click(664, 401)
        sleep(2)

    def pub_recruit(self):
        print("阿库柰子:自动公招功能调教(测试)中! ")
        # anchors = self.get_anchors('pub_recruit')
        anchors = [(8, 120), (445, 120), (8, 315), (445, 315)]
        for i in range(len(anchors)):
            img = self.win.capture(anchors[i], 430, 180)
            done = self.matcher.pub_recruit_check(img)
            if done:
                print("招募槽 {} 完成！".format(i+1))
                print("重装中...".format(i+1))
                self.recruit_reload(anchors[i])
            else:
                print("招募槽 {} 未完成...".format(i + 1))


cur_handle = 68204
app = aknt_mod(cur_handle)
app.pub_recruit()