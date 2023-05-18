from tkinter import *
import random

window = Tk()
window.geometry("600x600")
window.title('Guess the number game')

entry_str = StringVar()


class Output:
    
    def __init__(self, w, h, bg, j, username='', stage='greeting'):
        self.v = StringVar()
        self.username = username
        self.stage = stage
        self.number = 0
        self.count = 0
        self.label = Label(window, textvariable=self.v, 
                           width=w, height=h, background=bg,
                           justify=j, anchor='w', fg='white')

    def place_self(self, x, y):
        self.label.place(x=x, y=y)
    
    def talk(self, t):
        self.v.set(t)

    def rand_num(self):
        self.number = random.randint(1, 100)

    def start(self):
        self.talk('Hello user! What is your name?')

    def counting(self):
        self.count += 1

    def get_number(self, number):
        if self.username == '' and self.stage == 'greeting':
            self.username = number
            self.rand_num()
            self.stage = 'game'
            self.talk(f"Ok, {self.username}, I put up some number for you to guess. You have 10 tries!")
            entry_str.set('')
        elif self.stage == 'game' and not number.isdigit():
            self.talk('You have to print number!')
            entry_str.set('')
        elif self.number != int(number) and self.count >= 10 and self.stage == 'game':
            self.talk('You ran out of tries. And you loose.')
            entry_str.set('')
        elif self.number == int(number) and self.count <= 10 and self.stage == 'game':
            self.talk('Right in the spot! You got the number I have guessed!')
            self.stage = 'greeting'
            self.username = ''
            self.count = 0
            entry_str.set('')
        elif self.number < int(number) and self.stage == 'game' and self.count < 10:
            self.talk('It`s too great, try again') 
            self.counting()
            entry_str.set('')
        elif self.number > int(number) and self.stage == 'game' and self.count < 10:
            self.talk('It`s too less, try again') 
            self.counting()
            entry_str.set('')

    

    


l1 = Output(60, 5, 'blue', 'center')
l2 = Entry(window, textvariable=entry_str, selectbackground='blue')
submit_button = Button(window, 
                       text="submit", 
                       bg="blue", 
                       fg="white", 
                       command=lambda: l1.get_number(l2.get()))
l1.place_self(50, 50)
l2.place(x=250-20, y=170)
submit_button.place(x=250-20, y=270)
l1.start()
window.mainloop()