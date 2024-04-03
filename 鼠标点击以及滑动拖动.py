#点击以及滑动操作
import pyautogui as pg
import math
import time

# 计算五角星的外接圆半径
R = 250 / (2 * math.sin(36 * math.pi / 180))

# 计算五角星的中心点坐标
x_c = 1919/2
y_c = 1079/2

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


# 移动到顶点E
pg.moveTo(E_x, E_y)

# 依次拖动到顶点B, D, A, C, E
pg.dragTo(B_x, B_y, 1, button='left')
time.sleep(0.1)
pg.dragTo(D_x, D_y, 1, button='left')
time.sleep(0.1)
pg.dragTo(A_x, A_y, 1, button='left')
time.sleep(0.1)
pg.dragTo(C_x, C_y, 1, button='left')
time.sleep(0.1)
pg.dragTo(E_x, E_y, 1, button='left')
