from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in range(len(question_data)):
    pair = Question(question_data[i]["text"], question_data[i]["answer"])
    question_bank.append(pair)

# Testing
# for i in range(len(question_bank)-1):
#     print(question_bank[i].text)
#     print(question_bank[i].answer)
#     print(20*"*")

# print(question_bank[1].text)
# print(question_bank[1].answer)
# print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():  # if quiz still has questions remaining
    quiz.next_question()
