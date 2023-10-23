class Question:
    def __init__(self,q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


new_quest = Question("What is the atomic number of Carbon ?", "6")
print(new_quest.text)
print(new_quest.answer)

