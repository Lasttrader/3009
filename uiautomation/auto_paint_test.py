import uiautomation as auto
import subprocess
import time

# Запустите Paint с помощью командной строки (subprocess)
subprocess.Popen("mspaint.exe")

# Дождитесь, чтобы Paint полностью открылся (время задержки зависит от производительности компьютера)
time.sleep(2)

# Используйте inspect.exe для поиска AutomationId окна Paint
# Скопируйте AutomationId для окна Paint

# Теперь используйте AutomationId для взаимодействия с окном Paint
paint_window = auto.WindowControl(AutomationId="TitileBar")
if paint_window.Exists(1):
    print('найдено окно paint')

paint_window.SetFocus()

# Установите инструмент "Карандаш"
auto.PaneControl(AutomationId="4103").Click()

# Установите цвет чернил
auto.PaneControl(AutomationId="1008").Click()

# Выберите черный цвет
auto.PaneControl(AutomationId="8041").Click()

# Перейдите к рабочей области Paint
work_area = auto.PaneControl(AutomationId="PositioningContainer")
work_area.Click(100, 100)  # Выберите начальные координаты

# Рисуем квадрат
auto.MouseDragTo(200, 200) # 