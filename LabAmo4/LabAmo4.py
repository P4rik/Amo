import os.path
from math import exp, sin
from scipy.interpolate import lagrange, interp1d
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox,  ttk
from random import uniform
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

canvas = None

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def select_method():
    global canvas, canvas_complexity
    method = var.get()
    if method == 1:
        # Labels
        labelfr1.grid(row=0, column=1, columnspan=7, padx=(10, 10), sticky="snew")
        a_label.grid(row=1, column=2, padx=5, pady=5)
        b_label.grid(row=2, column=2, padx=5, pady=5)
        e_label.grid(row=3, column=2, padx=5, pady=20)
        # Entry
        a_entry.grid(row=1, column=3, padx=5, pady=5)
        b_entry.grid(row=2, column=3, padx=5, pady=5)
        e_entry.grid(row=3, column=3, padx=5, pady=20)
        # Button
        button_load.grid(row=5, column=2, padx=(15, 15), pady=(15, 0))
        button_clear.grid(row=5, column=3, padx=(15, 15), pady=(15, 0))
    else:
        labelfr1.grid_forget()
        a_label.grid_forget()
        b_label.grid_forget()
        e_label.grid_forget()
        a_entry.grid_forget()
        b_entry.grid_forget()
        e_entry.grid_forget()
        button_load.grid_forget()
        button_clear.grid_forget()
    if method == 2:
        labelfr2.grid(row=0, column=1, columnspan=7, padx=(10, 10), sticky="snew")
        labelA.grid(row=1, column=1, padx=10)
        labelB.grid(row=2, column=1, padx=10)
        labelE.grid(row=3, column=1, padx=10)
        labelint.grid(row=4, column=1, padx=10)
        labelx.grid(row=5, column=1, padx=10)
        labelct.grid(row=6, column=1, padx=10)
        button_calculate.grid(row=7, column=1, columnspan=2, padx=(15, 15), pady=(15, 0))
    else:
        labelfr2.grid_forget()
        labelA.grid_forget()
        labelB.grid_forget()
        labelE.grid_forget()
        labelint.grid_forget()
        labelx.grid_forget()
        labelct.grid_forget()
        button_calculate.grid_forget()
    if method == 3:
        labelfr3.grid(row=0, column=1, columnspan=7, padx=(10, 10), pady=(0, 0), sticky="snew")
        button_generate.grid(row=6, column=5, pady=(40, 0), padx=(20, 20), sticky="snew")
    else:
        labelfr3.grid_forget()
        button_generate.grid_forget()
        if canvas is not None:
            canvas.get_tk_widget().grid_forget()
def f(x):
    return x ** 3 + 6 * x - 5

def first_derivative(x):
    return 3 * x ** 2 + 6

def second_derivative(x):
    return 6 * x

# Win 1
win = tk.Tk()
photo = tk.PhotoImage(file=(resource_path('icon.png')))
win.iconphoto(False, photo)
win.title("Вікно 1")
win.config(bg='#363636')
win.geometry("")
win.resizable(False, False)

G = 24
N = 20

# frame
panel = tk.Frame(win, bg='#252425', relief=tk.RAISED, bd=5).grid(row=0, rowspan=11, column=0, sticky='snew')
panel2 = tk.Frame(win, bg='#252425', relief=tk.RAISED, bd=5).grid(row=0, rowspan=11, columnspan=9, column=1,
                                                                  sticky='snew')
panel3 = tk.Frame(win, bg='#252425', relief=tk.RAISED, bd=5).grid(row=0, rowspan=11, column=1, columnspan=9, sticky='snew')
panel4 = tk.Frame(win, bg='#252425', relief=tk.RAISED, bd=5).grid(row=0, rowspan=11, column=1, sticky='snew')

# Label
labelname = tk.Label(panel, text=f'Паровенко Данило Едуардович\nМоя група: ІО-{G}\nМій варіант: {N}',
                     bg='#252425', fg='white',
                     font=('Calibri', 20, 'bold')).grid(row=7, column=0, padx=(20, 20), pady=(0, 20))

