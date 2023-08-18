THEME_COLOR = "#375362"
from tkinter import *

class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text='Score: 0', fg='white', bg=THEME_COLOR, font=5)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=320, height=250, bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=270,
            text='Some Question Text',
            font=('Arial', 20, 'italic'),
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.right_image = PhotoImage(file='images/true.png')
        self.right_button = Button(image=self.right_image, highlightthickness=0, border=0, command=self.right_pressed)
        self.right_button.grid(column=0, row=2)

        self.wrong_image = PhotoImage(file='images/false.png')
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0, border=0, command=self.wrong_pressed)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window. mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have completed the Quiz!')
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')
    def right_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def wrong_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)