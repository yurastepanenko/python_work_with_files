from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
import os


def try_decorator(fn):
    """
    функция для обработки ошибок
    :param *args, **kwargs: любое кол-во параметров
    :return: выоленение ф-ии или возврат ошибки
    """
    def wrapped(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except ValueError as e:
            messagebox.showerror("Ошибка", "Вероятнее всего вы выбрали некорректный info-file")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

    return wrapped


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
    if not file_paths:
        messagebox.showwarning("Ошибка", "Не выбраны файлы для сохранения.")
        return

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


def select_tips_file(type_file_path, selected_file_label, type):
    """
    функция для выбора закодированного файла
    :param src_file_path: путь к файлу
    :param selected_file_label: метка для описания src - файла
    param type: тип для нашего лейбла
    :return: новый текст и цвет лейбла
    """
    if type == 'src':
        title ="Выберите закодированный файл"
        text = 'src: '
    elif type == 'info':
        title = "Выберите текстовый файл с информацией о размерах файлов"
        text = 'info: '

    file_path = filedialog.askopenfilename(title=title)
    type_file_path.clear()  # Очистка списка info_file_path
    type_file_path.append(file_path)
    selected_file_label.configure(text=text + file_path, background='green')
    return selected_file_label


def read_info_file(info_file_path):
    """
    Чтение файла с информацией о размерах
    :param info_file_path: путь к файлу с информацией
    :return: список кортежей (имя файла, размер)
    """
    file_sizes = []
    with open(info_file_path) as f:
        for line in f:
            filename, size = line.strip().split('-')
            file_sizes.append((filename, int(size)))
    return file_sizes


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

