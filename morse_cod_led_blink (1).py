from tkinter import *
import tkinter.font
import time
from xml.dom.minidom import CharacterData
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

led = LED(26)

# writing code needs to create the main window of the application creating main window object named gui
gui = Tk()

# giving title to the main window
gui.title("MORSE BLINKER")

# Open window having dimension 400x400
gui.geometry('620x400')


# Defining a font to use it for the button text (optional)
buttonFont = tkinter.font.Font(family="Helvetica", size= 12, weight="bold")
HeaderFont = tkinter.font.Font(family="Helvetica", size= 24, weight="bold")

#Label to show some header text  
header= Label(gui, text ="BLINK YOUR NAME IN MORSE CODE", font= HeaderFont)
header.grid(row=1, column= 0, padx= 10, pady= 10)

#-------------Entry Widget to get name input----------------#
name = StringVar()
name = Entry(gui, textvariable="Enter First Name", font= HeaderFont)
name.grid(row = 3, column=0, pady= 10)


#--------------BLINK Button-----------#

def dot():          # funciton to blink a dot of morse code
    led.on()
    time.sleep(0.2)
    led.off()
    time.sleep(0.2)

def dash():         # function to blink a dash of morse code
    led.on()
    time.sleep(0.6)
    led.off()
    time.sleep(0.6)

L = CharacterData
def morseConverter(L):      # function to compare and blink the led according to the corresponding alphabets
    if L == 'A':
        dot()
        dash()
        time.sleep(0.2)
    if L == 'B':
        dash()
        dot()
        dot()
        dot()
        time.sleep(0.2)
    if L == 'C':
        dash()
        dot()
        dash()
        dot()
        time.sleep(0.2)
    if L == 'D':
        dash()
        dot()
        dot()
        time.sleep(0.2)
    if L == 'E':
        dot()
        time.sleep(0.2)
    if L == 'F':
        dot()
        dot()
        dash()
        dot()
        time.sleep(0.2)
    if L == 'G':
        dash()
        dash()
        dot()
        time.sleep(0.2)
    if L == 'H':
        dot()
        dot()
        dot()
        dot()
        time.sleep(0.2)
    if L == 'I':
        dot()
        dot()
        time.sleep(0.2)
    if L == 'J':
        dot()        
        dash()
        dash()
        dash()
        time.sleep(0.2)
    if L == 'K':
        dash()
        dot()
        dash()
        time.sleep(0.2)
    if L == 'L':
        dot()
        dash()
        dot()
        dot()
        time.sleep(0.2)
    if L == 'M':
        dash()
        dash()
        time.sleep(0.2)
    if L == 'N':
        dash()
        dot()
        time.sleep(0.2)
    if L == 'O':
        dash()
        dash()
        dash()
        time.sleep(0.2)
    if L == 'P':
        dot()
        dash()
        dash()
        dot()
        time.sleep(0.2)
    if L == 'Q':
        dash()
        dash()
        dot()
        dash()
        time.sleep(0.2)
    if L == 'R':
        dot()
        dash()
        dot()
        time.sleep(0.2)
    if L == 'S':
        dot()
        dot()
        dot()
        time.sleep(0.2)
    if L == 'T':
        dash()
        time.sleep(0.2)
    if L == 'U':
        dot()
        dot()
        dash()
        time.sleep(0.2)
    if L == 'V':
        dot()
        dot()
        dot()
        dash()
        time.sleep(0.2)
    if L == 'W':
        dot()
        dash()
        dash()
        time.sleep(0.2)
    if L == 'X':
        dash()
        dot()
        dash()
        dot()
        time.sleep(0.2)
    if L == 'Y':
        dot()
        dash()
        dash()
        dash()
        time.sleep(0.2)
    if L == 'Z':
        dot()
        dash()
        time.sleep(0.2)

def blink():            # final function to blink the inputted name in morse code 
    for x in name.get():
        morseConverter(x)

blink_button = Button(gui, text='BLINK!', font= buttonFont, command= blink, bg= '#ADD8E6', height= 3, width= 15)
blink_button.grid(row= 4, column=0)


# ------------Exit Button------------#
def close_window():
    GPIO.cleanup()
    gui.destroy()

exit_button = Button(gui, text='EXIT', command=close_window, bg= '#008000', height= 3, width=9)
# Set the position of button on the bottom 
exit_button.grid(row=5, column=0, pady= 20)
# Syntax to perform the same function as exit button if the close window button on navigation bar is pressed
gui.protocol("WM_DELETE_WINDOW", close_window)


# calling mainloop method which is used
# when your application is ready to run
# and it tells the code to keep displaying
gui.mainloop()


