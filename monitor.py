import win32api, win32con, win32gui
from PIL import Image, ImageGrab
import tools


def get_win_handle(name, type=0):
    handle = win32gui.FindWindow(type, name)
    return handle

def win_up(handle):
    win32gui.SendMessage(handle, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
    text = win32gui.SetForegroundWindow(handle)


class win_monitor(object):
    def __init__(self, handle):
        self.handle = handle
        self.refresh_win_pos()

    def refresh_win_pos(self):
        # left top point & right bot point
        self.x1, self.y1, self.x2, self.y2 = win32gui.GetWindowRect(self.handle)

    def get_win_pos(self):
        return win32gui.GetWindowRect(self.handle)

    def tick(self):
        self.refresh_win_pos()
        img = ImageGrab.grab((self.x1, self.y1, self.x2, self.y2))
        return img

    def capture(self, pos, w, h):
        self.refresh_win_pos()
        x1, y1 = self.cpt_glob_pos(pos[0], pos[1])
        x2 = x1 + w
        y2 = y1 + h
        img = ImageGrab.grab((x1, y1, x2, y2))
        return img

    def cpt_rel_pos(self, glob_x, glob_y):
        self.refresh_win_pos()
        rel_x = glob_x - self.x1
        rel_y = glob_y - self.y1
        return (rel_x, rel_y)

    def cpt_glob_pos(self, rel_x, rel_y):
        self.refresh_win_pos()
        glob_x = rel_x + self.x1
        glob_y = rel_y + self.y1
        return (glob_x, glob_y)

'''
cur_handle = 1314182
app = win_monitor(cur_handle)
tools.cpt_rel(app)
# x1, y1, x2, y2 = get_window_pos('sub')
'''





