class QuizBrain:
    def __init__(self, ques_list):
        self.ques_no = 0
        self.ques_list = ques_list
        self.score = 0

    def next_question(self):
        current_question = self.ques_list[self.ques_no]
        self.ques_no += 1
        user_answer = input(f"Q.{self.ques_no}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.ques_no < len(self.ques_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You are right!.")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"Correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.ques_no}")
        print("\n")
