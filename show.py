from tkinter import *

win=Tk()

win.geometry('400x600')
win.title("EDUCATOR")
win.config(bg='#b6d7a8')
win.resizable(False,False)

def click():
    def show_less():
        
        etc_btn.config(text='and more ......',fg='green')
        subject6_btn.place_forget()
        subject7_btn.place_forget()
        show_less_btn.place_forget()
        
        
    etc_btn.config(text='Physics',fg='black')
    
    subject6_btn=Button(win,text='Chemistry',cursor='hand2',activebackground='#b6d7a8',font=("Calibri",10),bd=0,bg='#b6d7a8',fg='black')
    subject6_btn.place(x=5,y=200)
    
    subject7_btn=Button(win,text='Biology',cursor='hand2',activebackground='#b6d7a8',font=("Calibri",10),bd=0,bg='#b6d7a8',fg='black')
    subject7_btn.place(x=5,y=220)
    
    show_less_btn=Button(win, text='Show Less',cursor='hand2',command=show_less,activebackground='#b6d7a8',font=("Calibri",10),bd=0,bg='#b6d7a8',fg='green')
    show_less_btn.place(x=5,y=240)


title1_label=Label(win,text="SUBJECTS ",bg='#b6d7a8', font=("Calibri",15,'bold'),fg='black')
title1_label.place(x=5,y=10)

title2_label=Label(win,text='to LEARN',bg='#b6d7a8',font=("Calibri",15,'bold'),fg='black')
title2_label.place(x=5,y=40)

subject1_btn=Button(win,text='Philosophy',activebackground='#b6d7a8',font=("Calibri",10),cursor='hand2',bd=0,bg='#b6d7a8',fg='black')
subject1_btn.place(x=5,y=80)

subject2_btn=Button(win,text='Psychology',activebackground='#b6d7a8',cursor='hand2',font=("Calibri",10),bd=0,bg='#b6d7a8',fg='black')
subject2_btn.place(x=5,y=100)

subject3_btn=Button(win,text='Personal Development',cursor='hand2',activebackground='#b6d7a8',font=("Calibri",10),bd=0,bg='#b6d7a8',fg='black')
subject3_btn.place(x=5,y=120)

subject4_btn=Button(win,text='Economics',cursor='hand2',activebackground='#b6d7a8',font=("Calibri",10),bd=0,bg='#b6d7a8',fg='black')
subject4_btn.place(x=5,y=140)

subject5_btn=Button(win,text='History',cursor='hand2',activebackground='#b6d7a8',font=("Calibri",10),bd=0,bg='#b6d7a8',fg='black')
subject5_btn.place(x=5,y=160)

etc_btn=Button(win,text='and more ......',cursor='hand2',command=click,activebackground='#b6d7a8',font=("Calibri",10),bd=0,bg='#b6d7a8',fg='green')
etc_btn.place(x=5,y=180)


win.mainloop()
