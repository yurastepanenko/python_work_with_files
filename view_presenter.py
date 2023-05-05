from tkinter import ttk
from models import button_actions, root


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
