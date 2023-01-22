from tkinter import*
import tkinter as tk

#게임방법 
def method():
   methodWindow = tk.Toplevel()
   methodWindow.title("게임방법")
   methodWindow.geometry("500x500")
   methodWindow.resizable(width = False, height = False)
   
   photo400 = PhotoImage(file =r"C:\Users\luna2\Desktop\Dog Game\Dog Game\find.gif")
   methodWindow = Label(methodWindow, image = photo400)
   methodWindow.pack()
   methodWindow.mainloop()

#시작화면
startWindow = Tk()
startWindow.title("유기견 사료벌기 GAME")
startWindow.geometry("500x500")
startWindow.resizable(width = False, height = False)
photo200 = PhotoImage(file =r"C:\Users\luna2\Desktop\Dog Game\Dog Game\intro.gif")
photo201= PhotoImage(file = r"C:\Users\luna2\Desktop\Dog Game\Dog Game\howto.gif")
photo202= PhotoImage(file = r"C:\Users\luna2\Desktop\Dog Game\Dog Game\start.gif")

startWindow.configure(bg='#f7e15c')
btn_start = Button(startWindow, image = photo202, command = startWindow.destroy)
btn_ways = Button(startWindow, image = photo201, command = lambda:method())
startWindow = Label(startWindow, image = photo200, bg='#f7e15c')

startWindow.pack()
btn_start.place(x = 280, y = 430)
btn_ways.place(x = 80, y = 430)
startWindow.mainloop()

#문제 (1~3번 주관식, 4~6번 객관식)
answer = 0
user_answer = None

def q1w():
    global root1
    root1=Tk()
    root1.title("첫번째 문제")
    root1.geometry("500x500")
    root1.resizable(width = False, height = False)

    photo1=PhotoImage(file=r"C:\Users\luna2\Desktop\Dog Game\Dog Game\no1.gif")
    btn_q1=Button(root1,image=photo1, command=ans1) 
    btn_q1.pack()
    
    root1.mainloop()

def ans1(): #답안 입력
    global user_answer
    
    ans1=Toplevel(root1)
    ans1.geometry("300x240")
    ans1.resizable(width = False, height = False)
    ans1.title("정답을 입력해 주세요.")

    ans1.configure(bg='#f7e15c')

    user_answer = StringVar()
    
    user=tk.Entry(ans1, textvariable=user_answer, width = 30, bg='#f7e15c')
    user.insert(0, "(여기에 정답을 입력하세요.)")
    user.grid()
    user.pack()
    
    btn = Button(ans1, text="입력", font=("맑은 고딕", 13), command=m1)
    btn.pack()
        
def m1():
    m1=Toplevel(root1)
    m1.geometry("200x200")
    m1.resizable(width = False, height = False)
    m1.title("결과")

    answer1 = "포도"

    if user_answer.get() == answer1:
        at=Label(m1, text="정답입니다.", font=("맑은 고딕", 15), height=5)
        at.pack()
        global answer
        answer += 1
    else:
        af=Label(m1, text="틀렸습니다.", font=("맑은 고딕", 15), height=5)
        af.pack()

    open_btn=Button(m1,text="다음 문제로",font=("맑은 고딕", 11), command=lambda:q2w(root1))
    open_btn.pack()
    
def q2w(root1):
    root1.destroy()
    
    global root2
    root2=Tk()
    root2.title("두번째 문제")
    root2.geometry("500x500")
    root2.resizable(width = False, height = False)

    photo2=PhotoImage(file=r"C:\Users\luna2\Desktop\Dog Game\Dog Game\no2.gif")
    btn_q2=Button(root2,image=photo2, command=ans2) 
    btn_q2.pack()
    
    root2.mainloop()

def ans2(): #답안 입력
    global user_answer
    
    ans2=Toplevel(root2)
    ans2.geometry("300x240")
    ans2.resizable(width = False, height = False)
    ans2.title("정답을 입력해 주세요.")

    ans2.configure(bg='#f7e15c')

    user_answer = StringVar()
    
    user=tk.Entry(ans2, textvariable=user_answer, width = 30, bg='#f7e15c')
    user.insert(0, "(여기에 정답을 입력하세요.)")
    user.grid()
    user.pack()
    
    btn = Button(ans2, text="입력", font=("맑은 고딕", 13), command=m2)
    btn.pack()
        
def m2():
    m2=Toplevel(root2)
    m2.geometry("200x200")
    m2.resizable(width = False, height = False)
    m2.title("결과")

    answer2 = "초콜릿"

    if user_answer.get() == answer2:
        at=Label(m2, text="정답입니다.", font=("맑은 고딕", 15), height=5)
        at.pack()
        global answer
        answer += 1
    else:
        af=Label(m2, text="틀렸습니다.", font=("맑은 고딕", 15), height=5)
        af.pack()

    open_btn=Button(m2,text="다음 문제로",font=("맑은 고딕", 11), command=lambda:q3w(root2))
    open_btn.pack()

    
