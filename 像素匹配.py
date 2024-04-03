#像素匹配
import pyautogui as pg

try:
    while True:
        x,y = pg.position() #获取鼠标位置
        color = str(pg.pixel(x,y)).rjust(15) #用pixel()获取点x,y处的像素RGB颜色
        print(color,end = '')
        print('\b'*len(color),end = '',flush = True)
        
except KeyboardInterrupt:
    print("fine\n")
    

 
#静态方法
import pyautogui

im = pyautogui.screenshot()  #先获取屏幕截图
a = im.getpixel((100, 200)) #获取坐标点（100，200）处的像素RGB颜色
print(a)
