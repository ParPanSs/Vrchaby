"""Функции работы с костями"""

# Подключение системных модулей
from tkinter import *
import time


def show_rolls(g_set):
    """Выводим изображения выпавших кубиков текущего игрока на информационное поле"""

    global roll_xy
    global roll_image

    roll_xy = []

    g_set.field_canvas.create_text(g_set.gamefield_padx + 800 + 20 + 100,
                                   g_set.gamefield_pady + 10,
                                   font="Arial, 12",
                                   fill="white",
                                   text=g_set.current_player_color.capitalize() + " k pohybu")

    if len(roll_xy) > 0:
        for j in range(0, 4):  # Всего 4 позиции на информационном поле
            g_set.field_canvas.delete(roll_xy[j])

    for j in range(0, 4):  # Всего 4 позиции на информационном поле
        roll_xy.append(g_set.field_canvas.create_image(j * 47 + g_set.gamefield_padx + 830,
                                                       g_set.gamefield_pady + 30,
                                                       anchor=NW,
                                                       image=roll_image[g_set.current_player_dice[j]]))


def rand(g_set) -> int:  # Функция генерации случайного числа от 1 до 6
    """Генерация случайных чисел от 1 до 6"""
    _n = 0
    while _n > 6 or _n < 1:
        g_set.rand_next = g_set.rand_next * 1103515245 + 12345
        g_set.rand_next = int((g_set.rand_next / 65536) % 32768)
        _n = g_set.rand_next - int(g_set.rand_next / 10) * 10
    return _n


def dice_rolls(g_set):

    if not (g_set.current_player_dice[0] or g_set.current_player_dice[1] or
            g_set.current_player_dice[2] or g_set.current_player_dice[3]):

        g_set.current_player_dice[0] = 1  # Блокируем повторное бросание кубиков

        # Массив ссылок на изображения кубиков
        global roll_image
        roll_image = [PhotoImage(master=g_set.window_main, file="data/roll0.png"),
                      PhotoImage(master=g_set.window_main, file="data/roll1.png"),
                      PhotoImage(master=g_set.window_main, file="data/roll2.png"),
                      PhotoImage(master=g_set.window_main, file="data/roll3.png"),
                      PhotoImage(master=g_set.window_main, file="data/roll4.png"),
                      PhotoImage(master=g_set.window_main, file="data/roll5.png"),
                      PhotoImage(master=g_set.window_main, file="data/roll6.png")]

        # Создаем картинки избображений кубиков от 1 до 6 и прячим их

        _rolls1 = []

        if g_set.current_player_color == g_set.tg.black:
            r1_x = 180 + g_set.gamefield_padx
            r2_x = r1_x + 50
            r1_y = r2_y = 270 + g_set.gamefield_pady
        else:
            r1_x = 600 + g_set.gamefield_padx
            r2_x = r1_x + 50
            r1_y = r2_y = 270 + g_set.gamefield_pady

        for _i in range(1, 7):
            _rolls1.append(g_set.field_canvas.create_image(r1_x, r1_y, anchor=NW, image=roll_image[_i]))
            g_set.field_canvas.itemconfigure(_rolls1[_i - 1], state=HIDDEN)

        _rolls2 = []
        for _i in range(1, 7):
            _rolls2.append(g_set.field_canvas.create_image(r2_x, r2_y, anchor=NW, image=roll_image[_i]))
            g_set.field_canvas.itemconfigure(_rolls2[_i - 1], state=HIDDEN)

        # Анимация кидания сразу двоих костей
        for _i in range(0, rand(g_set) + 10):
            _r1 = rand(g_set)
            _r2 = rand(g_set)
            g_set.field_canvas.itemconfigure(_rolls1[_r1 - 1], state=NORMAL)
            g_set.field_canvas.itemconfigure(_rolls2[_r2 - 1], state=NORMAL)
            g_set.field_canvas.update()
            time.sleep(g_set.dice_roll_speed)
            g_set.field_canvas.itemconfigure(_rolls1[_r1 - 1], state=HIDDEN)
            g_set.field_canvas.itemconfigure(_rolls2[_r2 - 1], state=HIDDEN)

        g_set.field_canvas.itemconfigure(_rolls1[_r1 - 1], state=NORMAL)
        g_set.field_canvas.itemconfigure(_rolls2[_r2 - 1], state=NORMAL)

        g_set.current_player_dice[0] = _r1
        g_set.current_player_dice[1] = _r2

        if _r1 == _r2:
            g_set.current_player_dice[2] = g_set.current_player_dice[3] = _r2

        show_rolls(g_set)
        _is_clicked = False
