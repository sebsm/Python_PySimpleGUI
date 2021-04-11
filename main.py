
from charts import charts_window
import PySimpleGUI as sg
import os.path
from charts import *
# Amber theme
sg.theme('DarkAmber')
# First the window layout in 2 columns

file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 2), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
    [
        sg.Button('Exit'),sg.Button('Charts'), sg.Button('Windows 2 Status')
    ]
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("Choose an image from list on left:")],
    [sg.Text(size=(30, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

# ----- Full layout -----
layout_1 = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]



window_1 = sg.Window("Drawing Charts and Applying Functions", layout_1)


# Run the Event Loop
while True:
    event_1, values_1 = window_1.read()
    if (event_1 == "Exit" or event_1 == sg.WIN_CLOSE_ATTEMPTED_EVENT) and sg.popup_yes_no('Do you really want to quit?') == 'Yes':
        break
    # Folder name was filled in, make a list of files in the folder
    
    if event_1 == "Charts" and not window_2_active:
        #window_2_active = True
        window_1.Hide()
        layout_2 = [
            [sg.T('Graph')],
            [sg.T('Choose the type of chart:'),sg.Radio('Sine', 'RADIO1', key='SIN',size=(10,1)),sg.Radio('Cosine', "RADIO1", key = 'COS', size=(10,1)),sg.Radio('Linear', "RADIO1", key = 'LINEAR', size=(10,1))],
            [sg.T('A:'),sg.Input('', enable_events= True, key='INPUT A')], [sg.T('B:'),sg.Input('', enable_events= True, key='INPUT B')],
            #sg.T('Y:'),sg.Input('Enter the value', enable_events= True, key='INPUT Y')],
            #[sg.T('Equation:'),sg.Input('Enter the equation', enable_events= True, key='EQUATION')],
            [sg.B('Plot'), sg.B('Back')],
            [sg.T('Controls:')],
            [sg.Canvas(key='controls_cv')],
            [sg.T('Figure:')],
            [sg.Column(
                layout=[
                    [sg.Canvas(key='fig_cv',
                            # it's important that you set this size
                            size=(400 * 2, 400)
                            )]
                ],
                background_color='#DAE0E6',
                pad=(0, 0)
            )],
            [sg.B('Alive?')]

        ]
        window_2 = sg.Window('Chart', layout_2)
        
        charts_window(window_1, window_2, window_2_active)
    elif event_1 == "-FOLDER-":
        folder = values_1["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window_1["-FILE LIST-"].update(fnames)
    elif event_1 == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values_1["-FOLDER-"], values_1["-FILE LIST-"][0]
            )
            window_1["-TOUT-"].update(filename)
            window_1["-IMAGE-"].update(filename=filename)

        except:
            pass
    # elif event_1 == 'Windows 2 Status':
    #     print(window_2_active)

window_1.close()