from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
import os


def btn_exit(root):
    """
    функция которая завершает работу приложения(вынесена в данный файл, чтобы не было зацикливаний при импортах)
    :return: ничего не возвращает
    """
    root.destroy()  # закрываем окно


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
            sizes_file.write(f"{file_path}-{file_size}\n")


def save_files(parent_window, children_window, file_paths=None):
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

    parent_window.deiconify()  # Восстанвливаем основное окно
    messagebox.showinfo("Успешно", "Операция выполнена успешно! Файл закодирован!")
    btn_exit(children_window)  # Уничтожаем дочернее окно


def select_encoded_file(src_file_path):
    file_path = filedialog.askopenfilename(title="Выберите закодированный файл")
    src_file_path.append(file_path)


def select_info_file(info_file_path):
    file_path = filedialog.askopenfilename(title="Выберите текстовый файл с информацией о размерах файлов")
    info_file_path.append(file_path)


def decode_files(root, src_file_path, info_file_path):
    # Раскодирование файлов с помощью информационного файла
    print('название файла для декодирования', src_file_path)
    print('название файла инфо',info_file_path)

    if src_file_path and info_file_path:
        with open(info_file_path) as f:
            for line in f:
                filename, size = line.strip().split('-')
                size = int(size)
                print(filename, size, 'fffffff', type(size))

                # Открываем закодированный файл
                with open(src_file_path, 'rb') as src_file:
                    # Установка позиции чтения в нужное место
                    data = src_file.read(size)
                    # print(data)
                    # src_file.seek(0, size)
                    # data = src_file.read(size)
                    # print(data)
                    # Читаем размерности блоков из информационного файла

                    # blocks = []
                    # while True:
                    #     data = f.read(size)
                    #     print(data)
                    #     if not data:
                    #         break
                    #     blocks.append(int(data))

                    # Раскодируем блоки и записываем результат в новый файл
                    with open(os.path.splitext(filename)[0]+'new.txt', 'wb') as dst_file:
                        print('новое название - ', os.path.splitext(filename)[0])
                        # for block in blocks:
                        #     print(block)
                        #     data = src_file.read(block)
                        dst_file.write(data)
        messagebox.showinfo("Успешно", "Файлы успешно раскодированы.")
    else:
        messagebox.showwarning("Ошибка", "Не выбраны файлы для раскодирования.")


