import win32gui
import win32api
import win32con
import pyautogui
from util import *
import keyboard as kb
from PIL import Image, ImageGrab
import json
import os
import time
# from pymouse import PyMouse


# 输入你所使用的模拟器名称，如果不行把hwnd_list输出看看模拟器窗口名称
# 注意，模拟器窗口不能最小化，可以放在别的窗口下面，截图时会自动提到最前
win_title = "夜神模拟器"
save_path = "SavedImg/"

hwnd_list = {} # 用来存放所有窗口句柄和名称

def get_all_hwnd(hwnd, mouse):
    if (win32gui.IsWindow(hwnd) and
        win32gui.IsWindowEnabled(hwnd) and
        win32gui.IsWindowVisible(hwnd)):
        hwnd_list.update({hwnd: win32gui.GetWindowText(hwnd)})

# m = PyMouse()

class capturer:
    def __init__(self, title):
        self.win_title = title
        self.get_win_handle()
        self.refresh_win_pos()
        # self.imcnt = 0

        # if os.path.exists(save_path+'save.json'):
        #     with open(save_path+'save.json','r') as load_f:
        #         load_dict = json.load(load_f)
        #         self.imcnt = int(load_dict['cur_cnt'])





    # 获取窗口句柄
    def get_win_handle(self):
        for h, t in hwnd_list.items():
            if t:
                if t == self.win_title:
                    self.handle = h #窗口句柄
                    self.win_t = t #窗口名称
                    #hwnd=win32gui.FindWindow(None,t)
                    #win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
                    break

    # 输出窗口位置 左上角和右下角的x y坐标
    def refresh_win_pos(self):
        # left top point & right bot point
        self.left, self.top, self.right, self.bot = win32gui.GetWindowRect(self.handle)
        return self.left,self.top,self.right,self.bot

    # 保持窗口最前
    def win_up(self):
        win32gui.SetForegroundWindow(self.handle)

    def take_a_shot(self):
        # 格式化成2016-03-20 11:45:39形式
        save_name = time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())
        self.refresh_win_pos()
        # self.win_up()
        img = ImageGrab.grab((self.left,self.top,self.right,self.bot))
        img.save(save_path+save_name+".jpg", "JPEG")
        print("保存图片"+save_name+".jpg")
        # self.imcnt += 1

    def reload(self):
        self.imcnt = 0
        with open((save_path+'save.json'),'w') as f:
            save={'cur_cnt':self.imcnt}
            json_str=json.dumps(save)
            f.write(json_str)
        print("重新开始截图，注意未备份图片会被覆盖")

    # 监听截图,j键截图，t键退出
    def capture_loop(self):
        print("开始截图循环，J键截图, T键退出, 请手动把模拟器窗口放在最前")
        kb.add_hotkey('j', self.take_a_shot)
        # kb.add_hotkey('q', self.reload)
        kb.wait('t')
        print("结束截图循环结束")

        # with open((save_path+'save.json'),'w') as f:
        #     save={'cur_cnt':self.imcnt}
        #     json_str=json.dumps(save)
        #     f.write(json_str)




win32gui.EnumWindows(get_all_hwnd, 0)
app = capturer(win_title)
app.capture_loop()
