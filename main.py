
from charts import charts_window
import PySimpleGUI as sg
import os.path
from charts import *
from quadratic_solver import *
import psycopg2
from goods import *
# Amber theme
sg.theme('DarkAmber')
# First the window layout in 2 columns
if __name__=="__main__":
    try:
        conn = psycopg2.connect(
        dbname="APP",
        host="localhost",
        user="postgres",
        password = 's197328645S!'    
        )
        print('Success!')
    except:
        print('Cannot connect to databse') 

    cur = conn.cursor()

    # Database init
    try:
        cur.execute("CREATE TABLE IF NOT EXISTS  goods (id serial NOT NULL, PRIMARY KEY (id), name text, value numeric(4,2), quantity integer);")
        #cur.execute("INSERT INTO goods (name, value, quantity) VALUES ('Apple', 15.5, 10);")
        conn.commit()
        print('Table created')
    except:
        print('Failure!')
    
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
            sg.Button('Exit'),sg.Button('Charts'),sg.Button('Solver'),sg.Button('Item management')
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
        elif event_1 == 'Solver' and not window_3_active:
            window_1.Hide()
            layout_3 = [
                [sg.T('a', key='lbl_a',font='consalo 14'), sg.I('', key='edit_a', size=(10,1),pad=(10,10)),
                sg.T('b', key='lbl_b', font='consalo 14'), sg.I('', key='edit_b', size=(10,1),pad=(10,10)),
                sg.T('c', key='lbl_c', font='consalo 14'), sg.I('', key='edit_c', size=(10,1),pad=(10,10))],
                [sg.B('Calculate', key='calc', border_width=5, pad=(10,10))],
                [sg.T('x1', key='lbl_x1', font='consalo 14'), sg.I('', key='x1', size=(15,1),pad=(10,10))],
                [sg.T('x2', key='lbl_x2', font='consalo 14'), sg.I('', key='x2', size=(15,1),pad=(10,10))],
                [sg.B('Back')],
            ]
            window_3 = sg.Window('Solver', layout_3)

            solver(window_1, window_3, window_3_active)

        elif event_1 == 'Item management' and not window_4_active:
            window_1.Hide()

            tab1_layout = [
                [sg.T('Add item')],
                [sg.T('Name:')], [sg.In(key = 'Name_1')],
                [sg.T('Value:')], [sg.In(key = 'Value_1')],
                [sg.T('Quantity:')], [sg.In(key = 'Quantity_1')],
                [sg.B('Add')]]
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
            
            input_rows = rows[0]
            tab4_layout = header + input_rows
            layout_4 = [[sg.TabGroup([[sg.Tab('Add_t', tab1_layout), sg.Tab('Update_t', tab2_layout),sg.Tab('Delete_t', tab3_layout),sg.Tab('Show_t', tab4_layout)]])],
                        [sg.Button('Back'),sg.Button('Check the amount of records')]
            ]
            window_4 = sg.Window('Item management', layout_4)

            goods(window_1, window_4, window_4_active, cur, conn)

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

    window_1.close()