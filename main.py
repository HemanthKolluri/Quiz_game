from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank=[]
for i in question_data:
  question_text=i["text"]
  question_answer=i["answer"]
  new_question= Question(question_text,question_answer)
  question_bank.append(new_question)
quiz=Quizbrain(question_bank)
while quiz.still_has_question():
  quiz.next_question()
print("You have completed you quiz")
print(f"Your Final score is {quiz.score}/{quiz.question_no}")