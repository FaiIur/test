#绘制五角星
#在屏幕中心画一个五角星
import pyautogui as pg
import math
import time

pg.FAILSAFE = True

# 计算五角星的外接圆半径
R = 250 / (2 * math.sin(36 * math.pi / 180))

# 计算五角星的中心点坐标
x_c,y_c = pg.size()#  当前屏幕的分辨率（宽度和高度
x_c /= 2
y_c /= 2

# 计算五角星的五个顶点的坐标
A_x = x_c
A_y = y_c - R
B_x = x_c + R * math.sin(72 * math.pi / 180)
B_y = y_c - R * math.cos(72 * math.pi / 180)
C_x = x_c + R * math.sin(36 * math.pi / 180)
C_y = y_c + R * math.cos(36 * math.pi / 180)
D_x = x_c - R * math.sin(36 * math.pi / 180)
D_y = y_c + R * math.cos(36 * math.pi / 180)
E_x = x_c - R * math.sin(72 * math.pi / 180)
E_y = y_c - R * math.cos(72 * math.pi / 180)


# 移动到顶点E进行按下操作
pg.moveTo(E_x, E_y)
pg.mouseDown(button = 'left')

# 依次拖动到顶点B, D, A, C, E
pg.dragTo(B_x, B_y, 1, button='left',mouseDownUp=False)
pg.dragTo(D_x, D_y, 1, button='left',mouseDownUp=False)
pg.dragTo(A_x, A_y, 1, button='left',mouseDownUp=False)
pg.dragTo(C_x, C_y, 1, button='left',mouseDownUp=False)
pg.dragTo(E_x, E_y, 1, button='left',mouseDownUp=True)

##pg.moveTo(B_x, B_y, 1)
##pg.moveTo(D_x, D_y, 1)
##pg.moveTo(A_x, A_y, 1)
##pg.moveTo(C_x, C_y, 1)
##pg.moveTo(E_x, E_y, 2)


