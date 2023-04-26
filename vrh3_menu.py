"""Модуль формирования главного меню и функции обработки пунктов меню"""

# Подключение системных модулей
from tkinter import *
import tkinter as tk

# Подлючение локальных модулей
from vrh3_help import *


def init_menu(g_set):

    def _ai_mark_checked(*args):
        g_set.ai = _ai_checked.get()

    def _t_game_marked(*args):
        g_set.game_with_computer = int(_t_game.get())
        if g_set.game_with_computer == 1:
            g_set.gamer1 = g_set.computer
            g_set.gamer1_name = g_set.computer_name
            g_set.gamer2 = g_set.human1
            g_set.gamer2_name = g_set.human1_name

            lbl1 = "Hra s počítačem (" + g_set.gamer1_name + " vs " + g_set.gamer2_name + ")"
            lbl2 = "Hra pro dvě osoby"
        else:
            g_set.gamer1 = g_set.human1
            g_set.gamer1_name = g_set.human1_name
            g_set.gamer2 = g_set.human2
            g_set.gamer2_name = g_set.human2_name

            lbl1 = "Hra s počítačem"
            lbl2 = "Hra pro dvě osoby (" + g_set.gamer1_name + " vs " + g_set.gamer2_name + ")"

        _settings_menu.delete(0, 1)
        _settings_menu.insert_radiobutton(0, label=lbl1, value=1, variable=_t_game)
        _settings_menu.insert_radiobutton(1, label=lbl2, value=0, variable=_t_game)
        _settings_menu.update()

    # Формирование главного меню программы
    _m_menu = Menu()

    _hra_menu = Menu()
    _hra_menu.add_command(label="Nová hra")
    _hra_menu.add_command(label="Otevřená hra")
    _hra_menu.add_command(label="Uložte hru")
    _hra_menu.add_separator()
    _hra_menu.add_command(label="Výstup", command=lambda: g_set.finish_game(g_set.window_main))
    _m_menu.add_cascade(label="Hra", menu=_hra_menu)

    _okno_menu = Menu()

    # Rozbalení okna na celou obrazovku
    _okno_menu.add_command(label="Celá obrazovka (Ctrl-F)",
                           command=lambda: g_set.window_main.attributes("-fullscreen", True))

    # Normální velikost
    _okno_menu.add_command(label="Normální velikost (Ctrl-N)",
                           command=lambda: g_set.window_main.attributes("-fullscreen", False))

    _m_menu.add_cascade(label="Okno", menu=_okno_menu)

    _settings_menu = Menu()

    _t_game = tk.StringVar()
    _t_game.set(str(g_set.game_with_computer))
    _t_game.trace("w", _t_game_marked)
    if g_set.game_with_computer == 1:
        lbl1 = "Hra s počítačem (" + g_set.gamer1_name + " vs " + g_set.gamer2_name + ")"
        lbl2 = "Hra pro dvě osoby"
    else:
        lbl1 = "Hra s počítačem"
        lbl2 = "Hra pro dvě osoby (" + g_set.gamer1_name + " vs " + g_set.gamer2_name + ")"

    _settings_menu.add_radiobutton(label=lbl1, value=1, variable=_t_game)
    _settings_menu.add_radiobutton(label=lbl2, value=0, variable=_t_game)

    _settings_menu.add_separator()

    _ai_checked = tk.BooleanVar()
    _ai_checked.set(g_set.ai)
    _ai_checked.trace("w", _ai_mark_checked)
    _settings_menu.add_checkbutton(label="Chytrá AI", onvalue=True,
                                   offvalue=False, variable=_ai_checked)

    _m_menu.add_cascade(label="Nastavení", menu=_settings_menu)

    _pomoc_menu = Menu()
    _pomoc_menu.add_command(label="Pravidla hry (F1)", command=lambda: rules(g_set))
    _pomoc_menu.add_command(label="O programu (F9)", command=lambda: about(g_set))
    _m_menu.add_cascade(label="Pomoc", menu=_pomoc_menu)

    g_set.window_main.config(menu=_m_menu)
    