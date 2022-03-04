from tkinter import *
from conenct_to_database import *


class Interface(Canvas):
    def __init__(self):
        super().__init__(
            width=500,
            height=500,
            highlightthickness=0
        )
        self.create_objects()

    def submit_date(self):
        data_set = []
        data_set.append(self.quest.get())
        data_set.append(self.answer_1.get())
        data_set.append(self.answer_2.get())
        data_set.append(self.name_user.get())
        db = DB()
        db.add_dates(data_set)

    def create_objects(self):
        self.quest = Entry(main_window)
        self.answer_1 = Entry(main_window)
        self.answer_2 = Entry(main_window)
        self.name_user = Entry(main_window)
        self.button_submit = Button(main_window,text="submit date",command=self.submit_date)

        self.quest.pack(padx=20,pady=20)
        self.answer_1.pack(padx=20,pady=20)
        self.answer_2.pack(padx=20,pady=20)
        self.name_user.pack(padx=20,pady=20)
        self.button_submit.pack(padx=20,pady=20)


main_window = Tk()
main_window.title("Game")
main_window.resizable(False, False)
interface = Interface()
interface.pack()
main_window.mainloop()
