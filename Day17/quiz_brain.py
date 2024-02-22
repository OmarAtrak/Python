class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1} {current_question.text} (True/False)? ").lower().title()
        self.check_answer(answer)

        print(f"Your current score is: {self.score}/{self.question_number + 1}")
        self.question_number += 1
        print()

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer):
        if answer == self.question_list[self.question_number].answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {self.question_list[self.question_number].answer}")
