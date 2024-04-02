import os.path
from math import exp, sin
from scipy.interpolate import lagrange, interp1d
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from random import uniform
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

canvas = None
canvas_sin = None
canvas_errors = None


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
        labelfr1.grid(row=0, column=1, columnspan=7, padx=(10, 10), pady=(0, 0), sticky="snew")
        a_label.grid(row=1, column=2, padx=5, pady=5)
        b_label.grid(row=2, column=2, padx=5, pady=5)
        points_label.grid(row=3, column=2, padx=5, pady=5)
        x_label.grid(row=4, column=2, padx=5, pady=20)
        # Entry
        a_entry.grid(row=1, column=3, padx=5, pady=5)
        b_entry.grid(row=2, column=3, padx=5, pady=5)
        points_entry.grid(row=3, column=3, padx=5, pady=5)
        x_entry.grid(row=4, column=3, padx=5, pady=20)
        # Button
        button_load.grid(row=5, column=2, padx=(15, 15), pady=(15, 0))
        button_clear.grid(row=5, column=3, padx=(15, 15), pady=(15, 0))
    else:
        labelfr1.grid_forget()
        a_label.grid_forget()
        b_label.grid_forget()
        points_label.grid_forget()
        x_label.grid_forget()
        a_entry.grid_forget()
        b_entry.grid_forget()
        points_entry.grid_forget()
        x_entry.grid_forget()
        button_load.grid_forget()
        button_clear.grid_forget()
    if method == 2:
        labelfr2.grid(row=0, column=1, columnspan=7, padx=(10, 10), pady=(0, 0), sticky="snew")
        results_table.grid(row=1, column=2, columnspan=2, rowspan=5, padx=5, pady=5, ipadx=100)
        button_generate.grid(row=6, column=2, columnspan=2, padx=(15, 15), pady=(15, 0))
    else:
        labelfr2.grid_forget()
        results_table.grid_forget()
        button_generate.grid_forget()
    if method == 3:
        labelfr3.grid(row=0, column=1, columnspan=7, padx=(10, 10), pady=(0, 0), sticky="snew")
        button_generate1.grid(row=6, column=3, pady=(40, 0), padx=(20, 20), sticky="snew")
        button_generate2.grid(row=6, column=5, pady=(40, 0), padx=(20, 20), sticky="snew")
        button_generate3.grid(row=6, column=7, pady=(40, 0), padx=(20, 20), sticky="snew")
    else:
        labelfr2.grid_forget()
        button_generate1.grid_forget()
        button_generate2.grid_forget()
        button_generate3.grid_forget()
        if canvas is not None:
            canvas.get_tk_widget().grid_forget()
        if canvas_sin is not None:
            canvas_sin.get_tk_widget().grid_forget()
        if canvas_errors is not None:
            canvas_errors.get_tk_widget().grid_forget()


def f(x):
    return x ** 2 + 2 * exp(x)

def f2(x):
    return sin(x)


def lagrange_formula(x_nodes, y_nodes, x):
    result = 0
    for i in range(len(x_nodes)):
        temp = 1
        for j in range(i):
            if x_nodes[i] != x_nodes[j]:
                temp *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        for j in range(i + 1, len(x_nodes)):
            if x_nodes[i] != x_nodes[j]:
                temp *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        result += temp * y_nodes[i]
    return result


def generate_table():
    global xi, yi
    # Отримання введених значень
    a_val = float(a_entry.get())
    b_val = float(b_entry.get())
    num_points = int(points_entry.get())

    # Генерація вузлів інтерполяції
    h = (b_val - a_val) / (num_points - 1)
    xi = []
    for i in range(num_points):
        xi.append(a_val + h * i)
    yi = [f(i) for i in xi]

    # Обчислення значення для x
    x_val = float(x_entry.get())
    y_val = lagrange_formula(xi, yi, x_val)
    y_val_exact = f(x_val)

    # Визначення точок для візуалізації інтерполяції
    x_vals = []
    for i in range(num_points):
        x_vals.append(uniform(a_val, b_val))
    y_interp = [lagrange_formula(xi, yi, x_val) for x_val in x_vals]
    y_exact = [f(i) for i in x_vals]

    # Обчислення похибки та коефіцієнта k
    while True:
        additionalNode = uniform(a_val, b_val)
        if additionalNode not in xi:
            for i in range(len(xi)):
                if xi[i] > additionalNode:
                    xi.insert(i - 1, additionalNode)
                    yi.insert(i - 1, f(additionalNode))
                    break
            break

    nextInterpolationList = [lagrange_formula(xi, yi, i) for i in x_vals]

    interpolationDiff = []
    for i in range(len(y_interp)):
        if y_interp[i] - nextInterpolationList[i] != 0:
            interpolationDiff.append(y_interp[i] - nextInterpolationList[i])
        else:
            interpolationDiff.append(0.0000001)

    listOfK = []
    diff = []
    l = len(y_interp)
    for i in range(l):
        diff.append(y_interp[i] - y_exact[i])
        listOfK.append(1 - diff[i] / interpolationDiff[i])

    # Виведення таблиці з результатами
    results_table.delete(*results_table.get_children())
    for i in range(len(x_vals)):
        results_table.insert("", i, text=str(i + 1), values=(str(interpolationDiff[i]), str(diff[i]),
                                                             str(listOfK[i])))

    x_new = [i for i in xi]
    x_new.append(x_val + 0.35)
    x_new.sort()
    y_new = [f(i) for i in x_new]
    nextInterpolation = lagrange_formula(x_new, y_new, x_val)


    results_table.insert("", "end", text=("X"), values=(str(y_val - nextInterpolation),
                                                              str(y_val - y_val_exact),
                                                              str(1 - (y_val - y_val_exact) /
                                                                  (y_val - nextInterpolation + 0.000001))))

