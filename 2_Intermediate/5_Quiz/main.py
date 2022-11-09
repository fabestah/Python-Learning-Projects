from question_model import Question
from data import q_data
from quiz_brain import QuizBrain


q_bank = []
for q in q_data:
    q = Question(q["question"], q["correct_answer"])
    q_bank.append(q)

game_end = False
quiz = QuizBrain(q_bank)

while not game_end:
    quiz.next_question()
    game_end = quiz.still_has_questions()

print(f"You completed the quiz! 🎉\nFinal Score: {quiz.q_num}/{quiz.score}")
