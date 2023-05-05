import tkinter as tk
from presenter import btn_decode, btn_encode


def btn_exit():
    """
    функция которая завершает работу приложения(вынесена в данный файл, чтобы не было зацикливаний при импортах)
    :return: ничего не возвращает
    """
    root.destroy()  # закрываем окно


root = tk.Tk()
button_actions = {'Закодировать в файл': btn_encode,
                  'Декодировать из файла': btn_decode,
                  'Выход из программы': btn_exit,
                  }



