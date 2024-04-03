#键鼠操作
import pyautogui, sys

#实时监测
print("Press Ctrl-C to exit.") 

try:
    while True:
        x, y = pyautogui.position() #获取鼠标位置
        positionStr = 'X: '+str(x).rjust(4) + 'Y: ' + str(y).rjust(4) #右对齐，长度为4
        print(positionStr, end = '') 
        print('\b' * len(positionStr) , end = '' ,flush = True) #\b为退格符 flush刷新防止延迟显示
except KeyboardInterrupt:
    print( '\n' )

    
