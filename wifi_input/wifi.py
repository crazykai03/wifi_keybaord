from tkinter import *
from PIL import ImageTk , Image
import threading
import time
from tkinter import ttk

import tkinter.font as font





focus_index = 0
button_list_index =0







root = Tk()

# Adjust size
root.geometry("800x480")

# Add image file
bg = PhotoImage(file="Bg.png")
logo = PhotoImage(file="Logo.png")
def write_command():
    print("ready")
    print(ssid_text.get('1.0','end'))
    print(password_text.get('1.0','end'))


def create_current_button(display_index):
    x_position_index = 1
    y_position_index = 0
    for button in buttonlist[display_index]:
        command = lambda x=button: select(x)
        if button == 'Space':
            button = Button(root, text=button,font=("Helvetica", 10),bg='black',fg='white', height=2, width=85, command=command)
            x_position_index = 8
        elif button == 'Enter':
            button = Button(root, text=button, font=("Helvetica", 10), bg='red', fg='white', height=2, width=5,
                            command=command)
        else:
            button = Button(root, text=button,font=("Helvetica", 10), bg='black',fg='white',height=2, width=5, command=command)

        canvas_widget = canvas1.create_window(45 * x_position_index, 270 + y_position_index, window=button)
        x_position_index = x_position_index + 1
        if x_position_index > 15:
            y_position_index = y_position_index + 45
            x_position_index = 1





def ssid_focus_in(event):
    global focus_index
    focus_index=1
def pass_focus_in(event):
    global focus_index
    focus_index=2

def select(value):
    global button_list_index
    print(value)
    value_operate = value
    if value == 'Space':
        value_operate=" "

    elif value == 'Enter':
        write_command()
        return

    elif value == 'Tab':
        value_operate='\t'
    elif value == 'Caps':
        button_list_index=1
        create_current_button(button_list_index)
        return
    elif value == 'CAPS':
        button_list_index=0
        create_current_button(button_list_index)
        return
    elif value == 'Shift ↑':
        button_list_index=2
        create_current_button(button_list_index)
        return
    elif value == '↑ Shift':
        button_list_index=0
        create_current_button(button_list_index)
        return










    if focus_index==1:
        if(value_operate=='Del'):
            ssid_text.delete(1.0, END)
        elif value_operate == 'Backs':
            i = ssid_text.get(1.0, END)
            newtext = i[:-2]
            ssid_text.delete(1.0, END)
            ssid_text.insert(INSERT, newtext)
        else:
            ssid_text.insert(INSERT,value_operate)
    if focus_index == 2:
        if (value_operate == 'Del'):
            password_text.delete(1.0, END)
        elif value_operate == 'Backs':
            i = password_text.get(1.0, END)
            newtext = i[:-2]
            password_text.delete(1.0, END)
            password_text.insert(INSERT, newtext)
        else:
            password_text.insert(INSERT, value_operate)






canvas1 = Canvas(root, width=800,
                 height=480,bd=0, highlightthickness=0 , bg="#2B2E35")


canvas1.pack(fill="both", expand=True)


#bg_img_all = canvas1.create_image(400,240,)
logo_btn = canvas1.create_image(24+186,24+28,image=logo)

ssid_text = Text(canvas1,width = 15, height=1, font=("Helvetica", 20))
ssid_text.place(x=200,y=120)
password_text = Text(canvas1,width = 15, height=1, font=("Helvetica", 20))
password_text.place(x=200,y=180)
canvas1.create_text((120, 140), text="SSID        :", font=("Helvetica", 20),fill='white')
canvas1.create_text((100, 200), text="PASSWORD :", font=("Helvetica", 20),fill='white')




ssid_text.bind("<FocusIn>", ssid_focus_in)
password_text.bind("<FocusIn>", pass_focus_in)





buttons = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backs', 'Del',
           'Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', '7', '8', '9',
           'Caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'Enter', '4', '5', '6',
           'Shift ↑', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '↑ Shift', '1', '2', '3',
           'Space']


capsButtons = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backs', 'Del',
               'Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', '7', '8', '9',
               'CAPS', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', 'Enter', '4', '5', '6',
               'Shift ↑', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', '↑ Shift', '1', '2', '3',
               'Space']

leftShiftButtons = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 'Backs', 'Del',
                    'Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', ']', '7', '8', '9',
                    'Caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ':', 'Enter', '4', '5', '6',
                    'Shift ↑', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<', '>', '?', '↑ Shift', '1', '2', '3',
                    'Space'

                    ]

buttonlist = [buttons,capsButtons,leftShiftButtons]

create_current_button(button_list_index)






root.overrideredirect(True)

root.mainloop()