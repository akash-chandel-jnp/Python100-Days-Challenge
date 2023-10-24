from quiz_brain import QuizBrain
from quest_bank import question_bank

# print(question_bank)
# print(question_bank[0].text)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    # creating a new quiz
    quiz.next_question()

print("You have completed the Quiz.")
print(f"Your final score is : {quiz.score}/{len(question_bank)}")
