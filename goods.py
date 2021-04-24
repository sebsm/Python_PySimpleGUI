import PySimpleGUI as sg
from math import sqrt
from PySimpleGUI.PySimpleGUI import Submit, WINDOW_CLOSED
from records import *
# for i,j,k,l in every:
            #     rows = [i,j,k,l]
            #     print(rows)
                # id_row = [[(sg.Text(i,size=(15,1), pad=(0,0))) for row in range(10)]]
                # name_row = [[(sg.Text(j,size=(15,1), pad=(0,0))) for row in range(10)]]
                # value_row = [[(sg.Text(k,size=(15,1), pad=(0,0))) for row in range(10)]]
                # quantity_row = [[(sg.Text(l,size=(15,1), pad=(0,0))) for row in range(10)]]
                
            #input_rows = [[sg.Text('ok',size=(15,1), pad=(0,0)) for col in range(4)] for row in range(10)]
            # input_rows = [
            #     [(sg.Text(i,size=(15,1), pad=(0,0)),sg.Text(j,size=(15,1), pad=(0,0)),sg.Text(k,size=(15,1), pad=(0,0)),sg.Text(l,size=(15,1), pad=(0,0))) for i,j,k,l in every] for row in range(10)
            #     ]
            #input_rows = id_row + name_row + value_row + quantity_row


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
    [sg.T('Name:')], [sg.In(key ='Name_3')],
    [sg.B('Delete')]
    ]

# headings = ['ID', 'NAME', 'VALUE','QUANTITY']

# header =  [
#     [sg.T('Display records')],
#     [sg.Text('  ')] + [sg.Text(h, size=(14,1)) for h in headings]
# ]

# input_rows = [[sg.Text('  ',size=(15,1), pad=(0,0)) for col in range(4)] for row in range(10)]

# tab4_layout = header + input_rows



# layout_4 = [[sg.TabGroup([[sg.Tab('Add_t', tab1_layout), sg.Tab('Update_t', tab2_layout),sg.Tab('Delete_t', tab3_layout),sg.Tab('Show_t', tab4_layout)]])],
#             [sg.Button('Back'), sg.Button('Check the amount of records')]
# ]
#window_4 = sg.Window('Goods', layout_4)
window_4_active = False




def goods(window_1, window_4, window_4_active, cur, conn, layout_4):
    while True:
        event_4, values_4 = window_4.read()
        if event_4 in (sg.WIN_CLOSED, 'Back'):
            window_4.close()
            window_4_active = False
            window_1.UnHide()
            break
        elif event_4 == 'Add':
            try:
                SQL = "INSERT INTO goods (name, value, quantity) VALUES (%s, %s, %s);"
                data = (values_4['Name_1'], float(values_4['Value_1']), int(values_4['Quantity_1']))
                #cur.execute("INSERT INTO goods (name, value, quantity) VALUES (%s, %s, %s);",(values_4['Name_1'], float(values_4['Value_1']), int(values_4['Quantity_1'])))
                cur.execute(SQL, data)
                conn.commit()
                print('Record inserted')
            except:
                print('Failure!')
                print(values_4['Name_1'], values_4['Value_1'], values_4['Quantity_1'])
        elif event_4 == 'Update':
            try:
                SQL = "UPDATE goods SET value= %s, quantity= %s WHERE name= %s;"
                data = (float(values_4['Value_2']), int(values_4['Quantity_2']),values_4['Name_2'])
                #cur.execute("UPDATE goods SET value= %s, quantity=%s WHERE name=%s;",(float(values_4['Value_2']), int(values_4['Quantity_2']),values_4['Name_2']))
                cur.execute(SQL, data)
                conn.commit()
                print('Record updated')
            except:
                print('Failure!')
                sg.popup('Record not founded!')
                print(values_4['Name_2'], values_4['Value_2'], values_4['Quantity_2'])
        elif event_4 == 'Delete':
            try:
                SQL = "DELETE FROM goods WHERE name = (%s);"
                data = (values_4['Name_3'],)
                cur.execute(SQL, data)
                conn.commit()
                print('Record deleted')
            except:
                print('Failure!')
                sg.popup('There is no such record!')
                print(values_4['Name_3'])
        
        elif event_4 == 'Show records' and not window_5_active:
            window_4.Hide()
            cur.execute("SELECT * FROM goods;")
            every = cur.fetchall()
            ids = []
            names= []
            values = []
            quantities = []
            # print(every)
            for i,j,k,l in every:
                ids.append(i)
                names.append(j)
                values.append(k)
                quantities.append(l)

            headings = ['ID','NAME','VALUE','QUANTITY']


            
            header =  [
                [sg.T('Display records')],
                [sg.Text(h,size=(14,1), pad=(3,3)) for h in headings]
            ]

            id_row = [
                [(sg.Text(i,size=(15,1), pad=(0,0))) for i in ids]
            ]
            name_row = [
                [(sg.Text(j,size=(15,1), pad=(0,0))) for j in names]
            ]
            value_row = [
                [(sg.Text(k,size=(15,1), pad=(0,0))) for k in values]
            ]
            quantity_row = [
                [(sg.Text(l,size=(15,1), pad=(0,0))) for l in quantities]
            ]

            rows =[
                [((sg.Text(' '+ str(i),size=(15,1), pad=(0,0))),(sg.Text(' '+ str(j),size=(15,1), pad=(0,0))),(sg.Text(' '+ str(k),size=(15,1), pad=(0,0))),(sg.Text(' '+ str(l),size=(15,1), pad=(0,0)))) for i,j,k,l in every]
            ]
            
            
            input_rows = rows[0]
            tab5_layout = header + input_rows
            #,sg.Tab('Show_t', tab4_layout)
            back = [
                [sg.Button('Back'),sg.Button('Check the amount of records')]
            ]
            layout_5 = header + input_rows + back
            window_5 = sg.Window('Records', layout_5)

            show(window_4, window_5, window_5_active, cur, conn,layout_5)
    window_4.close()    
