class QuizBrain:
    """A simple attempt to model a Quiz Brain"""

    def __init__(self, q_list):
        """Initialize number of questions and question list attributes."""
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """Returns True if there are still questions remaining in the list"""
        length_of_quiz = len(self.question_list)
        return self.question_number < length_of_quiz # This evaluates to True or False

    def next_question(self):
        # Extract question object from self.question_list (question_bank).
        question_object = self.question_list[self.question_number]
        # Extract question.text attribute containing the question to display to user.
        question_text = question_object.text
        # Increment self.question_number by 1 to accurately display question number to user
        # and to prepare for next question in the list. 
        self.question_number += 1 
        user_answer = input(f"Q.{self.question_number}: {question_text} (True/False): ")
        question_answer = question_object.answer
        self.check_answer(user_answer, question_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
