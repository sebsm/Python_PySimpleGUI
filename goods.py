import PySimpleGUI as sg
from math import sqrt
from PySimpleGUI.PySimpleGUI import Submit, WINDOW_CLOSED

tab1_layout = [
    [sg.T('Add item')],
    [sg.T('Name:')], [sg.In(key = 'Name_1')],
    [sg.T('Value:')], [sg.In(key = 'Value_1')],
    [sg.T('Quantity:')], [sg.In(key = 'Quantity_1')],
    [sg.B('Add')]
]

tab2_layout = [
    [sg.T('Update item')],
    [sg.T('Name:')], [sg.In(key = 'Name_2')],
    [sg.T('Value:')], [sg.In(key = 'Value_2')],
    [sg.T('Quantity:')], [sg.In(key = 'Quantity_2')],
    [sg.B('Update')]
    ]
tab3_layout = [
    [sg.T('Delete item')],
    [sg.T('Name:')], [sg.In(key = 'Name_3')],
    [sg.B('Delete')]
    ]
tab4_layout = [
    [sg.T('Display records')],
    [sg.T('Name:')], [sg.In(key = 'Name_3')],
    [sg.B('Delete')]
    ]

layout_4 = [[sg.TabGroup([[sg.Tab('Add', tab1_layout), sg.Tab('Update', tab2_layout),sg.Tab('Delete', tab3_layout)]])],
            [sg.Button('Back')]
]
window_4_active = False

window_4 = sg.Window('Goods', layout_4)


def goods(window_1, window_4, window_4_active, cur, conn):
    while True:
        event_4, values_4 = window_4.read()
        if event_4 in (sg.WIN_CLOSED, 'Back'):
            window_4.close()
            window_4_active = False
            window_1.UnHide()
            break
        elif event_4 == 'Add':
            try:
                cur.execute("INSERT INTO goods (name, value, quantity) VALUES (%s, %s, %s);",(values_4['Name_1'], float(values_4['Value_1']), int(values_4['Quantity_1'])))
                conn.commit()
                print('Record inserted')
            except:
                print('Failure!')
                print(values_4['Name_1'], values_4['Value_1'], values_4['Quantity_1'])
        elif event_4 == 'Update':
            try:
                cur.execute("UPDATE goods SET value=%s, quantity=%s WHERE name=%s;",(float(values_4['Value_2']), int(values_4['Quantity_2']),values_4['Name_2']))
                conn.commit()
                print('Record updated')
            except:
                print('Failure!')
                sg.popup('Record not founded!')
                print(values_4['Name_2'], values_4['Value_2'], values_4['Quantity_2'])
        elif event_4 == 'Delete':
            try:
                cur.execute("DELETE FROM goods WHERE name=%s;",(values_4['Name_1']))
                conn.commit()
                print('Record deleted')
            except:
                print('Failure!')
                sg.popup('There is no such record!')
                print(values_4['Name_3'])
window_4.close()