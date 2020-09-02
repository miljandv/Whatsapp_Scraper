import pyautogui


def set_dial():
    pyautogui.moveTo(1122, 902,duration=1)
    pyautogui.click()
    num = [0,6,2,8,0,4,2,5,2,3]
    for i in num:
        print(i)
        if i==0:
            pyautogui.moveTo(953, 818,duration=1)
            pyautogui.click()
        elif i==1:
            pyautogui.moveTo(828,616,duration=1)
            pyautogui.click()
        elif i==2:
            pyautogui.moveTo(951,616,duration=1)
            pyautogui.click()
        elif i==3:
            pyautogui.moveTo(1089,616,duration=1)
            pyautogui.click()
        elif i==4:
            pyautogui.moveTo(819,690,duration=1)
            pyautogui.click()
        elif i==5:
            pyautogui.moveTo(949,690,duration=1)
            pyautogui.click()
        elif i==6:
            pyautogui.moveTo(1091,690,duration=1)
            pyautogui.click()
        elif i==7:
            pyautogui.moveTo(817,754,duration=1)
            pyautogui.click()
        elif i==8:
            pyautogui.moveTo(946,754,duration=1)
            pyautogui.click()
        elif i==9:
            pyautogui.moveTo(1088,754,duration=1)
            pyautogui.click()
    pyautogui.moveTo(955,159,duration=1)
    pyautogui.click()
    pyautogui.moveTo(926,595,duration=1)
    pyautogui.click()
    pyautogui.typewrite('AAA', interval=1) 
    pyautogui.moveTo(1110,450,duration=1)
    pyautogui.click()   
        
        
def start():
    pyautogui.moveTo(959, 960,duration=1)
    pyautogui.click()

def chack_whatsapp():
    pyautogui.moveTo(1102, 644,duration=1)
    pyautogui.click()
    pyautogui.moveTo(1115, 887,duration=1)
    pyautogui.click()
    pyautogui.moveTo(785, 347,duration=1)
    pyautogui.click()
    pyautogui.moveTo(946, 377,duration=1)
    pyautogui.doubleClick()
    pyautogui.moveTo(1004, 106,duration=1) # up menu position
    pyautogui.dragTo(1018, 817,duration=1) # up menu
    pyautogui.moveTo(1095, 255,duration=1) # screenshot
    pyautogui.click()
    pyautogui.moveTo(1037, 959,duration=1) # back
    pyautogui.click()
    pyautogui.moveTo(1037, 959,duration=1) # back
    pyautogui.click()


def delete_contact():
    pyautogui.moveTo(1124, 910,duration=1) # go to dial
    pyautogui.click()
    pyautogui.moveTo(1037, 959,duration=1) # back
    pyautogui.click()
    pyautogui.moveTo(1137, 150,duration=1) # x
    pyautogui.click()
    pyautogui.moveTo(790, 150,duration=1) # <-
    pyautogui.click()
    pyautogui.moveTo(958, 287,duration=1) # AAA
    pyautogui.click()
    pyautogui.moveTo(1133, 149,duration=1) # ...
    pyautogui.click()
    pyautogui.moveTo(1005, 157,duration=1) # Delete
    pyautogui.click()
    pyautogui.moveTo(1095, 577,duration=1) # Delete confirm
    pyautogui.click()
    pyautogui.moveTo(1105, 820,duration=1) # show numeric keyboard
    pyautogui.click()


set_dial()
start()
chack_whatsapp()
start()
delete_contact()
start()

#pyautogui.locateOnScreen('looksLikeThis.png')