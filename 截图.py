#截图
import pyautogui
##
import time
import os
###两种保存截图的方式 截图保存在工作目录下
##im1 = pyautogui.screenshot()
##im1.save('my_screenshot.png')
##
##im2 = pyautogui.screenshot('my_screenshot2.png')


os.chdir('E:/Python')
##button7location = pyautogui.locateOnScreen('button.png')
### returns (left, top, width, height) of matching region
##print(button7location)
while True:
    try:   
        #button7location = pyautogui.locateOnScreen('t.png',region = (0,0,1000,1000),grayscale = True,confidence = 0.7)
        # returns (left, top, width, height) of matching region
        while True:
            buttonx, buttony = pyautogui.locateCenterOnScreen('target.png',grayscale = True,confidence = 0.7)# returns (x, y) of matching region
            pyautogui.click(buttonx, buttony)  # clicks the center of where the button was found

        
    except pyautogui.ImageNotFoundException:
        print("没有匹配的图像！")

    except IOError:
        print("文件路径有误，请检查！")


