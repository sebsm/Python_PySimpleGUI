import PySimpleGUI as sg
import numpy as np
"""
    Embedding the Matplotlib toolbar into your application
"""

# ------------------------------- This is to include a matplotlib figure in a Tkinter canvas
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


# def draw_figure_w_toolbar(canvas, fig, canvas_toolbar):
#     if canvas.children:
#         for child in canvas.winfo_children():
#             child.destroy()
#     if canvas_toolbar.children:
#         for child in canvas_toolbar.winfo_children():
#             child.destroy()
#     figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
#     figure_canvas_agg.draw()
#     toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
#     toolbar.update()
#     figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)
def draw_figure_w_toolbar(canvas, fig, canvas_toolbar):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def delete_figure_agg(figure_agg):
    figure_agg.get_tk_widget().forget()
    figure_agg.get_tk_widget().destroy()
    plt.close('all')


class Toolbar(NavigationToolbar2Tk):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)


# ------------------------------- PySimpleGUI CODE

layout_2 = [
    [sg.T('Graph: y=sin(x)')],
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

window_2_active = False
window_2 = sg.Window('Graph with controls', layout_2)

def charts_window(window_1, window_2, window_2_active):
    flag_linear = 0
    figure_agg = None
    while True:
        event_2, values_2 = window_2.read()
        print(event_2, values_2)
        
        
        if len(values_2['INPUT A']) and values_2['INPUT A'][-1] not in ('0123456789'):
            # delete last char from input
            window_2['INPUT A'].update(values_2['INPUT A'][:-1])

        if event_2 in (sg.WIN_CLOSED, 'Back'):  # always,  always give a way out!
            window_2.close()
            window_2_active = False
            window_1.UnHide()
            break
        elif event_2 == 'Plot' and values_2['SIN'] == True:
            # ------------------------------- PASTE YOUR MATPLOTLIB CODE HERE
            if figure_agg:
            # ** IMPORTANT ** Clean up previous drawing before drawing again
                delete_figure_agg(figure_agg)

            plt.figure(1)
            fig1 = plt.gcf()
            DPI = fig1.get_dpi()
            # ------------------------------- you have to play with this size to reduce the movement error when the mouse hovers over the figure, it's close to canvas size
            fig1.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
            # -------------------------------
            x = np.linspace(-4*np.pi/2, 4 * np.pi/2)
            #x = np.linspace(-10, 10)
            y = np.sin(x)
            plt.plot(x, y)
            plt.title('y=f(x)')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.grid()
            #plt.xaxis.set_major_formatter(tck.FormatStrFormatter('%g $\pi$'))
            # ------------------------------- Instead of plt.show()
            figure_agg = draw_figure_w_toolbar(window_2['fig_cv'].TKCanvas, fig1, window_2['controls_cv'].TKCanvas)
        elif event_2 == 'Plot' and values_2['COS'] == True:
            # ------------------------------- PASTE YOUR MATPLOTLIB CODE HERE
            if figure_agg:
                # ** IMPORTANT ** Clean up previous drawing before drawing again
                delete_figure_agg(figure_agg)
            plt.figure(2)
            fig2 = plt.gcf()
            DPI = fig2.get_dpi()
            # ------------------------------- you have to play with this size to reduce the movement error when the mouse hovers over the figure, it's close to canvas size
            fig2.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
            # -------------------------------
            x = np.linspace(-4*np.pi/2, 4 * np.pi/2)
            #x = np.linspace(-10, 10)
            y = np.cos(x)
            plt.plot(x, y)
            plt.title('y=f(x)')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.grid()
            
            
            # ------------------------------- Instead of plt.show()
            figure_agg = draw_figure_w_toolbar(window_2['fig_cv'].TKCanvas, fig2, window_2['controls_cv'].TKCanvas)
        elif event_2 == 'Plot' and values_2['LINEAR'] == True:
            # and values_2['INPUT A'] != None and values_2['INPUT B'] != None
            if flag_linear != 0:
                # ** IMPORTANT ** Clean up previous drawing before drawing again
                print(1)
                delete_figure_agg(figure_agg)
                #plt.figure(3, clear = True)
                #fig3 = None

            fig3 = plt.figure(3)
            fig3 = plt.gcf()
            DPI = fig3.get_dpi()
            # ------------------------------- you have to play with this size to reduce the movement error when the mouse hovers over the figure, it's close to canvas size
            fig3.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
            # -------------------------------
            x = np.linspace(-2, 2)
            #x = np.linspace(-10, 10)
            y = int((values_2['INPUT A'])) * x + int((values_2['INPUT B']))
            #y = 2*x+4
            plt.plot(x, y)
            plt.title('y=f(x)')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.grid()
            figure_agg = draw_figure_w_toolbar(window_2['fig_cv'].TKCanvas, fig3, window_2['controls_cv'].TKCanvas)
            flag_linear = 1

window_2.close()
