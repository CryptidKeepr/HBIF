import PySimpleGUI as sg
import io
import os.path
from PIL import Image

# --------------------------------- Define Layout ---------------------------------

left_col = [[sg.Text('Folder'), sg.In(size=(25,1), enable_events=True ,key='-FOLDER-'), sg.FolderBrowse()],
            [sg.Listbox(values=[], enable_events=True, size=(40,20),key='-FILE LIST-')]]

pil_image = Image.open(io.BytesIO('-FOLDER-'))
png_bio = io.BytesIO()
pil_image.save(png_bio, format="PNG")
png_data = png_bio.getvalue()

images_col = [[sg.Text('You choose from the list:')],
              [sg.Text(size=(40,1), key='-TOUT-')],
              [sg.Image(png_data, key='-IMAGE-')]]

# --------------------------------- Full Layout ---------------------------------
layout = [[sg.Column(left_col), sg.VSeperator(), sg.Column(images_col)]]

# --------------------------------- Create Window ---------------------------------

window = sg.Window('Image Viewer', layout)

# --------------------------------- Event Loop ---------------------------------
while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == '-FOLDER-':
        folder = values['-FOLDER-']
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [f for f in file_list if os.path.isfile(
            os.path.join(folder, f)) and f.lower().endswith((".png", ".jpg", "jpeg", ".tiff", ".bmp"))]
        window['-FILE LIST-'].update(fnames)
    elif event == '-FILE LIST-':
        try:
            filename = os.path.join(values['-FOLDER-'], values['-FILE LIST-'][0])
            window['-TOUT-'].update(filename)
            window['-IMAGE-'].update(filename=filename)

        except:
            pass

# --------------------------------- Close & Exit ---------------------------------

window.close()