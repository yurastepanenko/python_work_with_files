import tkinter as tk
from tkinter import ttk, END, NW, X
from presenter import btn_exit
from presenter import add_files, remove_file, save_files, select_encoded_file, select_info_file, decode_files
from models import *


def on_window_close(parent_window, child_window):
    """
    функция которая при закрытии через крестик - восстановит основное окно программы
    :param parent_window: основное окно программы
    :param child_window: дочерннее окно программы
    :return:
    """
    parent_window.deiconify()  # Восстанавливаем основное окно
    child_window.destroy()  # Уничтожаем дочернее окно


def get_sizes_custom_window(custom_window):
    """
    функция для работы с координатами окон
    :param custom_window: окно для изменения
    :return: ничего не возвращает
    """
    # получаем размеры экрана
    screen_width = custom_window.winfo_screenwidth()
    screen_height = custom_window.winfo_screenheight()

    # вычисляем координаты верхнего левого угла окна
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # задаем положение окна
    custom_window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))


def create_buttons(button_actions, frame):
    """
    функция для динамического создания кнопок и привязки событий
    :param button_actions: словарь с кнопками и соытиями
    :param frame: фрейм на котором распологаются кнопки
    :return: ничего не возвращает
    """
    max_len = max(len(text) for text in button_actions)  # вычисляем максимальную длину текста
    for item, actions in button_actions.items():
        button = ttk.Button(frame, text=item, width=max_len + 5, command=actions)
        button.pack(side="top", fill="x", pady=5)


def create_main_root():
    """
    функция для создания основного окна программы
    :return: возвращает объект окна
    """
    button_actions = {'Закодировать в файл': lambda: create_window_encode(root),
                      'Декодировать из файла': lambda: create_window_decode(root),
                      'Выход из программы': lambda: btn_exit(root),
                      }

    root = tk.Tk()
    # задаем заголовок программы
    root.title("Работа с бинарными файлами")

    # работа с координатами
    get_sizes_custom_window(root)

    # Создаем фрейм для размещения кнопок
    frame = ttk.Frame(root)

    # Создаем кнопки
    create_buttons(button_actions, frame)

    # Размещаем фрейм по центру окна
    frame.place(relx=0.5, rely=0.5, anchor="center")
    root.mainloop()

    return root


def create_window_encode(root):
    encode_buttons = {
        'Добавить файлы': lambda: add_files(files_listbox),
        'Удалить файл': lambda: remove_file(files_listbox),
        'Сохранить файлы': lambda: save_files(root, window, files_listbox.get(0, END)),
    }
    files = []
    files_var = tk.Variable(value=files)
    root.withdraw()  # скрыть главное окно
    window = tk.Tk()
    window.title("Кодирование файла")

    # работа с координатами
    get_sizes_custom_window(window)

    frame = ttk.Frame(window)
    frame.pack(expand=True, fill='both', padx=5, pady=5)
    files_listbox = tk.Listbox(frame, listvariable=files_var)
    files_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Создаем кнопки
    create_buttons(encode_buttons, frame)

    # Обработчик события закрытия окна
    window.protocol("WM_DELETE_WINDOW", lambda: on_window_close(root, window))



def create_window_decode(root):
    src_file_path = []
    info_file_path = []
    decode_buttons = {
        'Добавить закодированный файл ': lambda: select_encoded_file(src_file_path),
        'Добавить информационный файл ': lambda: select_info_file(info_file_path),
        'Раскодировать ': lambda: decode_files(root, ''.join(src_file_path), ''.join(info_file_path), root, window),
    }
    root.withdraw()  # скрыть главное окно
    window = tk.Tk()
    window.title("ДЕКодирование файла")

    # работа с координатами
    get_sizes_custom_window(window)

    frame = ttk.Frame(window)
    frame.pack(expand=True, fill='both', padx=5, pady=5)
    frame.place(relx=0.5, rely=0.5, anchor="center")
    # Создаем кнопки
    create_buttons(decode_buttons, frame)

    # Обработчик события закрытия окна
    window.protocol("WM_DELETE_WINDOW", lambda: on_window_close(root, window))

