from question_model import Question
from data import question_data1
from data import question_data2
from data import question_data3
from data import question_data4
from data import question_data5
from quiz_brain import QuizBrain
import winsound

question_bank = []  #user의 답 기록?
def make_instance1():
    for question in question_data1:  #qusetion_data => 질문, 답 딕셔너리
        text = question["text"]
        answer = question["answer"]
        question_bank.append(Question(text, answer))  #리스트에 추가

def make_instance2():
    for question in question_data2:  
        text = question["text"]
        answer = question["answer"]
        question_bank.append(Question(text, answer)) 

def make_instance3():
    for question in question_data3:  
        text = question["text"]
        answer = question["answer"]
        question_bank.append(Question(text, answer)) 

def make_instance4():
    for question in question_data4:  
        text = question["text"]
        answer = question["answer"]
        question_bank.append(Question(text, answer)) 


def make_instance5():
    for question in question_data5:  
        text = question["text"]
        answer = question["answer"]
        question_bank.append(Question(text, answer)) 

#question_bank = []  #user의 답 기록?
print("(2020년 3회) 정보처리기사 필기 기출문제")
print("1과목 - 소프트웨어 설계")
print("2과목 - 소프트웨어 개발")
print("3과목 - 데이터베이스 구축")
print("4과목 - 프로그래밍 언어 활용")
print("5과목 - 정보시스템 구축 관리")

num=int(input("응시할 과목을 고르시오(1,2,3,4,5):"))
if num==1:
    make_instance1()
elif num==2:
    make_instance2()
elif num==3:
    make_instance3()
elif num==4:
    make_instance4()
elif num==5:
    make_instance5()
else:
    print("잘못 입력하셨습니다.")

quiz = QuizBrain(question_bank)  #객체 생성 
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz.\nYour final score was: {quiz.score}/{quiz.ques_no}")

if quiz.score >=4:
    print("합격입니다^0^")
else:
    print("불합격입니다 ㅠㅅㅠ")