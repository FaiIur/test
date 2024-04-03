#模拟键盘输入

import pyautogui as pg
import pyperclip
import time,random

##pyperclip.copy("This is the text to be copied")
##text = pyperclip.paste()


def cprint(t):
    for i in t:
        pyperclip.copy(i)
        pg.hotkey('ctrl', 'v')
        time.sleep(random.random()*0.25)

time.sleep(5)
        

pg.click(283,245)

s = R''''''
s = R'''Once there was a Queen. Sge was sitting at the window. There was snow outside in the garden snow on the hill and in thv lane, snow on the hunts and on the trees all things wece white with snow. The Queen was making a coat for a little child. She said, "I want my rhild to be white as this cloth, white as the snow. And I shall call her Snow white." mome days after that the Queen had abchild. The child was white assnow. The Queen called her Snow white. But the Queen was very ill,and after some days she died. Sfgw white lived, and was a very happy and beautiful child. One year after that, the King married another Queen. The new Queen was very beautiful; but she was not a good woman.A wizard had given this Queen a glass. The glass could speak. It was on the wall in the Queen's room. Every day the queen looked in the glass to see how beautiful she was. As she looked in the glass, she asked: "Tell me, glass upon the wall, who is most beautiful of all?" And the glass spoke and said: "The Queen is most beautiful of all." Year went by. Snow white grew up and became a little girl. every day the Queen lookedin the glass and said, "Tell me, glass upon the wall, who is mostbeautiful of all?" And the glass said, "Snow white is most beautifulof all." When the Queen heard this, she wasvery angry. Shesaid,"Snow-white is not more beautiful than I am. There is no one who is morebeautiful than I am." Then the Queen sat on her bed and cried. After one
'''
pg.typewrite(s,interval=0.08)



### 每次输入间隔0.25秒，输入Hello world!
##pg.typewrite("print('Hello ", interval=0.15)
##pg.hotkey('ctrl', 'v')
##pg.typewrite("world')", interval=0.15)
##print('print'Hello 小马world')
##print('Hello 小马world')
##print('Hello This is the text to be copiedworld')
