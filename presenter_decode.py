from tkinter import messagebox
import os
from presenter import select_tips_file, try_decorator, read_info_file, on_window_close, get_sizes_custom_window, btn_exit
from presenter_encode import read_encoded_data
from view_presenter import tk, ttk,  create_buttons



@try_decorator
def decode_files(root, src_file_path, info_file_path, parent_window, children_window):
    """
    функция для Раскодирование файлов с помощью информационного файла
    :param root: объект программы
    :param src_file_path: путь к файлу декодирования
    :param info_file_path: путь к файлу с информацией
    :param parent_window: основное окно программы
    :param children_window: окно декодирования
    :return:
    """

    if not src_file_path or not info_file_path:
        messagebox.showwarning("Ошибка", "Не выбраны файлы для раскодирования.")
        return

    file_sizes = read_info_file(info_file_path)
    old_size = 0

    for filename, size in file_sizes:
        decode_file(src_file_path, info_file_path, filename, size)
        old_size += size

    messagebox.showinfo("Успешно", "Файлы успешно раскодированы.")

    parent_window.deiconify()  # Восстанавливаем основное окно
    btn_exit(children_window)  # Уничтожаем дочернее окно


def decode_file(src_file_path, info_file_path, filename, size):
    """
    Раскодирование одного файла
    :param src_file_path: путь к файлу с закодированными данными
    :param info_file_path: путь к файлу с информацией о размерах
    :param filename: имя файла для раскодирования
    :param size: размер файла
    """
    encoded_data = read_encoded_data(src_file_path, 0, size)

    # Запись раскодированных данных в новый файл
    decoded_file_path = os.path.splitext(filename)[0] + '_new' + os.path.splitext(filename)[1]
    with open(decoded_file_path, 'wb') as dst_file:
        dst_file.write(encoded_data)


def create_window_decode(root):
    src_file_path = []
    info_file_path = []
    decode_buttons = {
        'Добавить закодированный файл ': lambda: select_tips_file(src_file_path, selected_src_file_label, 'src'),
        'Добавить информационный файл ': lambda: select_tips_file(info_file_path, selected_info_file_label, 'info'),
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

    selected_src_file_label = ttk.Label(frame, text="Не выбран файл для декодирования",background='red')
    selected_src_file_label.pack()
    selected_info_file_label = ttk.Label(frame, text="Не выбран информационный файл для декодирования",background='red')
    selected_info_file_label.pack()

    # Создаем кнопки
    create_buttons(decode_buttons, frame)

    # Обработчик события закрытия окна
    window.protocol("WM_DELETE_WINDOW", lambda: on_window_close(root, window))


