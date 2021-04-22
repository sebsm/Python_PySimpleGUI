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

headings = ['ID', 'NAME', 'VALUE','QUANTITY']

header =  [
    [sg.T('Display records')],
    [sg.Text('  ')] + [sg.Text(h, size=(14,1)) for h in headings]
]

input_rows = [[sg.Text('  ',size=(15,1), pad=(0,0)) for col in range(4)] for row in range(10)]

tab4_layout = header + input_rows



layout_4 = [[sg.TabGroup([[sg.Tab('Add_t', tab1_layout), sg.Tab('Update_t', tab2_layout),sg.Tab('Delete_t', tab3_layout),sg.Tab('Show_t', tab4_layout)]])],
            [sg.Button('Back'), sg.Button('Check the amount of records')]
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
        elif event_4 == 'Check the amount of records':
            try:
                cur.execute("SELECT COUNT(*) FROM goods;")
                count = cur.fetchone()
                conn.commit()
                print(count[0])
                # cur.execute("SELECT * FROM goods;")
                # every = cur.fetchall()
                # print(every)
                # for i,j,k,l in every:
                #     print(i)
                #     print(j)
                #     print(k)
                #     print(l)
                # for i in range(len(every)):
                #     for j in range(len(every)):
                #         print(every[i][j])
            except:
                print('Failure!')
                sg.popup('Incorrect query')

        
window_4.close()