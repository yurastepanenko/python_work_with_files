from presenter import (add_files,
                       remove_file,
                       save_files,on_window_close,
                       get_sizes_custom_window,
                       create_buttons
                       )
from view_presenter import (tk,
                            ttk)
from tkinter import END, NW, X


def read_encoded_data(src_file_path, start, size):
    """
    Чтение закодированных данных из файла
    :param src_file_path: путь к файлу с закодированными данными
    :param start: начальная позиция чтения
    :param size: размер данных для чтения
    :return: прочитанные данные
    """
    with open(src_file_path, 'rb') as src_file:
        src_file.seek(start)
        data = src_file.read(size)
    return data


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