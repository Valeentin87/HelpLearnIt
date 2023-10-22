from tkinter import *
import help_learn_system as hls
from tkinter import ttk

root = Tk()
root.title("Окно тестирования приложения")
root.geometry("1300x700")
root.resizable(False,False)
for c in range(6): root.columnconfigure(index=c, weight=1)
for r in range(4): root.rowconfigure(index=r,weight=1)
root.rowconfigure(index=3, weight=4)

header = Frame(bg="#FFD700")
lab_head = Label(header, text="Выберите нужный блок для изучения", justify=CENTER, padx=2, pady=2)
lab_head.pack(fill=X, ipadx=5, ipady=3)
lab_head_choose = Label(header, text="Вы выбрали", justify=LEFT, bg="#FFFFE0")
lab_head_choose.pack(fill=X, ipadx=15, ipady=3)
header.grid(row=0, column=0, columnspan=6)


list_name_pictures = ["JAVA+.txt", "Python.txt", "HTML_CSS.txt","Базы_данных.txt","Компьютерные_сети.txt","Linux.txt"]

baskets_ch_btns = []

def return_data_for_scrollbar(find_key):
        data_base = hls.add_to_base_questions(list_name_pictures)
        list_questions = data_base.get(find_key)
        result = []
        for i in list_questions:
            result.append(i.question)
        print(result)
        return result



def create_buttons(list):
    res_dict = hls.add_to_base_questions(list)
    count_column=0
    count_row=1
    ch_btn_list = []
    list_from_checkbutton = []
    for key in res_dict:
        enabled = StringVar(value="")
        newCnBtn = Checkbutton(text=key, bg="#9ACD32", variable=enabled, onvalue=key, offvalue="dont_press", padx=2, pady=2)
        newCnBtn.configure(command=return_data_for_scrollbar(newCnBtn.cget("text")))
        ch_btn_list.append(newCnBtn)
      
        newCnBtn.grid(row=1, column=count_column)
        ch_btn_list.append((newCnBtn,list_from_checkbutton))
        count_column+=1
        if(count_column==5): count_row+=1
    #return ch_btn_list
    

# enabled = IntVar(value=0)
# for btn in baskets_ch_btns:
#     btn.config(variable=enabled)
        
# pict1 = PhotoImage(file="./pictures/java.png")
# pict2= PhotoImage(file="./pictures/python3.png")       
# pict3 = PhotoImage(file="./pictures/html.png")
# pict4 = PhotoImage(file="./pictures/db.png")
# pict5 = PhotoImage(file="./pictures/KS.png")
# pict6 = PhotoImage(file="./pictures/linux.png")

# bcheckbuttons = create_buttons(hls.list_name_files)

# first_button = bcheckbuttons[0]
# second_button = bcheckbuttons[1]
# third_button = bcheckbuttons[2]
# fourth_button = bcheckbuttons[3]
# five_button = bcheckbuttons[4]
# six_button = bcheckbuttons[5]

# first_button.config(image=pict1)
# second_button.config(image=pict2)
# third_button.config(image=pict3)
# fourth_button.config(image=pict4)
# five_button.config(image=pict5)
# six_button.config(image=pict6)

create_buttons(list_name_pictures)

dict_but = hls.add_to_base_questions(list_name_pictures)
for key in dict_but:
    print(key)

choose_question_frame = Frame()
lab_choose_question = Label(choose_question_frame,text="Выберите вопрос из списка", padx=2, pady=2)
lab_choose_question.pack(fill=X, ipadx=15, ipady=3)
lab_scrollbar = Label(choose_question_frame, text="Здесь будет список вопросов", width="30", height="25", bg="#F0E68C")
lab_scrollbar.pack(fill=X, ipadx=4, ipady=4)
view_answer_btn = Button(choose_question_frame,text="Показать ответ", padx=5, pady=5)
view_answer_btn.pack(side="left")
go_test_btn = Button(choose_question_frame, text="Пройти тест", padx=5, pady=5)
go_test_btn.pack(side="left")
choose_question_frame.grid(row=3, column=0, columnspan=3)


root.mainloop()