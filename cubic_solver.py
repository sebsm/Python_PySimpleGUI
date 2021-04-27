import PySimpleGUI as sg
from math import sqrt
from cmath import phase
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED

def cub_solver(a,b,c,d):
    # p=(-b)/(3*a)
    # q = (p**3) + (b*c-3*a*d)/(6*a**2)
    # r = c/(3*a)
    # x = (q + (q**2 + (r-p**2)**3)**(1/2))**(1/3) + (q - (q**2 + (r-p**2)**3)**(1/2))**(1/3) + p
    # return x
    Q = ((3*a*c) - (b**2))/(9*a**2)
    #print(Q)
    R = ((9*a*b*c) - (27*a**2*d) - (2*b**3))/(54*a**3)
    #print(R)
    S = (R + (Q**3 + R**2)**(1/2))**(1/3)
    #print(S)
    #print(((-35+15*sqrt(6))**(1/3))/3)
    T = (R - (Q**3 + R**2)**(1/2))**(1/3)
    print('First T\n')
    print(-abs(T))
    T = -abs(T)
    print('Second T\n')
    print(-((35+15*sqrt(6))**(1/3))/3)
    x1  = S + T - b/(3*a)
    x2 = -(S+T)/2 -b/(3*a) + 1j*sqrt(3)/(2) * (S-T) 
    x3 = -(S+T)/2 -b/(3*a) - 1j*sqrt(3)/(2) * (S-T) 
    return x1,x2,x3

layout_6 = [
    [sg.T('a', key='lbl_a',font='consalo 14'), sg.I('', key='edit_a', size=(10,1),pad=(10,10)),
    sg.T('b', key='lbl_b', font='consalo 14'), sg.I('', key='edit_b', size=(10,1),pad=(10,10)),
    sg.T('c', key='lbl_c', font='consalo 14'), sg.I('', key='edit_c', size=(10,1),pad=(10,10)),
    sg.T('d', key='lbl_d', font='consalo 14'), sg.I('', key='edit_d', size=(10,1),pad=(10,10))],
    [sg.B('Calculate', key='calc', border_width=5, pad=(10,10))],
    [sg.T('x1', key='lbl_x1', font='consalo 14'), sg.I('', key='x1', size=(50,1),pad=(10,10))],
    [sg.T('x2', key='lbl_x2', font='consalo 14'), sg.I('', key='x2', size=(50,1),pad=(10,10))],
    [sg.T('x3', key='lbl_x3', font='consalo 14'), sg.I('', key='x3', size=(50,1),pad=(10,10))],
    [sg.B('Back')]
  ]
window_6_active = False
window_6 = sg.Window('Cubic solver', layout_6)

def cubic_solver(window_1, window_6, window_6_active):
    while True:
        event_6, values_6 = window_6.read()
        if event_6 in (sg.WIN_CLOSED, 'Back'):
            window_6.close()
            window_6_active = False
            window_1.UnHide()
            break
        if event_6 == 'calc':
            try:
                a = float(values_6['edit_a'])
            except:
                a = 0
                sg.popup_error("The leading coefficient cannot be zero")
                break
            try:
                b = float(values_6['edit_b'])
            except:
                b = 0
            try:
                c = float(values_6['edit_c'])
            except:
                c = 0
            try:
                d = float(values_6['edit_d'])
            except:
                d = 0
            
            # x1,x2,x3 = cubic_solver(a,b,c,d)
            # window_6['x1'].update(str(x1))
            # window_6['x2'].update(str(x2))
            # window_6['x3'].update(str(x3))
            x1,x2,x3 = cub_solver(a,b,c,d)
            window_6['x1'].update(str(x1))
            window_6['x2'].update(str(x2))
            window_6['x3'].update(str(x3))
            # x = cub_solver(a,b,c,d)
            # window_6['x1'].update(str(x))
            # print(x)
window_6.close()