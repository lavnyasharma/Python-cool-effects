import os
from pyfiglet import Figlet

def print_cool(text):

    cool_text = Figlet(font="default")

    os.system("cls")
    os.system('mode con: cols=75 lines= 30')
    return str(cool_text.renderText(text))

if __name__ == '__main__':
    print(print_cool("LAVANYA"))