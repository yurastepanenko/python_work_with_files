from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os


def add_files(files_listbox):
    """
    функция добавления файлов в лист-бокс
    :param files_listbox: лист-бокс в который нам необходимо добавить
    :return: ничего не возвращает
    """
    selected_files = filedialog.askopenfilenames()
    for file in selected_files:
        files_listbox.insert(END, file)


def remove_file(files_listbox):
    """
       функция удаления выделенного файла из лист-бокса
       :param files_listbox: лист-бокс из которого надо удалить файл
       :return: ничего не возвращает
       """
    selected_items = files_listbox.curselection()
    for item in selected_items:
        files_listbox.delete(item)


def generate_file_sizes(file_paths, save_file_path):
    """
    функция, которая генерирует файл с размерами
    :param file_paths: путь к файлу
    :param save_file_path: размер файла
    :return:
    """
    save_file_dir = os.path.dirname(save_file_path)
    sizes_file_path = os.path.join(save_file_dir, "file_sizes.txt")
    with open(sizes_file_path, "w") as sizes_file:
        for file_path in file_paths:
            file_size = os.path.getsize(file_path)
            sizes_file.write(f"{file_path} - {file_size} bytes\n")


def save_files(file_paths=None):
    """
    функция кодирует в файл другие файлы
    :param file_paths: передаем содержимое нашего лист-бокса
    :return:
    """
    save_file_path = filedialog.asksaveasfilename(title="Сохранить как", defaultextension=".txt")
    if save_file_path:
        with open(save_file_path, "wb") as save_file:
            for file_path in file_paths:
                with open(file_path, "rb") as f:
                    file_content = f.read()
                    save_file.write(file_content)
        generate_file_sizes(file_paths, save_file_path)


def btn_encode():
    decode_buttons = {
        'Добавить файлы': lambda: add_files(files_listbox),
        'Удалить файл': lambda: remove_file(files_listbox),
        'Сохранить файлы': lambda: save_files(files_listbox.get(0, END)),
    }
    files = []
    files_var = Variable(value=files)
    print("btn_decode")
    window = Tk()
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
    files_listbox = Listbox(frame, listvariable=files_var)
    files_listbox.pack(anchor=NW, fill=X, padx=5, pady=5)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    max_len = max(len(text) for text in decode_buttons)  # вычисляем максимальную длину текста
    for item, actions in decode_buttons.items():
        button = ttk.Button(frame, text=item, width=max_len + 1, command=actions)
        button.pack(side="top", fill="x", pady=5)

  



def btn_decode():
    print("btn_decode")



