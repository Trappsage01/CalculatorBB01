# Создание калькулятора от Trappsage01

import tkinter as tk

# Импортируем библиотеку для интерфейса 

def add_digit(digit):
    '''Функция для отображения строки ввода'''
    value = calc.get()
    if value[0] == '0' and len(value) ==1:
        value = value[1:]
    calc.delete(0,tk.END)
    calc.insert(0,value+digit)

def add_operation(operation):
    '''Функция для вычисления строки ввода'''
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END) 
    calc.insert(0, value+operation)

#Функция работа с равно
def calculate():
    value = calc.get()
    if value[-1] in '+-*/':
        value = value+value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, eval(value))

def clear():
    calc.delete(0, tk.END)
    calc.insert(0, 0)


#Функция для кнопки
def make_digit_button(digit):
    return tk.Button(text=digit, bd=5,font=('Arial', 12), command=lambda : add_digit(digit))
#Функция для операции кнопки
def make_operation_button(operation):
    return tk.Button(text=operation, bd=5,font=('Arial', 12), fg='#ff0000',
                    command=lambda : add_operation(operation)) 
#Функция вычисления 
def make_calc_button(operation):
    return tk.Button(text=operation, bd=5,font=('Arial', 12), fg='#ff0000',
                    command=calculate)
#Функция сброса
def make_clear_button(operation):
    return tk.Button(text=operation, bd=5,font=('Arial', 12), fg='#ff0000',
                    command=clear)

def press_key(event):
    print(event.char)
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-/*':
        add_operation(event.char)


#Создаем окно приложения
win = tk.Tk()
win.geometry(f"240x270+50+50")
win['bg'] = '#000000'
win.title('Калькулятор Trappsage01')

win.bind('<Key>', press_key)


calc = tk.Entry(win, justify=tk.RIGHT,font=('Arial', 15), width=15)
calc.insert(0,'0')
calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5)

#Кнопка - Функция благодоря  make_digit_button
make_digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5) 
make_digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5) 
make_digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5) 
make_digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, stick='wens', padx='5', pady='5')
make_operation_button('-').grid(row=2, column=3, stick='wens', padx='5', pady='5')
make_operation_button('/').grid(row=3, column=3, stick='wens', padx='5', pady='5')
make_operation_button('*').grid(row=4, column=3, stick='wens', padx='5', pady='5')

make_calc_button('=').grid(row=4, column=2, stick='wens', padx='5', pady='5')
make_clear_button('AC').grid(row=4, column=1, stick='wens', padx='5', pady='5')

#Размеры колонок
win.grid_columnconfigure(0,minsize=60)
win.grid_columnconfigure(1,minsize=60)
win.grid_columnconfigure(2,minsize=60)
win.grid_columnconfigure(3,minsize=60)

#Размеры рядов
win.grid_rowconfigure(1,minsize=60)
win.grid_rowconfigure(2,minsize=60)
win.grid_rowconfigure(3,minsize=60)
win.grid_rowconfigure(4,minsize=60)




win.mainloop()