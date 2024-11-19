from tkinter import *


class Variables:
    variable1 = 0
    variable2 = 0

def click1():
    def cmd1():
        lbl1 = Label(window, width=50, height=4, background='#FFF68F', font=("Arial", 12), )
        lbl1.grid(row=1, column=2)
        lbl1['text'] = f'{Variables.variable1}, {Variables.variable2} \n'
    def cmd2():
        lbl0 = Label(window,text='поставьте знак "-"', width=50, height=5, font=("Arial", 14), background='#FFE4E1').grid(row=1, column=2)
        entr1 = Entry(window, width=10)
        entr1.grid(row=2, column=2)
        entr2 = Entry(window, width=10)
        entr2.grid(row=3, column=2)
        b2 = Button(window, text='Сохранить', width=30, height=3, font=("Arial", 14))
        b2.config(command=save_numb)
        b2['bg'] = '#EE82EE'
        b2['fg'] = '#0A0A0A'
        b2.grid(row=4, column=2)
    def cmd3():
        lbl1 = Label(window, width=50, height=4, background='#FFF68F',  font=("Arial", 12), )
        lbl1.grid(row=1, column=2)
        lbl1['text'] = f'{int(Variables.variable1) + int(Variables.variable2)} \n'
    def cmd4():
        lbl1 = Label(window, width=50, height=4, background='#FFF68F',  font=("Aria l", 12), )
        lbl1.grid(row=1, column=2)
        lbl1['text'] = f'{max(int(Variables.variable1), int(Variables.variable2))} \n'


    window = Tk()
    window.title("2")
    text_button = ['Вывести числа на экран',  'Изменить введенные числа', 'Сумма введенных чисел','Найти наибольшее значение']
    r2 = 0
    func = [cmd1, cmd2, cmd3, cmd4]
    for i2 in range(len(text_button)):
        b21 = Button(window, text=f'{text_button[i2]}', width=40, height=3, font=("Arial", 14), background='#BFEFFF', foreground='#0A0A0A')
        cmd = lambda x=i2: func[x]()
        b21.config(command=cmd)
        b21.grid(row=0 + r2, column=0)
        r2 += 1
    window.mainloop()

def save_numb():
    root.withdraw()
    Variables.variable1 = entr1.get()
    Variables.variable2 = entr2.get()
    click1()
    print(Variables.variable1, Variables.variable2)
root = Tk()
root.minsize(1050, 1050)
root['bg'] = '#FFE4E1'
lbl0 = Label(root,text='Введите два числа', width=50, height=5, font=("Arial", 14), background='#FFE4E1').place(relx=.5, rely=.3, anchor="c")
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




