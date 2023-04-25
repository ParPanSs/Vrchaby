"""Функции сохранения и считывания установок игры"""
import json


def load_settings(g_set) -> bool:
    """Функция чтения установок программы"""

    try:
        fp = open(g_set.file_settings, "rt")  # открыть текстовый файл только для чтения
    except FileNotFoundError:  # Если файла установок не существует, то
        if save_settings(g_set):  # создаем его используя функцию записи
            return True
        else:
            return False  # Если не удалось создать файл установок

    _sett = json.load(fp)  # Считываем из файла установок данные в формате json

    # Парсинг считанной информации из файла установок
    # и заполнение объектов класса GameField
    _menu_set = False  # Раздел установок главного меню программы
    _game_field = False  # Раздел установок игрового поля

    for _i in _sett:

        if _menu_set:  # Заполняем установки объектов меню класса GameField
            _menu_set = False
            for _k in _i:
                if _k == 'Game_with_computer':
                    g_set.game_with_computer = _i[_k]
                if _k == 'AI':
                    g_set.ai = _i[_k]

        if _game_field:  # Заполняем объекты установок игры класса GameField
            _game_field = False
            for _k in _i:

                # установки игрока 1
                if _k == 'Gamer1':
                    g_set.gamer1 = _i[_k]
                if _k == 'Gamer1_stone_color':
                    g_set.gamer1_stone_color = _i[_k]
                if _k == 'Gamer1_name':
                    g_set.gamer1_name = _i[_k]

                # установки игрока 2
                if _k == 'Gamer2':
                    g_set.gamer2 = _i[_k]
                if _k == 'Gamer2_stone_color':
                    g_set.gamer2_stone_color = _i[_k]
                if _k == 'Gamer2_name':
                    g_set.gamer2_name = _i[_k]

                # установки текущего игрока
                if _k == 'Gamer_current':
                    g_set.current_player = _i[_k]
                if _k == 'Gamer_current_color':
                    g_set.current_player_color = _i[_k]
                if _k == 'Gamer_current_dice':
                    g_set.current_player_dice = _i[_k]

                # Переменная для функции генерации случайного числа rand()
                if _k == 'RandNext':
                    g_set.rand_next = _i[_k]

        if _i == 'Menu':  # Находим раздел "Menu"
            _menu_set = True
            _game_field = False

        if _i == 'GameField':  # Находим раздел "GameField"
            _menu_set = False
            _game_field = True

    fp.close()
    return True


def save_settings(g_set) -> bool:
    """Функция записи настроек программы"""

    fp = open(g_set.file_settings, "wt")   # открыть текстовый файл только для записи

    g_set.current_player_dice = [0,0,0,0]

    json.dump(['Menu', {'Game_with_computer': g_set.game_with_computer,
                        'AI': g_set.ai
                        },
               'GameField', {'Gamer1': g_set.gamer1,
                             'Gamer1_stone_color': g_set.gamer1_stone_color,
                             'Gamer1_name': g_set.gamer1_name,
                             'Gamer2': g_set.gamer2,
                             'Gamer2_stone_color': g_set.gamer2_stone_color,
                             'Gamer2_name': g_set.gamer2_name,
                             'Gamer_current': g_set.current_player,
                             'Gamer_current_color': g_set.current_player_color,
                             'Gamer_current_dice': g_set.current_player_dice,
                             'RandNext': g_set.rand_next}],
              fp, indent=4)

    fp.close()
    return True