def q3w(root2):
    root2.destroy()
    
    global root3
    root3=Tk()
    root3.title("세번째 문제")
    root3.geometry("500x500")
    root3.resizable(width = False, height = False)

    photo3=PhotoImage(file=r"C:\Users\luna2\Desktop\Dog Game\Dog Game\no3.gif")
    btn_q3=Button(root3,image=photo3, command=ans3) 
    btn_q3.pack()
    
    root3.mainloop()

def ans3(): #답안 입력
    global user_answer
    
    ans3=Toplevel(root3)
    ans3.geometry("300x240")
    ans3.title("정답을 입력해 주세요.")
    ans3.resizable(width = False, height = False)

    ans3.configure(bg='#f7e15c')

    user_answer = StringVar()
    
    user=tk.Entry(ans3, textvariable=user_answer, width = 30, bg='#f7e15c')
    user.insert(0, "(여기에 정답을 입력하세요.)")
    user.grid()
    user.pack()
    
    btn = Button(ans3, text="입력", font=("맑은 고딕", 13), command=m3)
    btn.pack()
        
def m3():
    m3=Toplevel(root3)
    m3.geometry("200x200")
    m3.title("결과")
    m3.resizable(width = False, height = False)

    answer3 = "마늘"

    if user_answer.get() == answer3:
        at=Label(m3, text="정답입니다.", font=("맑은 고딕", 15), height=5)
        at.pack()
        global answer
        answer += 1
    else:
        af=Label(m3, text="틀렸습니다.", font=("맑은 고딕", 15), height=5)
        af.pack()

    open_btn=Button(m3,text="다음 문제로",font=("맑은 고딕", 11), command=lambda:q4w(root3))
    open_btn.pack()

def q4w(root3):
    root3.destroy()
    
    global root4
    root4=Tk()
    root4.title("네번째 문제")
    root4.geometry("500x500")
    root4.resizable(width = False, height = False)

    photo4=PhotoImage(file=r"C:\Users\luna2\Desktop\Dog Game\Dog Game\no4.gif")
    btn_q4=Button(root4,image=photo4, command=s4)
    btn_q4.pack()

    root4.mainloop()
    
def s4():
    s4=Toplevel(root4)
    s4.geometry("300x240")
    s4.resizable(width = False, height = False)
    s4.title("정답을 골라 주세요.")

    s4.configure(bg='#f7e15c')
    
    global r
    r=IntVar()

    r1=Radiobutton(s4, text="1. 양파", font=("맑은 고딕", 20),bg='#f7e15c',variable=r, value="1")
    r1.pack()

    r2=Radiobutton(s4, text="2. 버섯", font=("맑은 고딕", 20),bg='#f7e15c',variable=r, value="2")
    r2.pack()

    r3=Radiobutton(s4, text="3. 아보카도", font=("맑은 고딕", 20),bg='#f7e15c',variable=r, value="3")
    r3.pack()

    show=Label(s4, bg='#f7e15c')
    show.pack()

    btn=Button(s4,text="확인", font=("맑은 고딕", 13), command=m4)
    btn.pack()

def m4(): #결과
    m4=Toplevel(root4)
    m4.geometry("200x200")
    m4.resizable(width = False, height = False)
    m4.title("결과")
    
    if r.get()==3:
        at=Label(m4, text="정답입니다.", font=("맑은 고딕", 15), height=5)
        at.pack()
        global answer
        answer+=1
    else:
        af=Label(m4, text="틀렸습니다.", font=("맑은 고딕", 15), height=5)
        af.pack()
        
    open_btn=Button(m4,text="다음 문제로",font=("맑은 고딕", 11), command=lambda:q5w(root4))
    open_btn.pack()
    

###5번 문제###
def q5w(root4):
    root4.destroy()
    
    global root5
    root5=Tk()
    root5.title("다섯번째 문제")
    root5.geometry("500x500")
    root5.resizable(width = False, height = False)

    photo5=PhotoImage(file=r"C:\Users\luna2\Desktop\Dog Game\Dog Game\no5.gif")
    btn_q5=Button(root5,image=photo5, command=s5)
    btn_q5.pack()

    root5.mainloop()
    
