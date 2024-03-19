import os.path
import tkinter as tk
from tkinter import filedialog, messagebox
import time
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import Counter

canvas = None
canvas_complexity = None

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
        M1.grid(row=1, column=2, padx=(20, 0), pady=(0, 0))
        M2.grid(row=2, column=2, padx=(20, 0), pady=(0, 20))
        M3.grid(row=3, column=2, padx=(20, 0), pady=(0, 30))
        M4.grid(row=4, column=2, padx=(20, 0), pady=(0, 30))
        M5.grid(row=5, column=2, padx=(20, 0), pady=(0, 30))
        M6.grid(row=1, column=4, padx=(20, 0), pady=(0, 0))
        M7.grid(row=2, column=4, padx=(20, 0), pady=(0, 20))
        M8.grid(row=3, column=4, padx=(20, 0), pady=(0, 30))
        M9.grid(row=4, column=4, padx=(20, 0), pady=(0, 30))
        M10.grid(row=5, column=4, padx=(20, 0), pady=(0, 30))
        # Entry
        vM1.grid(row=1, column=3, padx=(0, 20), pady=(0, 0), sticky='ew')
        vM2.grid(row=2, column=3, padx=(0, 20), pady=(0, 20), sticky='ew')
        vM3.grid(row=3, column=3, padx=(0, 20), pady=(0, 30), sticky='ew')
        vM4.grid(row=4, column=3, padx=(0, 20), pady=(0, 30), sticky='ew')
        vM5.grid(row=5, column=3, padx=(0, 20), pady=(0, 30), sticky='ew')
        vM6.grid(row=1, column=5, padx=(0, 20), pady=(0, 0), sticky='ew')
        vM7.grid(row=2, column=5, padx=(0, 20), pady=(0, 20), sticky='ew')
        vM8.grid(row=3, column=5, padx=(0, 20), pady=(0, 30), sticky='ew')
        vM9.grid(row=4, column=5, padx=(0, 20), pady=(0, 30), sticky='ew')
        vM10.grid(row=5, column=5, padx=(0, 20), pady=(0, 30), sticky='ew')
        # Button
        button_load.grid(row=6, column=3, pady=(40, 0), padx=(0, 20), sticky="snew")
        button_clear.grid(row=6, column=5, pady=(40, 0), padx=(0, 20), sticky="snew")
    else:
        labelfr1.grid_forget()
        M1.grid_forget()
        M2.grid_forget()
        M3.grid_forget()
        M4.grid_forget()
        M5.grid_forget()
        M6.grid_forget()
        M7.grid_forget()
        M8.grid_forget()
        M9.grid_forget()
        M10.grid_forget()
        vM1.grid_forget()
        vM2.grid_forget()
        vM3.grid_forget()
        vM4.grid_forget()
        vM5.grid_forget()
        vM6.grid_forget()
        vM7.grid_forget()
        vM8.grid_forget()
        vM9.grid_forget()
        vM10.grid_forget()
        button_load.grid_forget()
        button_clear.grid_forget()
    if method == 2:
        labelfr2.grid(row=0, column=1, columnspan=7, padx=(10, 10), pady=(0, 0), sticky="snew")
        button_generate1.grid(row=6, column=3, pady=(40, 0), padx=(20, 20), sticky="snew")
        button_generate2.grid(row=6, column=5, pady=(40, 0), padx=(20, 20), sticky="snew")
    else:
        labelfr2.grid_forget()
        button_generate1.grid_forget()
        button_generate2.grid_forget()
        if canvas is not None:
            canvas.get_tk_widget().grid_forget()
        if canvas_complexity is not None:
            canvas_complexity.get_tk_widget().grid_forget()

def bubble_sort(array):
    n = len(array)
    k = n
    operations = 0
    while k > 0:
        swapped = False
        operations += 1
        for i in range(1, k):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]
                swapped = True
                operations += 4
        k -= 1
        operations += 2
        if not swapped:
            break
    return array, operations

def generate_arrays(array_lengths):
    arrays = []
    for length in array_lengths:
        arrays.append([random.randint(0, 10000) for _ in range(length)])
    return arrays

