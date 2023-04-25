"""Модуль обработки событий нажатий клавиш и клацанья мышкой"""

# Подключение системных модулей
from tkinter import *

# Подлючение локальных модулей
from vrh3_help import *
from vrh3_rolls import *


# Формирование всплывающего меню программы
def _popup_menu(event):
    p_menu = Menu()
    p_menu.add_command(label="Бросить камни")
    p_menu.add_command(label="Отменить ход")
    p_menu.add_separator()
    p_menu.add_command(label="Закончить игру")

    p_menu.post(event.x, event.y)


def point_first(g):
    global p_first
    global pf1
    p_first = PhotoImage(master=g.window_main, file="data/point_red.png")

    if g.current_player == g.tg.human1:
        if g.current_player_color == g.tg.white:
            # Текущий игрок human1 играет белыми камнями
            # Есть ли на выбранной позиции белые камни?
            if g.click_first >= 0:
                for _i in range(14, -1, -1):
                    if g.cell_stone_white[g.click_first][_i] != 0:
                        pf1 = g.field_canvas.create_image(g.point_coords[g.click_first][0],
                                                          g.point_coords[g.click_first][1],
                                                          anchor=NW, image=p_first)
                        return True
                    else:
                        return False
            else:
                g.field_canvas.delete(pf1)

        else:
            # Текущий игрок human1 играет чёрными камнями
            # Есть ли на выбранной позиции чёрные камни?
            if g.click_first >= 0:
                for _i in range(14, -1, -1):
                    if g.cell_stone_black[g.click_first][_i] != 0:
                        pf1 = g.field_canvas.create_image(g.point_coords[g.click_first][0],
                                                          g.point_coords[g.click_first][1],
                                                          anchor=NW, image=p_first)
                        return True
                    else:
                        return False
            else:
                g.field_canvas.delete(pf1)

    elif g.current_player == g.tg.human2:
        if g.current_player_color == g.tg.white:
            # Текущий игрок human2 играет белыми камнями
            # Есть ли на выбранной позиции белые камни?
            if g.click_first >= 0:
                for _i in range(14, -1, -1):
                    if g.cell_stone_white[g.click_first][_i] != 0:
                        pf1 = g.field_canvas.create_image(g.point_coords[g.click_first][0],
                                                          g.point_coords[g.click_first][1],
                                                          anchor=NW, image=p_first)
                        return True
                    else:
                        return False
            else:
                g.field_canvas.delete(pf1)

        else:
            # Текущий игрок human2 играет чёрными камнями
            # Есть ли на выбранной позиции чёрные камни?
            if g.click_first >= 0:
                for _i in range(14, -1, -1):
                    if g.cell_stone_black[g.click_first][_i] != 0:
                        pf1 = g.field_canvas.create_image(g.point_coords[g.click_first][0],
                                                          g.point_coords[g.click_first][1],
                                                          anchor=NW, image=p_first)
                        return True
                    else:
                        return False
            else:
                g.field_canvas.delete(pf1)

    else:
        pass


def point_second_variants(g):
    """Показать все возможные ходы"""

    if g.current_player == g.tg.human1:
        if g.current_player_color == g.tg.white:
            pass
        else:
            # Проверяем
            pass
    elif g.current_player == g.tg.human2:
        if g.current_player_color == g.tg.white:
            pass
        else:
            pass
    else:
        pass


def _mouse_left_click(event, g):
    # Область на игровом поле в центре (кубик) и на информационном поле вверху в рамке
    # для выпавших кубиков текущего игрока
    if (((g.gamefield_padx + 800 // 2 - 50 < event.x < g.gamefield_padx + 800 // 2 + 50) and
         (g.gamefield_pady + 585 // 2 - 50 < event.y < g.gamefield_pady + 585 // 2 + 50)) or
            ((g.gamefield_padx + 800 + 10 < event.x < g.gamefield_padx + 800 + 220) and
             (g.gamefield_pady + 10 < event.y < g.gamefield_pady + 80))):
        dice_rolls(g)

    _position = -1
    # Область на игровом поле в позиции 0
    # (условный прямоугольник от границы поля до острой стрелы)
    if ((g.gamefield_padx + 90 < event.x < g.gamefield_padx + 130) and
            (g.gamefield_pady + 585 // 2 - 10 < event.y < g.gamefield_pady + 550)):
        _position = 0

    # Область на игровом поле в позиции 1
    if ((g.gamefield_padx + 90 + 40 < event.x < g.gamefield_padx + 130 + 40) and
            (g.gamefield_pady + 585 // 2 - 10 < event.y < g.gamefield_pady + 550)):
        _position = 1

    if _position >= 0:
        if g.click_first < 0:
            g.click_first = _position
            point_first(g)
            point_second_variants(g)
        elif g.click_first == _position:
            g.click_first = -1
            point_first(g)
            point_second_variants(g)
        else:
            g.click_first = -1
            point_first(g)
            point_second_variants(g)
            g.click_second = _position



def init_bind(g_set):
    # привязка события к окну программы

    g_set.window_main.bind("<KeyPress-F1>", lambda event: rules(g_set))
    g_set.window_main.bind("<KeyPress-F9>", lambda event: about(g_set))
    # win.bind("<Control-f>", okno_full)
    # win.bind("<Control-F>", okno_full)
    # win.bind("<Control-n>", okno_normall)
    # win.bind("<Control-N>", okno_normall)
    # win.bind("<Escape>", okno_normall)

    g_set.window_main.bind("<Button-1>", lambda event: _mouse_left_click(event, g_set))
    g_set.window_main.bind("<Button-3>", _popup_menu)  # Вызов всплывающего меню
