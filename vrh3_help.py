"""Функции обработки пунктов меню pomoc"""

# Подключение системных модулей
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
import tkinter.font as font


def about(g_set):

    def _close_window(_win):
        _win.grab_release()
        _win.destroy()

    _window = Toplevel()
    _window.title("О vrhcaby")

    # Вычисление размеров окна правил игры
    _w_width = (g_set.current_screenwidth * 25) // 100
    _w_height = (g_set.current_screenheight * 30) // 100

    # Левый верхний угол окна правил игры
    _w_topx = (g_set.current_screenwidth - _w_width) // 2
    _w_topy = (g_set.current_screenheight - _w_height) // 2

    _window.geometry("%dx%d+%d+%d" % (_w_width, _w_height, _w_topx, _w_topy))
    _window.protocol("WM_DELETE_WINDOW", lambda: _close_window(_window))  # перехватываем нажатие на крестик

    text_canvas = Canvas(_window, bg="white", width=_w_width, height=_w_height - 50)
    text_canvas.pack(anchor=NW, expand=1)

    global pic_logo
    pic_logo = PhotoImage(master=_window, file=g_set.file_logo)
    text_canvas.create_image(10, 10, anchor=NW, image=pic_logo)

    txt_about = "Программа разработана студентами группы оклоокл 2023 году как семинарская работа"
    text_canvas.create_text(100, 10, text="Vrhcaby v3.0", anchor="nw", font="Arial")
    text_canvas.create_text(10, 95, text=txt_about, anchor="nw",  width=_w_width)

    but_font = font.Font(family='Times New Roman', size=11, weight='bold')
    close_button = Button(_window, text="Ok", font=but_font, fg='blue',
                          command=lambda: _close_window(_window))
    close_button.pack(anchor="n", expand=1)

    _window.grab_set()  # захватываем пользовательский ввод


def rules(g_set):

    def _close_window(_win):
        _win.grab_release()
        _win.destroy()

    _window = Toplevel()
    _window.title("Правила игры")

    # Вычисление размеров окна правил игры
    _w_width = (g_set.current_screenwidth * 55) // 100
    _w_height = (g_set.current_screenheight * 60) // 100

    # Левый верхний угол окна правил игры
    _w_topx = (g_set.current_screenwidth - _w_width) // 2
    _w_topy = (g_set.current_screenheight - _w_height) // 2

    _window.geometry("%dx%d+%d+%d" % (_w_width, _w_height, _w_topx, _w_topy))
    _window.protocol("WM_DELETE_WINDOW", lambda: _close_window(_window))  # перехватываем нажатие на крестик

    text_canvas = Canvas(_window, bg="white", width=_w_width, height=_w_height - 50)
    text_canvas.pack(anchor=NW, expand=1)

    # Область прокрутки
    st = ScrolledText(_window, font=("Arial", 11), borderwidth=0, wrap=WORD)

    # Inserting Text from file
    st.insert('end', open(file=g_set.file_pravidla, mode='r').read())

    # Making the text read only
    st.configure(state='disabled')

    st.pack(fill=BOTH, anchor="n", side=LEFT, expand=True)

    text_canvas.create_window(10, 10, anchor=NW, window=st, width=_w_width - 20, height=_w_height - 60)

    but_font = font.Font(family='Times New Roman', size=11, weight='bold')
    close_button = Button(_window, text="Seznámil se", font=but_font, fg='blue',
                          command=lambda: _close_window(_window))
    close_button.pack(anchor="n", expand=1)

    st.focus()
    _window.grab_set()  # захватываем пользовательский ввод