label_1 = tk.Label(panel, text='Панель керування:', font=('Calibri', 25, 'bold'), bg='#252425', fg='white',
                   height=0).grid(row=0, column=0, padx=(10, 10), pady=(30, 30))

# Radbut
var = tk.IntVar()
radb1 = tk.Radiobutton(panel, text='Введення даних', variable=var, value=1, font=('Calibri', 25, 'bold'), bg='#977AF9',
                       fg='black', state=tk.NORMAL, width=22, activebackground='#760598', relief=tk.RAISED,
                       bd='5', command=select_method).grid(row=1, column=0, pady=(10, 10), padx=(15, 15))

radb2 = tk.Radiobutton(panel, text='Обрахунок рівняння', variable=var, value=2, font=('Calibri', 25, 'bold'), bg='#977AF9',
                       fg='black', state=tk.NORMAL, width=22, activebackground='#760598', relief=tk.RAISED,
                       bd='5', command=select_method).grid(row=2, column=0, pady=(10, 10), padx=(15, 15))

radb3 = tk.Radiobutton(panel, text='Генерація графіка', variable=var, value=3, font=('Calibri', 25, 'bold'),
                       bg='#977AF9',
                       fg='black', state=tk.NORMAL, width=22, activebackground='#760598', relief=tk.RAISED,
                       bd='5', command=select_method).grid(row=3, column=0, pady=(10, 10), padx=(15, 15))

#Win 2
def load_data():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                data_A1 = file.read().splitlines()
                for i, entry in enumerate(length_entries):
                    if i < len(data_A1):
                        entry.delete(0, tk.END)
                        entry.insert(0, data_A1[i])
                    else:
                        break
        except FileNotFoundError:
            messagebox.showerror(title='Помилка', message="Файл з даними не знайденно!")
        except IOError:
            messagebox.showerror(title='Помилка', message="Помилка при читанні файлу!")
    else:
        messagebox.showwarning(title='Попередження', message="Ви не обрали файл!")

def clear_entries():
    for entry in length_entries:
        entry.delete(0, tk.END)

labelfr1 = tk.Label(panel2, text="Задайте значення:", font=('Calibri', 25, 'bold'), bg='#252425', fg='white')
a_label = tk.Label(panel2, text="Введіть a:", bg='#252425', fg='white', font=('Calibri', 20, 'bold'))
b_label = tk.Label(panel2, text="Введіть b:", bg='#252425', fg='white', font=('Calibri', 20, 'bold'))
e_label = tk.Label(panel2, text="Введіть тоічність обчислення ε:", bg='#252425', fg='white',
                   font=('Calibri', 20, 'bold'))

