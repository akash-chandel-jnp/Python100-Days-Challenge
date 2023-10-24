# from quest_bank import question_bank


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):

        current_question = self.question_list[self.question_number]  # contains both question text and question answer
        correct_ans = current_question.answer
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}) : {current_question.text} (True / False) : ")
        self.check_answer(self.question_number, user_ans, current_question.answer)

    def check_answer(self, quest_no, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1

        else:
            print("That's wrong!")

        print(f"Your current score is {self.score}/{quest_no}")

        print(f"The correct answer is : {correct_ans}\n")

# quiz = QuizBrain(question_bank)
# quiz.next_question()
