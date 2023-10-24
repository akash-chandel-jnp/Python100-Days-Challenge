from data import question_data
from question_model import Question

question_bank = []  # a list containing question objects , which in turn contain two attributes - a)q_text b) q_answer

for q in question_data:
    quest = q["question"]
    ans = q["correct_answers"]

    # creating question object for every iteration and appending to the question bank list
    new_question = Question(quest, ans)
    question_bank.append(new_question)
