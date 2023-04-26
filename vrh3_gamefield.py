# Подключение системных модулей
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
import tkinter.font as font
import time

# Подключение локальных модулей
from vrh3_settings import *
from vrh3_menu import *
from vrh3_bind import *
from vrh3_stones import *


class GameField:
    """Игровое поле игры"""

    class TypeGamer:
        """Определение кодов для типов Игроков и их атрибутов"""

        unknown = 0
        computer = 1  # Компьютер или ИИ
        human1 = 2  #
        human2 = 3  #

        black = "černá"
        white = "bílý"

        computer_name = "Počítač"
        human1_name = "Člověk 1"
        human2_name = "Člověk 2"

    # Константы
    dice_roll_speed = 0.1  # Скорость кручения кубиков в секундах
    window_roll_speed = 0.1  # Скорость движения окна с кубиками в секундах
    pause_roll = 2  # Пауза перед движением окна с кубиками в секундах

    # Пути к файлам
    file_settings = "vrh3_set.json"  # Файл с сохраняемыми настройками игры

    file_ico = "data/vrhcaby.ico"  # Иконка для программы
    file_logo = "data/logo.png"  # Логотип программы
    file_stone_white = "data/stone_white.png"
    file_stone_black = "data/stone_black.png"

    file_pravidla = "data/pravidla.txt"  # Текстовый файл с правилами игры

    # ===============================================================================
    # Определение методов класса
    # ===============================================================================

    def finish_game(self, win):
        """Сохранение параметров игры и закрытие программы"""

        if not save_settings(self):
            showinfo(title="Уведомление", message="Невозможно сохранить установки игры !")

        win.destroy()  # Закрытие главного окна и всего приложения

    # ===============================================================================
    # Инициализация динамических объектов класса
    # ===============================================================================

    def __init__(self):

        self.tg = self.TypeGamer()

        # Установки главного меню
        self.game_with_computer = 1  # (1 - игра с компьютером)
        self.ai = False  # (True - Компьютерный интелект включен)

        # Настройка игроков
        self.gamer1 = self.tg.computer  # Игрок 1 типа TypeGamer.Computer
        self.gamer1_stone_color = self.tg.black  # Цвет камней Игрока 1 = black
        self.gamer1_name = self.tg.computer_name  # Имя Игрока 1
        self.gamer2 = self.tg.human1  # Игрок 2 TypeGamer.Human1
        self.gamer2_stone_color = self.tg.white  # Цвет камней Игрока 2 = white
        self.gamer2_name = self.tg.human1_name  # Имя Игрока 2
        self.rand_next = 21345  # Начальное значение для rand()

        # Текущий игрок и его атрибуты
        self.current_player = self.tg.unknown  # Текущий игрок
        self.current_player_color = self.tg.black
        self.current_player_dice = [0, 0, 0, 0]  # Выпавшие кубики текущего игрока
        self.click_first = -1
        self.click_second = -1

        # УСТАНОВКИ ДЛЯ ГРАФИКИ
        self.current_screenwidth = 0  # Ширина экранной области игры
        self.current_screenheight = 0  # Высота экранной области игры
        self.gamefield_padx = 100  # Смещение изображения игрового поля по x
        self.gamefield_pady = 50  # Смещение изображения игрового поля по y

        self.black_stone_xy = []
        self.white_stone_xy = []

        self.point_coords = [(self.gamefield_padx + 109, self.gamefield_pady + 566),
                             (self.gamefield_padx + 157, self.gamefield_pady + 566)]

        # =====================================================================================

        # Рассположение ячеек на игровом поле
        #
        # (23,0)-(22,0)-(21,0)-(20,0)-(19,0)-(18,0)-|-(17,0)-(16,0)-(15,0)-(14,0)-(13,0)-(12,0)
        # (23,1)-(22,1)-(21,1)-(20,1)-(19,1)-(18,1)-|-(17,1)-(16,1)-(15,1)-(14,1)-(13,1)-(12,1)
        # (23,2)-(22,2)-(21,2)-(20,2)-(19,2)-(18,2)-|-(17,2)-(16,2)-(15,2)-(14,2)-(13,2)-(12,2)
        # .....................................................................................
        # (23,14)-(22,14)-(21,14)-(20,14)-(19,14)-(18,14)-|-(17,14)-(16,14)-(15,14)-(14,14)-(13,14)-(12,14)
        # -------------------------------------------------------------------------------------
        # (0,14)-(1,14)-(2,14)-(3,14)-(4,14)-(5,14)-|-(6,14)-(7,14)-(8,14)-(9,14)-(10,14)-(11,14)
        # .....................................................................................
        # (0,2)-(1,2)-(2,2)-(3,2)-(4,2)-(5,2)-|-(6,2)-(7,2)-(8,2)-(9,2)-(10,2)-(11,2)
        # (0,1)-(1,1)-(2,1)-(3,1)-(4,1)-(5,1)-|-(6,1)-(7,1)-(8,1)-(9,1)-(10,1)-(11,1)
        # (0,2)-(1,2)-(2,2)-(3,0)-(4,0)-(5,0)-|-(6,0)-(7,0)-(8,0)-(9,0)-(10,0)-(11,0)
        #

        # Создаем двумерный массив расположения чёрных камней на игровом поле

        self.cell_stone_black = []
        for j in range(0, 24):  # Всего 24 ячеек на поле
            _arr = []
            for i in range(0, 15):  # Максимум 15 камней на ячейку
                _arr.append(0)  # Заполняем ячейки нулями (0 - камней нет)
            self.cell_stone_black.append(_arr)

        # Создаем двумерный массив расположения белых камней на игровом поле

        self.cell_stone_white = []
        for j in range(0, 24):  # Всего 24 ячеек на поле
            _arr = []
            for i in range(0, 15):  # Максимум 15 камней на ячейку
                _arr.append(0)  # Заполняем ячейки нулями (0 - камней нет)
            self.cell_stone_white.append(_arr)

        # Создаем двумерный массив (cell_img_xy) координат ячеек на игровом поле для
        # сопоставления изображений (картинок) камней с их позициями на игровом поле.
        # Рассположение ячеек на игровом поле (левый нижний угол 0,0):
        # Первый индекс массива - это номер позиции (от 0 до 23),
        # а второй - глубина вложения камней на позиции (0 до 14)
        #
        # (23,0)-(22,0)-(21,0)-(20,0)-(19,0)-(18,0)-|-(17,0)-(16,0)-(15,0)-(14,0)-(13,0)-(12,0)
        # (23,1)-(22,1)-(21,1)-(20,1)-(19,1)-(18,1)-|-(17,1)-(16,1)-(15,1)-(14,1)-(13,1)-(12,1)
        # (23,2)-(22,2)-(21,2)-(20,2)-(19,2)-(18,2)-|-(17,2)-(16,2)-(15,2)-(14,2)-(13,2)-(12,2)
        # .....................................................................................
        # (23,14)-(22,14)-(21,14)-(20,14)-(19,14)-(18,14)-|-(17,14)-(16,14)-(15,14)-(14,14)-(13,14)-(12,14)
        # -------------------------------------------------------------------------------------
        # (0,14)-(1,14)-(2,14)-(3,14)-(4,14)-(5,14)-|-(6,14)-(7,14)-(8,14)-(9,14)-(10,14)-(11,14)
        # .....................................................................................
        # (0,2)-(1,2)-(2,2)-(3,2)-(4,2)-(5,2)-|-(6,2)-(7,2)-(8,2)-(9,2)-(10,2)-(11,2)
        # (0,1)-(1,1)-(2,1)-(3,1)-(4,1)-(5,1)-|-(6,1)-(7,1)-(8,1)-(9,1)-(10,1)-(11,1)
        # (0,2)-(1,2)-(2,2)-(3,0)-(4,0)-(5,0)-|-(6,0)-(7,0)-(8,0)-(9,0)-(10,0)-(11,0)
        #

        self.cell_img_xy = []
        for j in range(0, 24):  # Всего 24 позиций на поле
            _arr = []
            for i in range(0, 15):  # Максимум 15 камней на позицию
                _arr.append(0)  # Заполняем ячейки нулями
            self.cell_img_xy.append(_arr)

        # Формируем бар черных камней с номерами от 15 до 1,
        # При этом номер камня 15 в самом начале этого массива,
        # в позиции 0 на игровом поле

        for _i in range(0, 15):
            self.cell_stone_black[0][_i] = 15 - _i

        # Формируем бар белых камней с номерами от 15 до 1,
        # При этом номер камня 15 в самом начале этого массива,
        # в позиции 12 на игровом поле

        for _i in range(0, 15):
            self.cell_stone_white[12][_i] = 15 - _i

        # ============================================================================
        # Формирование главного окна программы
        # ============================================================================

        self.window_main = Tk()
        self.window_main.title("Dlouhý vrhcaby (seminární práce KI/(K)APR2 LS 2023)")

        # Vypněte tečkovanou čáru v nabídce (отключает возможность открепления подменю)
        self.window_main.option_add("*tearOff", False)

        # Развернуть окно на весь экран
        self.window_main.state("zoomed")

        # Перехват процедуры закрытия окна
        self.window_main.protocol("WM_DELETE_WINDOW", lambda: self.finish_game(self.window_main))

        self.window_main.iconbitmap(default=self.file_ico)
        self.current_screenwidth = self.window_main.winfo_screenwidth()
        self.current_screenheight = self.window_main.winfo_screenheight()
        self.window_main.geometry("%dx%d" % (self.current_screenwidth,
                                             self.current_screenheight))

        self.field_canvas = Canvas(self.window_main, bg="#36100f", width=self.current_screenwidth,
                                   height=self.current_screenheight)
        self.field_canvas.pack(anchor=NW, expand=1)

        # Формируем игровое поле игры
        global _field_image
        _field_image = PhotoImage(file="data/gamefield800_585.png")
        _gamefield_x = self.gamefield_padx + self.current_screenwidth % 2 - 800 % 2
        _gamefield_y = self.gamefield_pady + self.current_screenheight % 2 - 585 % 2
        self.field_canvas.create_image(_gamefield_x, _gamefield_y, anchor=NW, image=_field_image)

        # Формируем информационное поле игры (справа от игрового поля)

        self.field_canvas.create_rectangle(self.gamefield_padx + 800 + 20,
                                           self.gamefield_pady + 20,
                                           self.gamefield_padx + 800 + 20 + 200,
                                           self.gamefield_pady + 20 + 60,
                                           fill="#36100f", outline="white")

        load_settings(self)  # Загружаем значения объектов класса из файла установок
        init_menu(self)  # Инициализируем главное меню программы
        init_stones(self)  # Инициализируем расположение камней на игровом поле
        init_bind(self)  # Инициализация системы событий
        move_stones(self)
        # ==================================================================================