def measure_sorting_time(arrays):
    sorting_times = []
    for array in arrays:
        start_time = time.time()
        sorted_array = bubble_sort(array)
        end_time = time.time()
        sorting_times.append(end_time - start_time)
    return sorting_times

def plot_sorting_times():
    global canvas
    try:
        array_lengths = [int(entry.get()) for entry in length_entries]
    except ValueError:
        messagebox.showerror(title="Помилка", message="Невірний ввід! Будь ласка, введіть цілі числа для довжини масивів.")
        return

    arrays = generate_arrays(array_lengths)
    sorting_times = measure_sorting_time(arrays)

    # Сортування за довжиною масивів
    array_lengths, sorting_times = zip(*sorted(zip(array_lengths, sorting_times)))

    # Побудова графіка за виміряними часами сортування
    fig, ax = plt.subplots()
    ax.plot(array_lengths, sorting_times, marker='o', linestyle='-')
    ax.set_title('Залежність часу сортування від розміру масиву')
    ax.set_xlabel('Розмір масиву')
    ax.set_ylabel('Час сортування (секунди)')
    ax.grid(True)

    # Відображення графіка у вікні
    canvas = FigureCanvasTkAgg(fig, master=panel3)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=3, rowspan=5, padx=15)

def plot_complexity():
    global canvas_complexity
    try:
        array_lengths = [int(entry.get()) for entry in length_entries]
    except ValueError:
        messagebox.showerror(title="Помилка", message="Невірний ввід! Будь ласка, введіть цілі числа для довжини масивів.")
        return

    # Створюємо списки для зберігання кількості операцій та довжини масиву
    operations_list = []
    array_lengths_list = []

    for length in array_lengths:
        array = [random.randint(0, 10000) for _ in range(length)]
        sorted_array, operations = bubble_sort(array)  # Отримуємо відсортований масив та кількість операцій
        operations_list.append(operations)
        array_lengths_list.append(length)

    # Сортуємо дані за зростанням розміру масиву
    array_lengths_list, operations_list = zip(*sorted(zip(array_lengths_list, operations_list)))

    # Побудова графіка
    fig, ax = plt.subplots()
    ax.plot(array_lengths_list, operations_list, marker='o', linestyle='-', color='red', label='Кількість операцій')
    ax.set_title('Теоретичний графік')
    ax.set_xlabel('Розмір масиву')
    ax.set_ylabel('Кількість операцій')
    ax.legend()
    ax.grid(True)

    # Відображення графіка у вікні
    canvas_complexity = FigureCanvasTkAgg(fig, master=panel3)
    canvas_complexity.draw()
    canvas_complexity.get_tk_widget().grid(row=1, column=5, rowspan=5, padx=15)


#Win 1
win = tk.Tk()
photo = tk.PhotoImage(file=(resource_path('icon.png')))
win.iconphoto(False, photo)
win.title("Вікно 1")
win.config(bg='#363636')
win.geometry("")
win.resizable(False, False)

G = 24
N = 20

#frame
panel = tk.Frame(win,bg='#252425', relief=tk.RAISED, bd=5).grid(row=0, rowspan=11, column=0, sticky='snew')
panel2 = tk.Frame(win, bg='#252425', relief=tk.RAISED, bd=5).grid(row=0, rowspan=11, columnspan=9, column=1,
                                                                  sticky='snew')
panel3 = tk.Frame(win, bg='#252425', relief=tk.RAISED, bd=5).grid(row=0, rowspan=11, column=1, sticky='snew')

#Label
labelname = tk.Label(panel, text=f'Паровенко Данило Едуардович\nМоя група: ІО-{G}\nМій варіант: {N}',
                     bg='#252425', fg='white',
                     font=('Calibri', 20, 'bold')).grid(row=7, column=0, padx=(20, 20), pady=(0, 20))

label_1 = tk.Label(panel, text='Панель керування:', font=('Calibri', 25, 'bold'), bg='#252425', fg='white',
                   height=0).grid(row=0, column=0, padx=(10, 10), pady=(30, 30))

