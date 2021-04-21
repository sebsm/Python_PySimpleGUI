import PySimpleGUI as sg

layout  = [[sg.Text(f'{i}. '), sg.In(key=i)] for i in range(1,6)] + [[sg.Button('Save'), sg.Button('Exit')]]

window = sg.Window('To Do List Example', layout)

event, values = window.read()