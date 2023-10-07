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


square =''

#определяем окно paint
paintwindow = auto.WindowControl(searchDepth=1, ClassName='MSPaintApp')
if paintwindow.Exists(1):
    print('найдено окно paint')
auto.ButtonControl(searchFromControl=paintwindow, Name="Pencil").Click()

#определяем родительский элеиент
shapes = auto.GroupControl(searchFromControl=paintwindow, Name="Shapes")
#кликаем по дочернему элементу - квадрат
auto.ListItemControl(searchFromControl=shapes, Name="Rectangle").Click()
#рисуем квадрат
auto.PaneControl(searchFromControl=paintwindow, 
                 Name = "Using Rectangle tool on Canvas").DragDrop(100, 100, 200, 200)
print('rectangle success')




