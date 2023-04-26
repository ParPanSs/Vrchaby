"""Модуль работы с камнями в игре"""

# Подключение системных модулей
from tkinter import *


def create_cell_img(g_set):
    for _n in range(1, 6):
        for _i in range(0, 7):
            g_set.cell_img_xy[_n][_i] = (192 + _n * 47, 558 - _i * 44)

    for _n in range(6, 12):
        for _i in range(0, 7):
            g_set.cell_img_xy[_n][_i] = (528 + (_n - 6) * 47, 558 - _i * 44)

    for _n in range(13, 18):
        for _i in range(0, 7):
            g_set.cell_img_xy[_n][_i] = (
                g_set.gamefield_padx + 616 - (_n - 13) * 47, g_set.gamefield_pady + 32 + _i * 44)

    for _n in range(18, 24):
        for _i in range(0, 7):
            g_set.cell_img_xy[_n][_i] = (
                g_set.gamefield_padx + 328 - (_n - 18) * 47, g_set.gamefield_pady + 32 + _i * 44)

    update_cell_img(g_set)


def update_cell_img(g_set):
    """Пересчет координат картинок камней"""

    # Заполняем массив cell_img_xy фиксированными координатами для отображения
    # изображения (картинок) камня размером 45 на 43 пикселей для каждой ячейки игрового поля
    # в ужатом виде (когда кол-во камней на одной позиции превышает 6 (это
    # может быть тока на позициях 0 и 12)

    # Подсчитаем кол-во черных камней на позиции 0
    _max_stone = 0
    for _k in range(0, 15):
        if g_set.cell_stone_black[0][_k] != 0:
            _max_stone += 1

    match _max_stone:
        case 0 | 1 | 2 | 3 | 4 | 5 | 6:
            for _i in range(0, 15):
                g_set.cell_img_xy[0][_i] = (192, 558 - _i * 44)  # Нижняя левая позиция (обычно бар черных)
        case 7 | 8 | 9 | 10 | 11:
            for _i in range(0, 15):
                g_set.cell_img_xy[0][_i] = (192, 558 - _i * 22)  # Нижняя левая позиция (обычно бар черных)
        case 12 | 13 | 14 | 15:
            for _i in range(0, 15):
                g_set.cell_img_xy[0][_i] = (192, 558 - _i * 16)  # Нижняя левая позиция (обычно бар черных)

    # Подсчитаем кол-во белых камней на позиции 12
    _max_stone = 0
    for _k in range(0, 15):
        if g_set.cell_stone_white[12][_k] != 0:
            _max_stone += 1

    match _max_stone:
        case 0 | 1 | 2 | 3 | 4 | 5 | 6:
            for _i in range(0, 15):
                g_set.cell_img_xy[12][_i] = (g_set.gamefield_padx + 662,
                                             g_set.gamefield_pady + 32 + _i * 44)  # Нижняя левая позиция (обычно бар черных)
        case 7 | 8 | 9 | 10 | 11:
            for _i in range(0, 15):
                g_set.cell_img_xy[12][_i] = (g_set.gamefield_padx + 662,
                                             g_set.gamefield_pady + 32 + _i * 22)  # Нижняя левая позиция (обычно бар черных)
        case 12 | 13 | 14 | 15:
            for _i in range(0, 15):
                g_set.cell_img_xy[12][_i] = (g_set.gamefield_padx + 662,
                                             g_set.gamefield_pady + 32 + _i * 16)  # Нижняя левая позиция (обычно бар черных)


def move_stones(g_set):
    """Распределяем изображения камней по игровому полю"""

    update_cell_img(g_set)

    for _i in range(0, 24):
        for _j in range(0, 15):
            if g_set.cell_stone_black[_i][_j] != 0:
                g_set.field_canvas.coords(g_set.black_stone_xy[g_set.cell_stone_black[_i][_j] - 1],
                                          g_set.cell_img_xy[_i][_j][0],
                                          g_set.cell_img_xy[_i][_j][1])

    for _i in range(0, 24):
        for _j in range(0, 15):
            if g_set.cell_stone_white[_i][_j] != 0:
                g_set.field_canvas.coords(g_set.white_stone_xy[g_set.cell_stone_white[_i][_j] - 1],
                                          g_set.cell_img_xy[_i][_j][0],
                                          g_set.cell_img_xy[_i][_j][1])


def init_stones(g_set):
    # Формирование изображений (виджетов) всех камней на игровом поле

    global stone_fileimage_white
    global stone_fileimage_black
    stone_fileimage_white = PhotoImage(file=g_set.file_stone_white)
    stone_fileimage_black = PhotoImage(file=g_set.file_stone_black)

    create_cell_img(g_set)

    for _i in range(0, 15):
        g_set.black_stone_xy.append(
            g_set.field_canvas.create_image(g_set.cell_img_xy[0][0][0],
                                            g_set.cell_img_xy[0][0][1],
                                            image=stone_fileimage_black,
                                            anchor=NW))

    for _i in range(0, 15):
        g_set.white_stone_xy.append(
            g_set.field_canvas.create_image(g_set.cell_img_xy[0][0][0],
                                            g_set.cell_img_xy[0][0][1],
                                            image=stone_fileimage_white,
                                            anchor=NW))