def s5():#선택
    s5=Toplevel(root5)
    s5.geometry("300x240")
    s5.resizable(width = False, height = False)
    s5.title("정답을 골라 주세요.")

    s5.configure(bg='#f7e15c')
    
    global r
    r=IntVar()

    r1=Radiobutton(s5, text="1. 양파", font=("맑은 고딕", 20),bg='#f7e15c',variable=r, value="1",)
    r1.pack()

    r2=Radiobutton(s5, text="2. 버섯", font=("맑은 고딕", 20),bg='#f7e15c',variable=r, value="2")
    r2.pack()

    r3=Radiobutton(s5, text="3. 아보카도", font=("맑은 고딕", 20),bg='#f7e15c',variable=r, value="3")
    r3.pack()

    show=Label(s5, bg='#f7e15c')
    show.pack()


    btn=Button(s5,text="확인", font=("맑은 고딕", 13), command=m5)
    btn.pack()

def m5(): #결과
    m5=Toplevel(root5)
    m5.geometry("200x200")
    m5.resizable(width = False, height = False)
    m5.title("결과")
    
    if r.get()==1:
        at=Label(m5, text="정답입니다.", font=("맑은 고딕", 15), height=5)
        at.pack()
        global answer
        answer+=1
    else:
        af=Label(m5, text="틀렸습니다.", font=("맑은 고딕", 15), height=5)
        af.pack()
        
    open_btn=Button(m5,text="다음 문제로",font=("맑은 고딕", 11), command=lambda:q6w(root5))
    open_btn.pack()


###6번 문제###
def q6w(root5):
    root5.destroy()
    
    global root6
    root6=Tk()
    root6.title("여섯번째 문제")
    root6.geometry("500x500")
    root6.resizable(width = False, height = False)

    photo6=PhotoImage(file=r"C:\Users\luna2\Desktop\Dog Game\Dog Game\no6.gif")
    btn_q6=Button(root6,image=photo6, command=s6)
    btn_q6.pack()

    root6.mainloop()
    
def s6():#선택
    s6=Toplevel(root6)
    s6.geometry("300x240")
    s6.resizable(width = False, height = False)
    s6.title("정답을 골라 주세요.")

    s6.configure(bg='#f7e15c')
    
    global r
    r=IntVar()

    r1=Radiobutton(s6, text="1. 양파", font=("맑은 고딕", 20),bg='#f7e15c',variable=r, value="1",)
    r1.pack()

    r2=Radiobutton(s6, text="2. 버섯", font=("맑은 고딕", 20),bg='#f7e15c',variable=r, value="2")
    r2.pack()

    r3=Radiobutton(s6, text="3. 아보카도", font=("맑은 고딕", 20),bg='#f7e15c',variable=r, value="3")
    r3.pack()

    show=Label(s6, bg='#f7e15c')
    show.pack()

    btn=Button(s6,text="확인", font=("맑은 고딕", 13), command=m6)
    btn.pack()

def m6(): #결과
    m6=Toplevel(root6)
    m6.geometry("200x200")
    m6.resizable(width = False, height = False)
    m6.title("결과")
    
    if r.get()==2:
        at=Label(m6, text="정답입니다.", font=("맑은 고딕", 15), height=5)
        at.pack()
        global answer
        answer+=1
    else:
        af=Label(m6, text="틀렸습니다.", font=("맑은 고딕", 15), height=5)
        af.pack()
        
    open_btn=Button(m6,text="최종 결과",font=("맑은 고딕", 11), command=lambda:final(root6)) 
    open_btn.pack()


