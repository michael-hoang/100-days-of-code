from question_model import Question
from data import question_data, question_data2
from quiz_brain import QuizBrain

question_bank = []  # List of question objects

# Extract question and answer string from data.py to pass through as arguments when
# creating instance/object from the class Question.
for i in question_data2:
    text_value = i['question']
    answer_value = i['correct_answer']

    question = Question(text_value, answer_value) 
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

final_score = f"{quiz.score}/{quiz.question_number}"
print("You've completed the quiz.")
print(f"Your final score was: {final_score}")