a_entry = tk.Entry(panel2, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')
b_entry = tk.Entry(panel2, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')
e_entry = tk.Entry(panel2, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')

length_entries = [a_entry, b_entry, e_entry]

button_load = tk.Button(panel2, text="Завантажити дані з файлу", font=('Calibri', 25, 'bold'), bg='#977AF9',
                        width=22, relief=tk.RAISED, activebackground='#760598', bd=5, fg='white', command=load_data)
button_clear = tk.Button(panel2, text='Очистити', font=('Calibri', 25, 'bold'), bg='#977AF9', width=22,
                         relief=tk.RAISED, activebackground='#760598', bd=5, fg='white', command=clear_entries)

#Win 3
def calculation_data():
    global a_temp, b_temp, e_temp, counter, a_value, b_value, e_value, x_value

    try:
        # Отримання вхідних даних з полів введення
        a_value = float(a_entry.get())
        b_value = float(b_entry.get())
        e_value = float(e_entry.get())
        a_temp = a_value
        b_temp = b_value
        e_temp = e_value

        # Перевірка умови для розрахунків
        if f(a_value) * f(b_value) > 0:
            messagebox.showerror("Помилка", "Введіть інші вхідні дані!")
            return

        # Обчислення кореня рівняння
        counter = 0
        while abs(b_value - a_value) > e_value:
            x = (b_value + a_value) / 2
            if first_derivative(x) * second_derivative(x) < 0:
                a_value, b_value = b_value, a_value
            a_value = a_value - (f(a_value) * (b_value - a_value)) / (f(b_value) - f(a_value))
            b_value = b_value - f(b_value) / first_derivative(b_value)
            counter += 1
        x_value = (b_value + a_value) / 2

        # Оновлення значень лейблів з обчисленими даними
        labelA.config(text=f"Межа(A): {a_temp}", font=('Calibri', 25, 'bold'), bg='#252425', fg='white')
        labelB.config(text=f"Межа(B): {b_temp}")
        labelE.config(text=f"Точність обчислення(ε): {e_temp}")
        labelint.config(text=f"Проміжок ізольованого корення: [{a_value}, {b_value}]")
        labelx.config(text=f"X: {x_value}")
        labelct.config(text=f"Ізольований за таку кількість кроків:{counter}")

    except ValueError:
        messagebox.showerror("Помилка", "Дані повинні бути десятковими або цілими")

# Створення пустих змінних
a_temp = ""
b_temp = ""
e_temp = ""
a_value = ""
b_value = ""
e_value = ""
x_value = ""
counter = ""

# Створення та розміщення лейблів у вікні
labelfr2 = tk.Label(panel3, text="Результати рівняння:", font=('Calibri', 25, 'bold'), bg='#252425', fg='white')
labelA = tk.Label(panel3, text=f"Межа(A): {a_temp}", font=('Calibri', 25, 'bold'), bg='#252425', fg='white')
labelB = tk.Label(panel3, text=f"Межа(B): {b_temp}", font=('Calibri', 25, 'bold'), bg='#252425', fg='white')
labelE = tk.Label(panel3, text=f"Точність обчислення(E): {e_temp}", font=('Calibri', 25, 'bold'), bg='#252425', fg='white')
labelint = tk.Label(panel3, text=f"Проміжок ізольованого корення: [{a_value}, {b_value}]", font=('Calibri', 25, 'bold'),
                  bg='#252425', fg='white')
labelx = tk.Label(panel3, text=f"X: {x_value}", font=('Calibri', 25, 'bold'), bg='#252425', fg='white')
labelct = tk.Label(panel3, text=f"Ізольований за таку кількість кроків:{counter}", font=('Calibri', 25, 'bold'),
                  bg='#252425', fg='white')

# Створення кнопки для обчислення рівняння
button_calculate = tk.Button(panel3, text="Обрахувати рівняння", font=('Calibri', 25, 'bold'), bg='#977AF9',
                            width=22, relief=tk.RAISED, activebackground='#760598', bd=5, fg='white',
                            command=calculation_data)
#Win 4
labelfr3 = tk.Label(panel4, text="Генерація графіків:", font=('Calibri', 25, 'bold'), bg='#252425', fg='white')
def generate_plot():
    global canvas
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())

        x_values = [a + (b - a) / 100 * i for i in range(100)]
        y_values = [x ** 3 + 6 * x - 5 for x in x_values]
        x_ord = [0] * len(x_values)

        fig, ax = plt.subplots()
        ax.plot(x_values, y_values, marker="", linestyle="-", color="red")
        ax.plot(x_values, x_ord, marker="", linestyle="-", color="blue")
        ax.plot(x_value, 0, marker="o", color="red")
        ax.set_title('Графік функції: x^3 + 6x - 5')
        ax.grid(True)

        canvas = FigureCanvasTkAgg(fig, master=panel4)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=5, rowspan=5, padx=15)

    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректні значення для інтервалу")

button_generate = tk.Button(panel4, text='Згенерувати графік', font=('Calibri', 25, 'bold'), bg='#977AF9',
                             relief=tk.RAISED, activebackground='#760598', bd=5, fg='white', command=generate_plot)

win.mainloop()