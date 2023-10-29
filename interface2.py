from tkinter import *
import help_learn_system as hls
from tkinter import ttk


enabled = ""

def check_status_button():
    
    # buttons_list = []
    # for button in buttons:
    #     buttons_list.append(button[0])
    
    active_buttons = []

    for item in buttons:
        
        if item[1].get(): 
            active_buttons.append(item[0])
        else: print(item[1].get())
    print(active_buttons)
    return active_buttons

    

def create_buttons(name_pictures):
    date_base = hls.add_to_base_questions(list_name_pictures)
    count = 0
    count_column = 0
    count_row = 1
    btn_list = []
    list_int_var = []
    btn_tuple_list = []
    for i in range(6):
        new_int_var = IntVar(value=0)
        list_int_var.append(new_int_var)
    for name in name_pictures:
        btn_tuple_list.append(((Checkbutton(text=name, variable=list_int_var[count])), list_int_var[count]))
        count+=1
    for j in btn_tuple_list:
        j[0].grid(row=1, column=count_column)
        count_column+=1
        if count_column==6:
            count_row+=1
    for item in btn_tuple_list:
        btn_list.append(item[0])
    
    return btn_tuple_list
    








# def create_buttons(list):
#     global enabled
#     res_dict = hls.add_to_base_questions(list)
#     count_column=0
#     count_row=1
#     ch_btn_list = []
#     list_from_checkbutton = []
#     enabled = StringVar()
#     for key in res_dict:
        
#         newCnBtn = Checkbutton(text=key, bg="#9ACD32", variable=enabled, onvalue=key, offvalue="", padx=2, pady=2)
#         ch_btn_list.append(newCnBtn)
      
#         newCnBtn.grid(row=1, column=count_column)
#         ch_btn_list.append(newCnBtn)
#         count_column+=1
#         if(count_column==5): count_row+=1
#     return ch_btn_list


def add_image_to_button(dict_button_image):
    list_button = create_buttons(list_name_pictures)
    pic = []
    for button in list_button:
        text_button = button[0].cget("text")
        for key in dict_button_image:
            if text_button == key:
                button_picture = PhotoImage(file=f"pictures/{dict_button_image[text_button]}")
                pic.append(button_picture)
                button[0].configure(image=button_picture, compound=TOP)
    return pic


def create_command_for_button(buttons):
    
    for button in buttons:
        text_button = button[0].cget("text")
        button[0].configure(command=make_list_qestions(text_button))




def make_list_qestions(text):
    
    base = hls.add_to_base_questions(list_name_pictures)
    print(text)       
    return base[text]

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
button_images = {"Базы_данных.txt":"db.png",
                 "Компьютерные_сети.txt":"KS.png",
                 "HTML_CSS.txt":"html.png",
                 "JAVA+.txt":"java.png",
                 "Linux.txt":"linux.png",
                 "Python.txt":"python3.png"}


choose_question_frame = Frame()
lab_choose_question = Label(choose_question_frame,text="Выберите вопрос из списка", padx=2, pady=2)
lab_choose_question.pack(fill=X, ipadx=15, ipady=3)














#list_box = Variable(value=)

#list_box_questions = Listbox(choose_question_frame, listvariable=list_box)
#list_box_questions.pack(fill=X, padx=5, pady=5)



baskets_ch_btns = []






buttons = create_buttons(list_name_pictures)
pictures = add_image_to_button(button_images)
create_command_for_button(buttons)



view_answer_btn = Button(choose_question_frame,text="Сформировать вопросы по выбранному блоку", padx=5, pady=5,command=check_status_button)
view_answer_btn.pack(side="left", fill=X)
go_test_btn = Button(choose_question_frame, text="Показать ответ на вопрос", padx=5, pady=5)
go_test_btn.pack(side="left")
choose_question_frame.grid(row=2, column=0, columnspan=3)



root.mainloop()