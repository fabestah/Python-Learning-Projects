class QuizBrain:
    def __init__(self, q_list):
        self.q_num = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        q = self.q_list[self.q_num]
        self.q_num += 1
        print(f"{self.q_num}. Question: {q.text} (True/False)?")
        u_answer = input("Your answer: ")
        self.check_answer(u_answer, q.answer)

    def check_answer(self, u_answer, answer):
        if u_answer.lower() == answer.lower():
            self.score += 1
            print(
                f"Right! ✔️\nCorrect answer was: {answer}\nYour score: {self.score}\n"
            )
            return True
        else:
            self.score -= 1
            print(f"Wrong! ❌\nCorrect answer was: {answer}\nYour score: {self.score}\n")

    def still_has_questions(self):
        return self.q_num >= len(self.q_list)
