import tkinter as tk
from tkinter import ttk
from presenter import btn_exit
from models import (window_width,
                    window_height)
from presenter_decode import create_window_decode
from presenter_encode import create_window_encode









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






