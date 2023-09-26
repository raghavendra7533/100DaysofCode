from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

if not quiz.still_has_questions():
    print("You've completed the quiz")
    if quiz.score > 10:
        print("Awesome!")
        print(f"Your final score was {quiz.score}/{quiz.question_number}")
    else:
        print("Better luck next time!")