#Radbut
var = tk.IntVar()
radb1 = tk.Radiobutton(panel, text='Задати довжину масивів',variable=var, value=1, font=('Calibri', 25, 'bold'), bg='#977AF9',
                       fg='black', state=tk.NORMAL, width=22, activebackground='#760598', relief=tk.RAISED,
                       bd='5', command=select_method).grid(row=1, column=0, pady=(10, 10), padx=(15, 15))

radb2 = tk.Radiobutton(panel, text='Згенерувати графіки',variable=var, value=2, font=('Calibri', 25, 'bold'), bg='#977AF9',
                       fg='black', state=tk.NORMAL, width=22, activebackground='#760598', relief=tk.RAISED,
                       bd='5', command=select_method).grid(row=2, column=0, pady=(10, 10), padx=(15, 15))

#win3
labelfr2 = tk.Label(panel3, text="Генерація графіків:", font=('Calibri', 25, 'bold'), bg='#252425',
                    fg='white')

button_generate1 = tk.Button(panel3, text='Згенерувати практичний графік', font=('Calibri', 25, 'bold'), bg='#977AF9', relief=tk.RAISED,
                        activebackground='#760598', bd=5, fg='white', command=plot_sorting_times)
button_generate2 = tk.Button(panel3, text='Згенерувати теоретичний графік', font=('Calibri', 25, 'bold'), bg='#977AF9', relief=tk.RAISED,
                          activebackground='#760598', bd=5, fg='white', command=plot_complexity)
#win2
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

#labels win2
labelfr1 = tk.Label(panel2, text="Задайте довжину для кожного масиву:", font=('Calibri', 25, 'bold'), bg='#252425',
                    fg='white')
M1 = tk.Label(panel2, text='1 =', bg='#252425', fg='white', font=('Calibri', 20, 'bold'))
M2 = tk.Label(panel2, text='2 =', bg='#252425', fg='white', font=('Calibri', 20, 'bold'))
M3 = tk.Label(panel2, text='3 =', bg='#252425', fg='white', font=('Calibri', 20, 'bold'))
M4 = tk.Label(panel2, text='4 =', bg='#252425', fg='white', font=('Calibri', 20, 'bold'))
M5 = tk.Label(panel2, text='5 =', bg='#252425', fg='white', font=('Calibri', 20, 'bold'))
M6 = tk.Label(panel2, text='6 =', bg='#252425', fg='white', font=('Calibri', 20, 'bold'))
M7 = tk.Label(panel2, text='7 =', bg='#252425', fg='white', font=('Calibri', 20, 'bold'))
M8 = tk.Label(panel2, text='8 =', bg='#252425', fg='white', font=('Calibri', 20, 'bold'))
M9 = tk.Label(panel2, text='9 =', bg='#252425', fg='white', font=('Calibri', 20, 'bold'))
M10 = tk.Label(panel2, text='10 =', bg='#252425', fg='white', font=('Calibri', 20, 'bold'))

#Entry win2
vM1 = tk.Entry(panel2, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')
vM2 = tk.Entry(panel2, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')
vM3 = tk.Entry(panel2, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')
vM4 = tk.Entry(panel2, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')
vM5 = tk.Entry(panel2, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')
vM6 = tk.Entry(panel2, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')
vM7 = tk.Entry(panel2, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')
vM8 = tk.Entry(panel2, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')
vM9 = tk.Entry(panel2, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')
vM10 = tk.Entry(panel2, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')
length_entries = [vM1, vM2, vM3, vM4, vM5, vM6, vM7, vM8, vM9, vM10]

#Button win2
button_load = tk.Button(panel2, text='Завантажити дані з файлу', font=('Calibri', 25, 'bold'), bg='#977AF9', width=22,
                        relief=tk.RAISED, activebackground='#760598', bd=5, fg='white', command=load_data)
button_clear = tk.Button(panel2, text='Очистити', font=('Calibri', 25, 'bold'), bg='#977AF9', width=22,
                         relief=tk.RAISED, activebackground='#760598', bd=5, fg='white', command=clear_entries)
win.mainloop()