def generate_plot1():
    global canvas
    # Отримання введених значень
    a_val = float(a_entry.get())
    b_val = float(b_entry.get())
    num_points = int(points_entry.get())
    x_val = float(x_entry.get())

    # Визначення точок для візуалізації інтерполяції
    x_vals = []
    for i in range(num_points):
        x_vals.append(uniform(a_val, b_val))
    x_vals.sort()
    y_interp = [lagrange_formula(xi, yi, x_val) for x_val in x_vals]
    y_exact = [f(i) for i in x_vals]

    x_data = []
    for i in xi:
        x_data.append(i)
    for i in x_vals:
        x_data.append(i)
    x_data.append(x_val)
    x_data.sort()
    y_data = [lagrange_formula(xi, yi, x) for x in x_data]
    y_data2 = [f(i) for i in x_data]

    # Виведення графіка
    fig, ax = plt.subplots()
    ax.plot(x_data, y_data2, label='Вихідна функція')
    ax.plot(x_data, y_data, label='Інтерпольована функція')
    ax.scatter(xi, yi, color='red', label='Вузли інтерполяції')
    ax.scatter(x_val, f(x_val), color='blue', label=f'Точка (x)')
    ax.scatter(x_val, lagrange_formula(xi, yi, x_val), color='green', label=f'Точка(x) інтерпольована')
    ax.set_title('Інтерполяція за допомогою многочлена Лагранджа')
    ax.set_xlabel('a')
    ax.set_ylabel('b')
    ax.legend()
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=panel3)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=3, rowspan=5, padx=15)


def generate_plot2():
    global canvas_sin
    # Отримання введених значень
    a_val = float(a_entry.get())
    b_val = float(b_entry.get())
    num_points = int(points_entry.get())
    x_val = float(x_entry.get())

    # Генерація вузлів інтерполяції
    h = (b_val - a_val) / (num_points - 1)
    xi = []
    for i in range(num_points):
        xi.append(a_val + h * i)
    yi = [f2(i) for i in xi]

    x_vals = []
    for i in range(num_points):
        x_vals.append(uniform(a_val, b_val))
    x_vals.sort()
    y_interp = [lagrange_formula(xi, yi, x_val) for x_val in x_vals]
    y_exact = [f2(i) for i in x_vals]

    x_data = []
    for i in xi:
        x_data.append(i)
    for i in x_vals:
        x_data.append(i)
    x_data.append(x_val)
    x_data.sort()
    y_data = [lagrange_formula(xi, yi, x) for x in x_data]
    y_data2 = [f2(i) for i in x_data]

    # Виведення графіка
    fig, ax = plt.subplots()
    ax.plot(x_data, y_data2, label='Вихідна функція')
    ax.plot(x_data, y_data, label='Інтерпольована функція')
    ax.scatter(xi, yi, color='red', label='Вузли інтерполяції')
    ax.scatter(x_val, f2(x_val), color='blue', label=f'Точка (x)')
    ax.scatter(x_val, lagrange_formula(xi, yi, x_val), color='green', label=f'Точка(x) інтерпольована')
    ax.set_title('Інтерполяція за допомогою функції sin(x)')
    ax.set_xlabel('a')
    ax.set_ylabel('b')
    ax.legend()
    ax.grid(True)

    canvas_sin = FigureCanvasTkAgg(fig, master=panel3)
    canvas_sin.draw()
    canvas_sin.get_tk_widget().grid(row=1, column=5, rowspan=5, padx=15)

