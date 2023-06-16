from tkinter import *
from random import *

class Dice:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("305x449")
        self.root.title("Dice Game")
        self.frame = Frame(self.root)
        self.frame.pack()

        self.user_a_count = IntVar()
        self.user_b_count = IntVar()
        self.chance = StringVar()
        self.dice_result = StringVar()
        self.player1_name = StringVar()
        self.player2_name = StringVar()
        self.play_count = 1

    def widgets(self):
        self.usr_a = Label(self.frame, text="Enter User A Name:", font=("Roboto", 10))
        self.usr_a_name = Entry(self.frame, textvariable=self.player1_name, font=("Roboto", 10), width=13)
        self.usr_b = Label(self.frame, text="Enter User B Name:", font=("Roboto", 10))
        self.usr_b_name = Entry(self.frame, textvariable=self.player2_name, font=("Roboto", 10), width=13)
        self.submit = Button(self.frame, text="Submit", command=self.widgets2, font=("Roboto", 10))

        self.usr_a.grid(row=1, column=0)
        self.usr_a_name.grid(row=1, column=1)
        self.usr_b.grid(row=2, column=0)
        self.usr_b_name.grid(row=2, column=1)
        self.submit.grid(row=3, column=1)

        self.frame.place(relx=0.4, rely=0.4, anchor="center")

    def widgets2(self):
        self.a = self.player1_name.get()
        self.b = self.player2_name.get()

        self.usr_a.destroy()
        self.usr_b.destroy()
        self.usr_a_name.destroy()
        self.usr_b_name.destroy()
        self.submit.destroy()

        self.usr_a_label = Label(self.frame, text=self.a, font=("Roboto", 10))
        self.usr_b_label = Label(self.frame, text=self.b, font=("Roboto", 10))

        self.btn = Button(self.frame, text="Click to Roll the Dice", command=self.play, font=("Roboto", 10))
        self.turn = Message(self.frame, textvariable=self.chance, width=505, font=("Roboto", 10))
        self.result = Message(self.frame, textvariable=self.dice_result, width=310, font=("Roboto", 10))

        self.usra_msg = Message(self.frame, textvariable=self.user_a_count, width=20, font=("Roboto", 10))
        self.usrb_msg = Message(self.frame, textvariable=self.user_b_count, width=20, font=("Roboto", 10))

        self.usr_a_label.grid(row=1, column=0)
        self.usr_b_label.grid(row=2, column=0)

        self.usra_msg.grid(row=1, column=1)
        self.usrb_msg.grid(row=2, column=1)

        self.result.grid(row=3, column=0)
        self.turn.grid(row=4, column=0, columnspan=3)
        self.btn.grid(row=5, column=0, columnspan=3)

        self.frame.place(relx=0.4, rely=0.4, anchor="center")
        self.current_playing()

    def current_playing(self):
        if self.play_count % 2 != 0:
            self.chance.set(f"Now {self.a}'s Turn,")
        else:
            self.chance.set(f"Now {self.b}'s Turn, ")

    def rolling_dice(self):
        self.res = randint(1, 6)
        if self.play_count % 2 != 0:
            self.dice_result.set(f"{self.a} got "+str(self.res))
        else:
            self.dice_result.set(f"{self.b} got "+str(self.res))
    def play(self):
        self.rules()
        self.rolling_dice()
        if self.play_count % 2 != 0:
            a_count = self.user_a_count.get() + self.res
            self.user_a_count.set(a_count)
        else:
            b_count = self.user_b_count.get() + self.res
            self.user_b_count.set(b_count)
        self.play_count += 1
        self.current_playing()

    def rules(self):
        if self.user_a_count.get() >= 25:
            self.usr_a_label.destroy()
            self.usr_b_label.destroy()
            self.usra_msg.destroy()
            self.usrb_msg.destroy()
            res = Label(self.frame, text=f"{self.a} won the game", font=("Roboto",15))
            res.grid(row=6, column=0)
            self.btn.destroy()
            self.turn.destroy()
            self.result.destroy()

        if self.user_b_count.get() >= 25:
            self.usr_a_label.destroy()
            self.usr_b_label.destroy()
            self.usra_msg.destroy()
            self.usrb_msg.destroy()
            res = Label(self.frame, text=f"{self.b} won the game", font=("Roboto",15))
            res.grid(row=6, column=0)
            self.btn.destroy()
            self.turn.destroy()
            self.result.destroy()

    def result(self):
        self.widgets()
        self.root.mainloop()


obj = Dice()
obj.result()
