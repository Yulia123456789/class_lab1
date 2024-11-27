
from tkinter import *


class Variable:

    def __init__(self, variable1, variable2):
        self.variable1 = variable1
        self.variable2 = variable2

    def sum_variable(self):
        return self.variable1 + self.variable2

    def max_variable(self):
        return max(self.variable1, self.variable2)

    def change_var(self, variable1, variable2):

        self.variable1 = variable1
        self.variable2 = variable2

obj = Variable(0, 0)

def save_numb():
    new_variable1 = entr1.get()
    new_variable2 = entr2.get()
    obj.variable1, obj.variable2 = int(new_variable1), int(new_variable2)
    print(obj.variable1, obj.variable2)
    click1()

def text_box_func(message):

    text_box = Text(root, width=50, height=10, font=("Arial", 10), background='#FFE4E1', foreground='#0A0A0A')

    text_box.grid(row=3, column=0, ipadx=10, ipady=10, padx=10, pady=10, columnspan= 2)
    text_box.insert('end', message)
    text_box.config(state='disabled')

def click1():
    def cmd1():
        lbl1 = Label(window, width=50, height=4, background='#FFF68F', font=("Arial", 12), )
        lbl1.grid(row=1, column=2)
        lbl1['text'] = f'{obj.variable1}, {obj.variable2} \n'

    def cmd2():
        def save_numb2():
            root1.withdraw()
            if entr11 != '-' and entr21 != '-':
                new_variable1 = entr11.get()
                new_variable2 = entr21.get()
                obj.variable1, obj.variable2 = int(new_variable1), int(new_variable2)
            elif entr11 == '-':
                new_variable2 = entr21.get()
                obj.variable2 = int(new_variable2)
            elif entr21 == '-':
                new_variable1 = entr11.get()
                obj.variable1 = int(new_variable1)
            print(obj.variable1, obj.variable2)

        root1 = Tk()
        root1.minsize(1050, 1050)
        root1.title = 'Ввод чисел'
        root1['bg'] = '#FFE4E1'
        lbl0 = Label(root1, text='Введите два числа, если число без изменений "-"', width=50, height=5, font=("Arial", 14),
                     background='#FFE4E1').place(relx=.5, rely=.3, anchor="c")
        entr11 = Entry(root1, width=10)
        entr11.place(relx=.5, rely=.4, anchor="c")
        entr21 = Entry(root1, width=10)
        entr21.place(relx=.5, rely=.5, anchor="c")

        b2 = Button(root1, text='Сохранить', width=30, height=3, font=("Arial", 14))
        b2.config(command=save_numb2)
        b2['bg'] = '#EE82EE'
        b2['fg'] = '#0A0A0A'
        b2.place(relx=.5, rely=.6, anchor="c")
        root1.mainloop()


    def cmd3():
        lbl1 = Label(window, width=50, height=4, background='#FFF68F', font=("Arial", 12), )
        lbl1.grid(row=1, column=2)
        lbl1['text'] = f'{obj.sum_variable()} \n'

    def cmd4():
        lbl1 = Label(window, width=50, height=4, background='#FFF68F', font=("Aria l", 12), )
        lbl1.grid(row=1, column=2)
        lbl1['text'] = f'{obj.max_variable()} \n'

    window = Tk()
    window.title("2")
    text_button = ['Вывести числа на экран', 'Изменить введенные числа', 'Сумма введенных чисел',
                       'Найти наибольшее значение']
    r2 = 0
    func = [cmd1, cmd2, cmd3, cmd4]
    for i2 in range(len(text_button)):
        b21 = Button(window, text=f'{text_button[i2]}', width=40, height=3, font=("Arial", 14),
                         background='#BFEFFF', foreground='#0A0A0A')
        cmd = lambda x=i2: func[x]()
        b21.config(command=cmd)
        b21.grid(row=0 + r2, column=0)
        r2 += 1
    window.mainloop()


root = Tk()
root.minsize(1050, 1050)
root.title = 'Ввод чисел'
root['bg'] = '#FFE4E1'
lbl0 = Label(root, text='Введите два числа', width=50, height=5, font=("Arial", 14),
                 background='#FFE4E1').place(relx=.5, rely=.3, anchor="c")
entr1 = Entry(root, width=10)
entr1.place(relx=.5, rely=.4, anchor="c")
entr2 = Entry(root, width=10)
entr2.place(relx=.5, rely=.5, anchor="c")

b2 = Button(root, text='Сохранить', width=30, height=3, font=("Arial", 14))
b2.config(command=save_numb)
b2['bg'] = '#EE82EE'
b2['fg'] = '#0A0A0A'
b2.place(relx=.5, rely=.6, anchor="c")
root.mainloop()
root.withdraw()









