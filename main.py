from question_model import Question
from data import *
from quiz_brain import QuizBrain
import winsound
import sqlite3
# tkinter를 사용하기 위한 import
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as ms

with sqlite3.connect("login.db") as db:
    c=db.cursor()
#테이블 생성(Datatype : INTEGER, TEXT)
#학번,  비번 를 저장하는 쿼리 작성
c.execute("CREATE TABLE IF NOT EXISTS user(id INTEGER NOT NULL, \
    password TEXT NOT NULL)")
c.execute("SELECT * FROM user")
db.commit()
db.close()

class main():
    def __init__(self,master):
        self.master=master
        self.id=StringVar()
        self.password=StringVar()
        self.n_id=StringVar()
        self.n_password=StringVar()
        self.widgets()
    
    def login(self):
        # conn=sqlite3.connect("C:/Users/user/Oss/oss/quizgame/quizgame-master/quizgame-master/resource/database.db", isolation_level=None)
        # c=conn.cursor()
        with sqlite3.connect("login.db") as db:
            c=db.cursor()
        find_user=("SELECT * FROM user WHERE id =? AND password = ?")
        c.execute(find_user,[(self.id.get()),(self.password.get())])
        results=c.fetchall()
        if results:
            self.logf.pack_forget()
            self.head["text"]=self.id.get() + "\n 로그인 완료\n창을 닫고 \n시험을 응시해 주세요"
            self.head["pady"]=150
        else:
            ms.showerror("경고!","id가 맞지 않습니다")
    def new_user(self):
        # conn=sqlite3.connect("C:/Users/user/Oss/oss/quizgame/quizgame-master/quizgame-master/resource/database.db", isolation_level=None)
        # c=conn.cursor()
        with sqlite3.connect("login.db") as db:
            c=db.cursor()
        find_user=("SELECT * FROM user WHERE id =?")
        c.execute(find_user,[(self.id.get())])
        if c.fetchall():
            ms.showerror("oops!","id가 존재한다")
        else:
            ms.showinfo("성공!","Account Created")
            self.log()
        insert='INSERT INTO user(id,password) VALUES(?,?)'
        c.execute(insert,[(self.n_id.get()),(self.n_password.get())])
        db.commit()

    def log(self):
        self.id.set("")
        self.password.set("")
        self.crf.pack_forget()
        self.head['text']="  로그인  "
        self.logf.pack()

    def cr(self):
        self.n_id.set("")
        self.n_password.set("")
        self.head['text']="계정생성"
        self.logf.pack_forget()
        self.crf.pack()

    def widgets(self):
        self.head=Label(self.master,text="  LOGIN  ",font=('freesansbold',35),pady=40)
        self.head.pack()

        self.logf=Frame(self.master,padx=10,pady=10)
        Label(self.logf,text="ID       : ",font=('freesansbold',20),padx=5,pady=5).grid(sticky=W)
        Entry(self.logf,textvariable=self.id,bd=8,font=('calibri',15,'bold')).grid(row=0,column=1,sticky=E)
        Label(self.logf,text="Password : ",font=('freesansbold',20),padx=5,pady=5).grid(row=1,column=0,sticky=W)
        Entry(self.logf,textvariable=self.password,bd=8,font=('calibri',15,'bold')).grid(row=1,column=1,sticky=E)
        Button(self.logf,text='  LOGIN  ',bd=7,font=("monaco",15,'bold'),padx=5,pady=5,command=self.login).grid(row=2)
        Button(self.logf,text='회원가입',bd=7,font=("monaco",15,'bold'),padx=5,pady=5,command=self.cr).grid(row=2,column=1)
        self.logf.pack()

        self.crf=Frame(self.master,padx=10,pady=10)
        Label(self.crf,text="ID       : ",font=('freesansbold',20),padx=5,pady=5).grid(sticky=W)
        Entry(self.crf,textvariable=self.n_id,bd=8,font=('calibri',15,'bold')).grid(row=0,column=1,sticky=E)
        Label(self.crf,text="Password : ",font=('freesansbold',20),padx=5,pady=5).grid(row=1,column=0,sticky=W)
        Entry(self.crf,textvariable=self.n_password,bd=8,font=('calibri',15,'bold')).grid(row=1,column=1,sticky=E)
        Button(self.crf,text='로그인하기 ',bd=7,font=("monaco",15,'bold'),padx=5,pady=5,command=self.log).grid(row=2)
        Button(self.crf,text='계정 생성',bd=7,font=("monaco",15,'bold'),padx=5,pady=5,command=self.new_user).grid(row=2,column=1)
        self.logf.pack()

root=Tk()
main(root)
root.geometry("400x350+350+150")
root.mainloop()


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

#테이블 만들기
with sqlite3.connect("login.db") as db:
    c=db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS user2(id INTEGER NOT NULL, \
     scoree INTEGER)")
c.execute("SELECT * FROM user2")
db.commit()

find_user=("SELECT * FROM user2 WHERE id =? AND scoree=?")
c.execute(find_user,[id,int(score)])
insert='INSERT INTO user2(id,scoree) VALUES(?,?)'
c.execute(insert,[id,int(score)])
db.commit()

    