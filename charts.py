import PySimpleGUI as sg
import numpy as np
"""
    Embedding the Matplotlib toolbar into your application
"""

# ------------------------------- This is to include a matplotlib figure in a Tkinter canvas
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


def draw_figure_w_toolbar(canvas, fig, canvas_toolbar):
    if canvas.children:
        for child in canvas.winfo_children():
            child.destroy()
    if canvas_toolbar.children:
        for child in canvas_toolbar.winfo_children():
            child.destroy()
    figure_canvas_agg = FigureCanvasTkAgg(fig, master=canvas)
    figure_canvas_agg.draw()
    toolbar = Toolbar(figure_canvas_agg, canvas_toolbar)
    toolbar.update()
    figure_canvas_agg.get_tk_widget().pack(side='right', fill='both', expand=1)


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
    
    while True:
        event_2, values_2 = window_2.read()
        print(event_2, values_2)
        if event_2 in (sg.WIN_CLOSED, 'Back'):  # always,  always give a way out!
            window_2.close()
            window_2_active = False
            window_1.UnHide()
            break
        elif event_2 == 'Plot':
            # ------------------------------- PASTE YOUR MATPLOTLIB CODE HERE
            plt.figure(1)
            fig = plt.gcf()
            DPI = fig.get_dpi()
            # ------------------------------- you have to play with this size to reduce the movement error when the mouse hovers over the figure, it's close to canvas size
            fig.set_size_inches(404 * 2 / float(DPI), 404 / float(DPI))
            # -------------------------------
            x = np.linspace(0, 2 * np.pi)
            y = np.sin(x)
            plt.plot(x, y)
            plt.title('y=sin(x)')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.grid()

            # ------------------------------- Instead of plt.show()
            draw_figure_w_toolbar(window_2['fig_cv'].TKCanvas, fig, window_2['controls_cv'].TKCanvas)

window_2.close()
