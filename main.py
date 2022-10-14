import pyautogui
from time import sleep

def click_on_interval(seconds = 5,):
    try: 
        pos = pyautogui.position()
        
        while True:
            sleep(seconds)
            pyautogui.click(pos)
            print("Clicked")

    except KeyboardInterrupt:
        print("Exit")


def main():
   click_on_interval() 


if __name__=="__main__":
    main()
