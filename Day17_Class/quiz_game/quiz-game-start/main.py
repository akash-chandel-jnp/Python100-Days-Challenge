from data import question_data
from question_model import  Question

question_bank = []

for q in question_data:
    quest = q["text"]
    ans = q["answer"]

    new_question = Question(quest, ans)
    question_bank.append(new_question)


# print(question_bank)
print(question_bank[0].text)
print(question_bank[0].answer)



