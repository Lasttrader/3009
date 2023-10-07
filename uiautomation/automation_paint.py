#!python3
# -*- coding: utf-8 -*-
# works on windows XP, 7, 8, 8.1 and 10
import os
import sys
import time
import subprocess

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # not required after 'pip install uiautomation'
import uiautomation as auto

auto.uiautomation.DEBUG_EXIST_DISAPPEAR = True  # set it to False and try again, default is False
auto.uiautomation.DEBUG_SEARCH_TIME = True  # set it to False and try again, default is False
auto.uiautomation.TIME_OUT_SECOND = 10  # global time out

def get_squared(window, square):
    
    pass


paintWindow = auto.WindowControl(searchDepth=1, ClassName='MSPaintApp')

#определяем клики по ID элемента 
paintWindow.SetActive()
paintWindow.ButtonControl(AutomationId='TogglePaneButton').Click()

square =''

if paintWindow.Exists(1):
    print('найдено окно paint')


# if __name__ == '__main__':
#     osVersion = os.sys.getwindowsversion().major
#     if osVersion >= 10: CalcOnWindows10()

#     auto.Logger.Write('\nPress any key to exit', auto.ConsoleColor.Cyan)
#     import msvcrt
#     while not msvcrt.kbhit():
#         time.sleep(0.05)
