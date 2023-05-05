import tkinter as tk
from tkinter import ttk, END, NW, X
from presenter import btn_exit
from presenter import add_files, remove_file, save_files


def create_main_root():
    button_actions = {'Закодировать в файл': lambda: btn_encode(root),
                      'Декодировать из файла': lambda: btn_decode(root),
                      'Выход из программы': lambda: btn_exit(root),
                      }

    root = tk.Tk()
    # задаем заголовок программы
    root.title("Работа с бинарными файлами")

    # задаем размеры окна
    window_width = 350
    window_height = 100

    # получаем размеры экрана
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # вычисляем координаты верхнего левого угла окна
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # задаем положение окна
    root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

    # Создаем фрейм для размещения кнопок
    frame = ttk.Frame(root)

    # Создаем кнопки
    max_len = max(len(text) for text in button_actions)  # вычисляем максимальную длину текста
    for item, actions in button_actions.items():
        button = ttk.Button(frame, text=item, width=max_len+1, command=actions)
        button.pack(side="top", fill="x", pady=5)

    # Размещаем фрейм по центру окна
    frame.place(relx=0.5, rely=0.5, anchor="center")
    root.mainloop()

    return root


def btn_encode(root):
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


    # задаем размеры окна
    window_width = 350
    window_height = 300

    # получаем размеры экрана
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # вычисляем координаты верхнего левого угла окна
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # задаем положение окна
    window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
    frame = ttk.Frame(window)
    frame.pack(expand=True, fill='both', padx=5, pady=5)
    files_listbox = tk.Listbox(frame, listvariable=files_var)
    files_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    max_len = max(len(text) for text in encode_buttons)  # вычисляем максимальную длину текста
    for item, actions in encode_buttons.items():
        button = ttk.Button(frame, text=item, width=max_len + 1, command=actions)
        button.pack(side="top", fill="x", pady=5)


def btn_decode(root):
    decode_buttons = {
        'Добавить закодированный файл ': lambda: add_files(root),
        'Добавить информационный файл ': lambda: add_files(),
        'Раскодировать ': lambda: add_files(),
    }
    root.withdraw()  # скрыть главное окно
    window = tk.Tk()
    window.title("ДЕКодирование файла")

    # задаем размеры окна
    window_width = 350
    window_height = 300

    # получаем размеры экрана
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # вычисляем координаты верхнего левого угла окна
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # задаем положение окна
    window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
    frame = ttk.Frame(window)
    frame.pack(expand=True, fill='both', padx=5, pady=5)

    max_len = max(len(text) for text in decode_buttons)  # вычисляем максимальную длину текста
    for item, actions in decode_buttons.items():
        button = ttk.Button(frame, text=item, width=max_len + 1, command=actions)
        button.pack(side="top", fill="x", pady=5)