def generate_plot3():
    global canvas_errors
    # Отримання значень з таблиці
    errors = [float(results_table.item(item, 'values')[0]) for item in results_table.get_children()]
    num_points = len(errors)

    # Створення графіка
    fig, ax = plt.subplots()
    ax.plot(range(1, num_points + 1), errors, marker='o')
    ax.set_title('Залежність похибки від кількості точок')
    ax.set_xlabel('Кількість точок')
    ax.set_ylabel('Похибка')
    ax.grid(True)

    canvas_errors = FigureCanvasTkAgg(fig, master=panel3)
    canvas_errors.draw()
    canvas_errors.get_tk_widget().grid(row=1, column=7, rowspan=5, padx=15)



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
panel3 = tk.Frame(win, bg='#252425', relief=tk.RAISED, bd=5).grid(row=0, rowspan=11, column=1, sticky='snew')
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

radb2 = tk.Radiobutton(panel, text='Таблиця похибок', variable=var, value=2, font=('Calibri', 25, 'bold'), bg='#977AF9',
                       fg='black', state=tk.NORMAL, width=22, activebackground='#760598', relief=tk.RAISED,
                       bd='5', command=select_method).grid(row=2, column=0, pady=(10, 10), padx=(15, 15))

radb3 = tk.Radiobutton(panel, text='Згенерувати графіки', variable=var, value=3, font=('Calibri', 25, 'bold'),
                       bg='#977AF9',
                       fg='black', state=tk.NORMAL, width=22, activebackground='#760598', relief=tk.RAISED,
                       bd='5', command=select_method).grid(row=3, column=0, pady=(10, 10), padx=(15, 15))


# win2
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


# labels
labelfr1 = tk.Label(panel2, text="Задайте значення:", font=('Calibri', 25, 'bold'), bg='#252425', fg='white')
a_label = tk.Label(panel2, text="Введіть a:", bg='#252425', fg='white', font=('Calibri', 20, 'bold'))
b_label = tk.Label(panel2, text="Введіть b:", bg='#252425', fg='white', font=('Calibri', 20, 'bold'))
points_label = tk.Label(panel2, text="Кількість точок:", bg='#252425', fg='white', font=('Calibri', 20, 'bold'))
x_label = tk.Label(panel2, text="Введіть x:", bg='#252425', fg='white', font=('Calibri', 20, 'bold'))
# entry
a_entry = tk.Entry(panel2, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')
b_entry = tk.Entry(panel2, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')
points_entry = tk.Entry(panel2, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')
x_entry = tk.Entry(panel2, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')
length_entries = [a_entry, b_entry, points_entry, x_entry]
# buttons
button_load = tk.Button(panel2, text="Завантажити дані з файлу", font=('Calibri', 25, 'bold'), bg='#977AF9',
                        width=22, relief=tk.RAISED, activebackground='#760598', bd=5, fg='white', command=load_data)
button_clear = tk.Button(panel2, text='Очистити', font=('Calibri', 25, 'bold'), bg='#977AF9', width=22,
                         relief=tk.RAISED, activebackground='#760598', bd=5, fg='white', command=clear_entries)

# win3
labelfr2 = tk.Label(panel3, text="Таблиця похибок:", font=('Calibri', 25, 'bold'), bg='#252425', fg='white')
results_table = ttk.Treeview(panel3)
results_table["height"] = 15
results_table["columns"] = ("error", "difference", "k_value")
results_table.heading("#0", text="Кількість точок")
results_table.heading("error", text="Похибка")
results_table.heading("difference", text="Різниця")
results_table.heading("k_value", text="Коефіцієнт k")

# Налаштування стилю тексту у таблиці
style = ttk.Style()
style.configure("Treeview", font=('Calibri', 15, 'bold'))
style.configure("Treeview.Heading", font=('Calibri', 15, 'bold'))

button_generate = tk.Button(panel3, text="Згенерувати таблицю", font=('Calibri', 25, 'bold'), bg='#977AF9',
                            width=22, relief=tk.RAISED, activebackground='#760598', bd=5, fg='white',
                            command=generate_table)
# win4
labelfr3 = tk.Label(panel4, text="Генерація графіків:", font=('Calibri', 25, 'bold'), bg='#252425',
                    fg='white')

button_generate1 = tk.Button(panel4, text='Згенерувати практичний графік', font=('Calibri', 25, 'bold'), bg='#977AF9',
                             relief=tk.RAISED, activebackground='#760598', bd=5, fg='white', command=generate_plot1)
button_generate2 = tk.Button(panel4, text='Згенерувати теоретичний графік', font=('Calibri', 25, 'bold'), bg='#977AF9',
                             relief=tk.RAISED, activebackground='#760598', bd=5, fg='white', command=generate_plot2)
button_generate3 = tk.Button(panel4, text='Згенерувати теоретичний графік', font=('Calibri', 25, 'bold'), bg='#977AF9',
                             relief=tk.RAISED, activebackground='#760598', bd=5, fg='white', command=generate_plot3)

win.mainloop()
