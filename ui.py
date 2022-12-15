import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 16, 'italic')


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.root = tk.Tk()
        self.root.title('Quizzler')
        self.root.config(background=THEME_COLOR, padx=20, pady=20)
        
        self.score_label = tk.Label(text='Score: 0', bg=THEME_COLOR,
                                    fg='white', font=('Arial', 12, 'normal'))
        self.score_label.grid(column=1, row=0)

        self.canvas = tk.Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text='Question Placeholder',
                                                    font=FONT, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        img_true = tk.PhotoImage(file='images/true.png')
        self.green_button = tk.Button(image=img_true, borderwidth=0, command=self.answer_true,
                                    highlightthickness=0, activebackground='green')
        self.green_button.grid(column=0, row=2, padx=20, pady=20)

        img_false = tk.PhotoImage(file='images/false.png')
        self.red_button = tk.Button(image=img_false, borderwidth=0, command=self.answer_false,
                                    highlightthickness=0, activebackground='red')
        self.red_button.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()

        self.root.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score_label.config(text=f'Score: {self.quiz.score}')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.button_state(tk.ACTIVE)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.button_state(tk.DISABLED)

    def answer_true(self):
        answer = 'True'
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)

    def answer_false(self):
        answer = 'False'
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.button_state(tk.DISABLED)
        if is_right:
            self.canvas.config(bg='green')
            self.root.after(1000, func=self.get_next_question)
        else:
            self.canvas.config(bg='red')
            self.root.after(1000, func=self.get_next_question)

    def button_state(self, state: str):
        self.green_button.config(state=state)
        self.red_button.config(state=state)
         
