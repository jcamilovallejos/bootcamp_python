class QuizBrain:


    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.correct_answers = 0
        self.wrong_answers = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_answer = input(f"Q.{self.question_number} {current_question.text} (T/F)")
        self.check_answer(current_question.answer, q_answer)

    def still_has_question(self):
        try:
            self.question_list[self.question_number]
        except IndexError as e:
            print(f"It is over... You result: {self.correct_answers} Correct and {self.wrong_answers} Incorrect")
            return False
        return True

    def check_answer(self, c_answer, q_answer):
        if (c_answer == "True" and q_answer == "t") or (c_answer == "False" and q_answer == "f"):
            self.correct_answers += 1
        else:
            self.wrong_answers += 1






