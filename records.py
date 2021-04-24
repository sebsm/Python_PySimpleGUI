import PySimpleGUI as sg
from math import sqrt
from PySimpleGUI.PySimpleGUI import Submit, WINDOW_CLOSED

window_5_active = False

def show(window_4, window_5, window_5_active, cur, conn, layout_5):
    while True:
        event_5, values_5 = window_5.read()
        if event_5 in (sg.WIN_CLOSED, 'Back'):
            window_5.close()
            window_5_active = False
            window_4.UnHide()
            break
        elif event_5 == 'Check the amount of records':
            try:
                cur.execute("SELECT COUNT(*) FROM goods;")
                count = cur.fetchone()
                conn.commit()
                print(count[0])
                sg.popup(('Number of records:',count[0])) 
            except:
                print('Failure!')
                sg.popup('Incorrect query')