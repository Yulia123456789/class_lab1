from tkinter import *

class Train:

    def __init__(self, name_destination, train_number, departure_time):
        self.name_destination = name_destination
        self.train_number = train_number
        self.departure_time = departure_time
    def display_info(self):
        return f'название пункта назначения: {self.name_destination}, Номер поезда: {self.train_number},  Время отправления: {self.departure_time}'
    def get_values(self):
        return (self.name_destination, self.train_number, self.departure_time)


trains = [
    Train("Москва", 101, "12:30"),
    Train("Москва", 103, "10:00"),
    Train("Владивосток", 102, "14:15"),
    Train("Новосибирск", 104, "16:20"),
    Train("Екатеринбург", 105, "09:45")
]

def text_box_func(message):

    text_box = Text(root, width=90, height=10, font=("Arial", 10), background='#FFE4E1', foreground='#0A0A0A')

    text_box.grid(row=3, column=0)
    text_box.insert('end', message)
    text_box.config(state='disabled')

def show_write_number_train():
    def show_range_number_card():
        number_train = entr1_range.get()

        message = ""
        for train in trains:
            if int(number_train) == train.train_number:
                message += f'{train.display_info()} \n'
        print(message)
        text_box_func(message)

    root1 = Tk()
    root1.minsize(1050, 1050)
    root1['bg'] = '#FFE4E1'
    lbl0_range = Label(root1, text='Введите номер поезда', width=50, height=2, font=("Arial", 14), background='#FFE4E1')
    lbl0_range.grid(row=0, column=2, rowspan=1)
    entr1_range = Entry(root1, width=30)
    entr1_range.grid(row=1, column=2, rowspan=1)

    b2_range = Button(root1, text='Сохранить', width=20, height=2, font=("Arial", 10), background='#EE82EE', foreground='#0A0A0A')
    b2_range.config(command=show_range_number_card)
    b2_range.grid(row=4, column=2, rowspan=1)
    root1.mainloop()

def show_train():
    message = ""
    inf_abn = []
    for train in trains:
        inf_abn.append(train.get_values())
    inf_abn.sort(key=lambda train1: train1[1])

    for train2 in inf_abn:
        v = ''
        for j in train2:
            v += str(j) + "  "
        message += v + '\n'
    text_box_func(message)

def show_train_destination():
    message = ""
    destination_name = ''
    inf_abn = []
    for train in trains:
        inf_abn.append(train.get_values())
    inf_abn.sort(key=lambda train1: (train1[0], train1[1]))

    for train2 in inf_abn:
        v = ''
        for j in train2:
            v += str(j) + "  "
        message += v + '\n'
    text_box_func(message)




root = Tk()
root.title("Лабораторные")
root['bg'] = '#FFE4E1'
r1 = 0
funcn = [show_train, show_write_number_train, show_train_destination]
text_button = ['Упорядочить элементы по номерам поездов', 'Вывести информации о поезде по его номеру', 'Сортировки массива по пункту назначения']
for i1 in range(1, 4):
    b1 = Button(root, text=f'{text_button[i1 - 1]}', width=80, height=3, font=("Arial", 14), background='#FFB6C1', foreground='#0A0A0A')
    cmd = lambda x=i1: funcn[x - 1]()
    b1.config(command=cmd)
    b1.grid(row=0 + r1, column=0)
    r1 += 1

root.mainloop()