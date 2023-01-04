from question_model import Question
from data import question_data, question_data1, question_data2
from quiz_brain import QuizBrain

question_bank = []
for i in range(len(question_data)):
    pair = Question(question_data[i]["question"], question_data[i]["correct_answer"])
    question_bank.append(pair)

question_bank1 = []
for i in range(len(question_data1)):
    pair = Question(question_data1[i]["text"], question_data1[i]["answer"])
    question_bank1.append(pair)

question_bank2 = []
for i in range(len(question_data2)):
    pair = Question(question_data2[i]["question"], question_data2[i]["correct_answer"])
    question_bank2.append(pair)

# Testing
# for i in range(len(question_bank)-1):
#     print(question_bank[i].text)
#     print(question_bank[i].answer)
#     print(20*"*")

# print(question_bank[1].text)
# print(question_bank[1].answer)
# print(question_bank)

quiz = QuizBrain(question_bank)
quiz1 = QuizBrain(question_bank1)
quiz2 = QuizBrain(question_bank2)

while quiz2.still_has_questions():  # if quiz still has questions remaining
    quiz2.next_question()

print(f"You've completed the quiz.\nYour final score was {quiz2.score}/{len(question_bank2)}.")
