from question_model import Question
from data import *
from quiz_brain import QuizBrain
import winsound
# tkinter를 사용하기 위한 import
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msgbox

# tkinter 객체 생성
window = Tk()
window.title("로그인 화면")

# 사용자 학번과 비밀번호를 저장하는 변수 생성
user_id, password = StringVar(), StringVar()

# 로그인 메세지 박스 
def info():
    with open("./chosun_student.txt","r",encoding="utf8") as student_file:
        student_dict = {}
        for x in student_file: 
            dic = x.strip().split(":")
            student_dict[dic[0]] = dic[1]
        a=user_id.get()
        b=password.get()
        if a in student_dict.keys() and b in student_dict.values(): #정상 로그인
            msgbox.showinfo("로그인","정상적으로 로그인되었습니다.")
        else: #로그인 실패
            msgbox.showinfo("로그인 실패","다시 입력하세요.")

# 학번과 비번, 로그인 버튼의 GUI를 만드는 부분
ttk.Label(window, text = "학번 : ").grid(row = 0, column = 0, padx = 10, pady = 10)
ttk.Label(window, text = "비밀번호 : ").grid(row = 1, column = 0, padx = 10, pady = 10)
ttk.Entry(window, textvariable = user_id).grid(row = 0, column = 1, padx = 10, pady = 10)
ttk.Entry(window, textvariable = password).grid(row = 1, column = 1, padx = 10, pady = 10)
ttk.Button(window, command=info, text = "로그인").grid(row = 2, column = 1, padx = 10, pady = 10)
window.mainloop()

question_bank = []  #질문리스트
#question.py 파일에서 각 파트에 해당되는 질문을 읽어들여 질문 리스트에 추가
def make_instance1():
    for question in question_data1: 
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

print("(2020년 3회) 정보처리기사 필기 기출문제")
print("1과목 - 소프트웨어 설계")
print("2과목 - 소프트웨어 개발")
print("3과목 - 데이터베이스 구축")
print("4과목 - 프로그래밍 언어 활용")
print("5과목 - 정보시스템 구축 관리")

while(1):
    num=int(input("응시할 과목을 고르시오(1~5, 0입력시 종료):"))
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
    elif num==0:
        print("프로그램을 종료합니다.")
        break
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
    question_bank = []

    