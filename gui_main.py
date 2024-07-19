from functions import *
import os
import PySimpleGUI as psg


layout = [[psg.Titlebar(title='Huntingdon Badge Image Formater',
                        text_color=hunt_grey,
                        background_color=hunt_white,
                        font=(custom_font, 10),
                        icon=icon_logo,)
            ],
           [psg.Text(text='Huntingdon Badge Image Formater',
                     font=(custom_font, 26),
                     expand_x=True,
                     expand_y=True,
                     justification='center',
                     background_color=hunt_white,
                     text_color=hunt_grey,
                     pad=(0, 0),)
            ],
          [psg.Image(key='IMAGE-')],
          [psg.Image(filename=logo, expand_x=True, expand_y=True, background_color=hunt_white)],
          [psg.Button('BEGIN',
                      key='-BEGIN-',
                      button_color=hunt_grey,
                      expand_x=True,
                      expand_y=True,
                      size=(20, 5),
                      mouseover_colors=hunt_red,
                      font=(custom_font, 16),),
           psg.Button('EXIT',
                      key='-EXIT-',
                      button_color=hunt_grey,
                      expand_x=True,
                      expand_y=True,
                      size=(20, 5),
                      mouseover_colors=hunt_red,
                      font=(custom_font, 16))
           ]
          ]

window = psg.Window('Huntingdon Badge Image Formater', layout, background_color=hunt_white, resizable=True, grab_anywhere=True)


while True:
    event, values = window.read()

    if event == '-BEGIN-':
        file_folder=psg.popup_yes_no('Press \'Yes\' if you need to format a single image.\nPress \'No\' if you need to format a folder of images.',
                         title='Huntingdon Badge Image Formater',
                         font=(custom_font, 16),
                         text_color=hunt_grey,
                         button_color=hunt_grey,
                         background_color=hunt_white,
                         grab_anywhere=True,
                         image=logo,
                         keep_on_top=True,
                         no_titlebar=True,)
        if file_folder == 'Yes':
            file_select=psg.popup_get_file('Select image',
                                           title='Huntingdon Badge Image Formater',
                                           font=(custom_font, 16),
                                           text_color=hunt_grey,
                                           button_color=hunt_grey,
                                           background_color=hunt_white,
                                           no_titlebar=True,
                                           grab_anywhere=True,
                                           image=logo,
                                           keep_on_top=True,)
            image_formater(file_select)
            delete_files_in_directory(temp_dir)
            break
        elif file_folder == 'No':
            folder_select = psg.popup_get_folder('Select folder',
                                             title='Select folder',
                                             font=(custom_font, 16),
                                             text_color=hunt_grey,
                                             button_color=hunt_grey,
                                             background_color=hunt_white,
                                             no_titlebar=True,
                                             grab_anywhere=True,
                                             image=logo,
                                             keep_on_top=True,)

            pathlist = os.fsencode(folder_select)
            progress_percent = 1

            for file in os.listdir(pathlist):
                filename = os.fsdecode(file)
                file_path = os.path.abspath(os.path.join(pathlist, file)).decode('ASCII')
                MAX = sum(os.path.isfile(os.path.join(folder_select, name)) for name in os.listdir(folder_select))
                psg.one_line_progress_meter(title='Progress',
                                            current_value=progress_percent,
                                            max_value=MAX,
                                            orientation='horizontal',
                                            no_titlebar=True,
                                            bar_color=(hunt_red,hunt_grey),
                                            button_color=hunt_grey,)
                image_formater(file_path)
                delete_files_in_directory(temp_dir)
                progress_percent += 1
            break
        elif event == psg.WIN_CLOSED:
            event, values = window.read()

    elif event == psg.WIN_CLOSED or event == '-EXIT-':
        break

window.close()