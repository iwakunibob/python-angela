class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
    def printQuestion(self):
        print(f"Is this true or false {self.text}")
    def printAnswer(self):
        print(self.answer)
new_q = Question("2+3=5", "True")

new_q.printQuestion()
new_q.printAnswer()

