import pyautogui as ptg
import time
# import sys

class TargetNotFoundException(Exception):
    pass

ptg.FAIL_SAFE = True


def ptg_maxImize():
    ptg.keyDown('Alt')
    ptg.press(' ')
    ptg.press('x')
    ptg.keyUp('Alt')


def ptg_reDuce():
    ptg.keyDown('Alt')
    ptg.press(' ')
    ptg.press('r')
    ptg.keyUp('Alt')

# area1 = (0, 0, 960, 540)
# area2 = (960, 0, 1920, 540)
# area3 = (0, 540, 960, 1080)
# area4 = (960, 540, 1920, 1080)
# area5 = (480, 270, 1920-480, 1080-270)


def move_to_target(obj_pic, obj_loc, try_n_times=20, int_erval=2):
    for i in range(try_n_times):
        print(i)
        target = ptg.locateCenterOnScreen(obj_pic, region=obj_loc)
        # if target != None:
        if target:
            ptg.moveTo(target)
            return
        else:
            print("target not found")
        time.sleep(int_erval)
    # sys.exit("ERROR:target not found")
    raise TargetNotFoundException("ERROR:target not found")

# move_to_target('reduce_window.png', area2)

# ptg.click()
try:
    print("anything")
except TargetNotFoundException:
    pass
