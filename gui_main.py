import PySimpleGUI as psg
from settings import *
from functions import *


layout1 = [[psg.Titlebar(title='Huntingdon Badge Image Formater',
                        text_color=hunt_grey,
                        background_color=hunt_white,
                        font=(custom_font, 10),
                        icon=icon_logo)],
           [psg.Text(text='Huntingdon Badge Image Formater',
                     font=(custom_font, 26),
                     size=20,
                     expand_x=True,
                     justification='center',
                     background_color=hunt_white,
                     text_color='#696b68')],
          [psg.Image(key='IMAGE-')],
          [psg.Image(filename=logo)],
          [psg.Button('BEGIN',
                      key='-BEGIN-',
                      button_color=hunt_grey,
                      size=(30, 30),
                      mouseover_colors=hunt_red,
                      font=(custom_font, 16))],
          [psg.Button('EXIT',
                      key='-EXIT-',
                      button_color=hunt_grey,
                      size=(30, 30),
                      mouseover_colors=hunt_red,
                      font=(custom_font, 16))],
          ]

layout2 = [[psg.Titlebar(title='Huntingdon Badge Image Formater',
                        text_color=hunt_grey,
                        background_color=hunt_white,
                        font=(custom_font, 10),
                        icon=icon_logo)],
            [psg.Text(text='Huntingdon Badge Image Formater',
                      font=(custom_font, 26),
                      size=20,
                      expand_x=True,
                      justification='center',
                      background_color=hunt_white,
                      text_color='#696b68')],
            [psg.FileBrowse()],
            ]

layout = layout1

window = psg.Window('Huntingdon Badge Image Formater', layout, size=(800, 400), element_justification='c', background_color='#ffffff')

layout = 1

while True:
    event, values = window.read()
    print(event, values)

    if event == psg.WIN_CLOSED:
        break
    elif event == '-BEGIN-':
        print("Crap")

window.close()