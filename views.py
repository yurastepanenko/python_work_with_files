import tkinter as tk

root = tk.Tk()
root.title("Работа с бинарными файлами")

# задаем размеры окна
window_width = 400
window_height = 300

# получаем размеры экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# вычисляем координаты верхнего левого угла окна
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# задаем положение окна
root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

root.mainloop()