def final(root6):
    root6.destroy()

    global window
    window=Tk()
    window.geometry("500x500")
    window.resizable(width = False, height = False)
    window.title("게임 결과")

    if answer<=2:

        label5=Label(window,text="아직 배가 고파요", font=("맑은 고딕",20),bg='#f7e15c')

        photo2=PhotoImage(file=r"C:\Users\luna2\Desktop\Dog Game\Dog Game\hungry.gif")
        label55=Label(window,image=photo2, bg='#f7e15c')

        label6=Label(window,text="맞춘 문제 개수: ", font=("맑은 고딕",20),bg='#f7e15c')

        label65=Label(window,text=answer, font=("맑은 고딕",20),bg='#f7e15c')
        
        label5.place(x=125,y=40)
        label6.place(x=120, y=0)
        label65.place(x=320, y=0)
        label55.place(x=125, y=125)

        window.configure(bg='#f7e15c')
        photo100=PhotoImage(file=r"C:\Users\luna2\Desktop\Dog Game\Dog Game\end.gif")
        label100=Label(window, image=photo100, bg='#f7e15c')
        button1=Button(window,text="종료", font=("맑은 고딕", 11), command=lambda:createNewWindow(window))
        button1.place(x=450, y=450)
        
        window.mainloop()

    elif 3<=answer<=4:

        label7=Label(window,text="적당히 먹었어요",font=("맑은 고딕",20), bg='#f7e15c')

        photo3=PhotoImage(file=r"C:\Users\luna2\Desktop\Dog Game\Dog Game\tryhard.gif")
        label75=Label(window,image=photo3, bg='#f7e15c')

        label8=Label(window,text="맞춘 문제 개수: ",font=("맑은 고딕",20),bg='#f7e15c')

        label85=Label(window,text=answer,font=("맑은 고딕",20),bg='#f7e15c')

        label75.pack()
        label75.place(x=115, y=110)
        label7.place(x=125,y=40)
        label8.place(x=120,y=0)
        label85.place(x=320,y=0)
       
        window.configure(bg='#f7e15c')
        photo100=PhotoImage(file=r"C:\Users\luna2\Desktop\Dog Game\Dog Game\end.gif")
        label100=Label(window, image=photo100, bg='#f7e15c')
        button1=Button(window,text="종료", font=("맑은 고딕", 11), command=lambda:createNewWindow(window))
        button1.place(x=450, y=450)
        
        window.mainloop()


    else:
        label10=Label(window,text="맞춘 문제 개수: ",
             font=("맑은 고딕",20),bg='#f7e15c')

        label9=Label(window,text="배가 불러요 참 잘했어요!", font=("맑은 고딕",20),bg='#f7e15c')

        photo4=PhotoImage(file=r"C:\Users\luna2\Desktop\Dog Game\Dog Game\great.gif")
        label95=Label(window,image=photo4,bg='#f7e15c')

        label105=Label(window,text=answer,font=("맑은 고딕",20),bg='#f7e15c')

        label95.pack()
        label95.place(x=55, y=145)
        label9.place(x=80,y=40)
        label10.place(x=120,y=0)
        label105.place(x=320,y=0)
       
        window.configure(bg='#f7e15c')
        photo100=PhotoImage(file=r"C:\Users\luna2\Desktop\Dog Game\Dog Game\end.gif")
        label100=Label(window, image=photo100, bg='#f7e15c')
        button1=Button(window,text="종료", font=("맑은 고딕", 11), command=lambda:createNewWindow(window))
        button1.place(x=450, y=450)
        
        window.mainloop()

def createNewWindow(window):
    window.destroy()

    global newWindow
    newWindow = Tk()
    newWindow.geometry("500x500")
    newWindow.resizable(width = False, height = False)
    newWindow.title("종료하기 전에")

    newWindow.configure(bg='#f7e15c')
    label1=Label(newWindow,text="여기서 잠깐!",
                 font=("맑은 고딕",20),bg='#f7e15c').pack()

    label2=Label(newWindow,text="강아지가 먹으면 안되는 음식에는",
                 font=("맑은 고딕",15),bg='#f7e15c').pack()

    photo1=PhotoImage(file=r"C:\Users\luna2\Desktop\Dog Game\Dog Game\no1ans.gif")
    label25=Label(newWindow,image=photo1,bg='#f7e15c')

    photo3=PhotoImage(file=r"C:\Users\luna2\Desktop\Dog Game\Dog Game\no2ans.gif")
    label26=Label(newWindow,image=photo3,bg='#f7e15c')

    photo4=PhotoImage(file=r"C:\Users\luna2\Desktop\Dog Game\Dog Game\no3ans.gif")
    label27=Label(newWindow,image=photo4,bg='#f7e15c')

    photo5=PhotoImage(file=r"C:\Users\luna2\Desktop\Dog Game\Dog Game\no4ans.gif")
    label28=Label(newWindow,image=photo5,bg='#f7e15c')

    photo6=PhotoImage(file=r"C:\Users\luna2\Desktop\Dog Game\Dog Game\no5ans.gif")
    label29=Label(newWindow,image=photo6,bg='#f7e15c')

    photo7=PhotoImage(file=r"C:\Users\luna2\Desktop\Dog Game\Dog Game\no6ans.gif")
    label30=Label(newWindow,image=photo7,bg='#f7e15c')


    label3=Label(newWindow,text="포도 초콜릿 마늘 아보카도 양파 버섯",
                 font=('Modern',20),fg='red',bg='#f7e15c')

    label4=Label(newWindow,text="이 있습니다!",
                 font=("맑은 고딕",15),bg='#f7e15c')


    photo200 = PhotoImage(file =r"C:\Users\luna2\Desktop\Dog Game\Dog Game\end.gif")
    button2=tk.Button(newWindow,image = photo200, command=quit)


    button2.pack(side=BOTTOM,anchor=E)

    label25.pack()
    label26.pack()
    label27.pack()
    label28.pack()
    label29.pack()
    label30.pack()

    
    label25.place(x=50,y=70)
    label26.place(x=245,y=70)
    label27.place(x=50,y=180)
    label28.place(x=245,y=180)
    label29.place(x=50,y=290)
    label30.place(x=245,y=290)

    label3.pack()
    label3.place(x=25,y=408)
                
    label4.pack()
    label4.place(x=200,y=451)

    newWindow.mainloop()

q1w()
