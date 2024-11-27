from tkinter import *


class Student():
    def __init__(self, surname, initials, group_number, grade):
        self.surname = surname
        self.initials = initials
        self.group_number = group_number
        self.grade = grade

    def avrg_grade(self):
        avrg = sum(self.grade) / len(self.grade)
        full_inf = [self.surname, self.initials, self.group_number, self.grade, avrg]
        return full_inf


    def grade_4_5(self):
        if 2 not in self.grade and 3 not in self.grade:
            return f"Фамилия студента: {self.surname}, Номер группы студента: {self.group_number}"


students = [
    Student("Иванов", "И.И.", 11, [4, 5, 4, 5, 4]),
    Student("Петров", "П.П.", 12, [5, 5, 5, 4, 4]),
    Student("Сидоров", "С.С.", 13, [3, 3, 3, 4, 5]),
    Student("Кузнецов", "К.К.", 14, [4, 4, 4, 4, 4]),
    Student("Попов", "П.П.", 15, [5, 4, 5, 5, 5]),
    Student("Смирнов", "С.С.", 12, [3, 2, 4, 3, 5]),
    Student("Захаров", "З.З.", 14, [4, 5, 4, 5, 4]),
    Student("Морозов", "М.М.", 13, [3, 4, 3, 3, 4]),
    Student("Новиков", "Н.Н.", 15, [5, 5, 5, 5, 5]),
    Student("Васильев", "В.В.", 11, [2, 3, 3, 4, 4])
]


def sort_name():
    text_box = Text(window, width=50, height=10, font=("Arial", 14),
                     background='#FFE4E1', foreground='#0A0A0A')
    text_box.grid(row=2, column=0)
    full_inf = []
    for student in students:
        full_inf.append(student.avrg_grade())
    full_inf.sort(key=lambda student2: student2[-1])
    message = ""
    for i in full_inf:
        v = ''
        for j in i:
            v += str(j) + "  "
        message += v + '\n'
    text_box.insert('end', message)
    text_box.config(state='disabled')

def show_name_students_4_5():

    text_box = Text(window, width=50, height=10, font=("Arial", 14),
                     background='#FFE4E1', foreground='#0A0A0A')
    text_box.grid(row=2, column=0)
    message = ""
    for student in students:
        if student.grade_4_5():
            message += f'{student.grade_4_5()} \n'

    text_box.insert('end', message)

    text_box.config(state='disabled')

window = Tk()
window.minsize(1050, 1050)
window ['bg'] = '#FFE4E1'

b21 = Button(window, text='Вывести информацию \n о студентах с оценками 4 и 5', width=50, height=4, font=("Arial", 14),
                     background='#FFB6C1', foreground='#0A0A0A')
b21.config(command=show_name_students_4_5)
b21.grid(row=0, column=0)
b22 = Button(window, text='Упорядочить записи по возрастанию среднего балла', width=50, height=4,font=("Arial", 14), background='#FFB6C1', foreground='#0A0A0A')
b22.config(command=sort_name)
b22.grid(row=1, column=0)
window.mainloop()