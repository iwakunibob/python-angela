class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        select_answer = input(f"Q.{self.question_number}: {current_question.text} (T or F) ").lower()
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self):
        skip

