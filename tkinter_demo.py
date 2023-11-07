from tkinter import *
import help_learn_system as hls
import tkinter.messagebox as box

root = Tk()
root.title("Демонтстрация")
root.geometry("1500x800")

list_name_pictures = ["JAVA+.txt", "Python.txt", "HTML_CSS.txt","Базы_данных.txt","Компьютерные_сети.txt","Linux.txt"]
button_images = {"Базы_данных.txt":"db.png",
                 "Компьютерные_сети.txt":"KS.png",
                 "HTML_CSS.txt":"html.png",
                 "JAVA+.txt":"java.png",
                 "Linux.txt":"linux.png",
                 "Python.txt":"python3.png"}

dict_base = hls.add_to_base_questions(list_name_pictures)

for key, value in dict_base.items():
    l = value
    print(len(l))

def check_status_button():
    list_status_button = []
    for key, value in dict_int_var.items():
        list_status_button.append((key, value.get()))
    #     if value.get():
    #         list_status_button.append(key)
    # print(list_status_button)
    # return list_status_button
    print(list_status_button)


list_questions_from_buttons = []

def create_all_questions():
    global list_questions_from_buttons
    global list_quest_var
    global list_quest_listbox
    list_questions_from_buttons = []
    dict_questions = hls.add_to_base_questions(list_name_pictures)
    
    for key, value in dict_int_var.items():
        if value.get():
            list_questions_from_buttons.extend(dict_questions[key])
    list_quest_var = Variable(value=list_questions_from_buttons)
    list_quest_listbox.configure(listvariable=list_quest_var)
    
    list_quest_listbox.pack()
    print(list_questions_from_buttons)
    return list_questions_from_buttons

def view_question():
    global text_answer
    global list_questions_from_buttons
    index_active_element = list_quest_listbox.curselection()
    typle_to_list = index_active_element[0]
    answer_from_button = list_questions_from_buttons[typle_to_list]
    text_answer.insert("1.0",answer_from_button.answer)
    print(index_active_element)

def click_add():
    box.showinfo("Добавление вопроса", "Вам предстоит добавить вопрос")

def window_exit():
    #window.destroy()
    pass
listbox_blocks = Listbox()
var_name_block = StringVar(value="Выбран блок: ")
var_numbers_question = StringVar(value="Здесь будет отображаться количество вопросов в выбранном блоке")
lab_check_block = Label()
var_blocks = StringVar()
entry_name_block = Entry()
lab_list_name_pictures = Label()

def click_listbox_blocks(event):
    select = listbox_blocks.curselection()
    print(select)
    s = select[0]
    name_block = listbox_blocks.get(s)
    var_name_block.set("Выбран блок: " + name_block)
    nums = len(dict_base[name_block])
    var_numbers_question.set(f"В выбранном блоке всего \n {nums} вопросов ")


def add_new_block():
    global list_name_pictures
    global lab_list_name_pictures
    global var_blocks
    #new_list_names = list_name_pictures.copy()
    list_name_pictures.append(entry_name_block.get())
    #list_name_pictures = new_list_names
    box.showinfo("Результат", f"блок {entry_name_block.get()} успешно добавлен")
    listbox_blocks.insert(END, entry_name_block.get())
    print(list_name_pictures)
    var_blocks.set(list_name_pictures)
    
    

def add_new_quest_wind():
    window = Toplevel(root)
    window.title("Добавление новых вопросов")
    window.geometry("1000x800")
    global listbox_blocks
    global entry_name_block
    for r in range(8): window.rowconfigure(index=r, weight=1)
    for c in range(3): window.columnconfigure(index=c, weight=1)
    frame_list_blocks = LabelFrame(window, text="Имеющиеся блоки")
    var_blocks = StringVar(value=list_name_pictures)
    listbox_blocks = Listbox(frame_list_blocks, listvariable=var_blocks)
    scroll_blocks = Scrollbar(frame_list_blocks, orient="vertical", command=listbox_blocks.yview)
    listbox_blocks["yscrollcommand"] = scroll_blocks.set
    scroll_blocks.pack(side=RIGHT, fill=Y)
    listbox_blocks.bind("<<ListboxSelect>>", click_listbox_blocks)
    listbox_blocks.pack(fill=BOTH, expand=1)
    frame_list_blocks.grid(row=0, column=0, sticky=NSEW)

    frame_checkblock_info = Frame(window)
    global var_name_block
    global var_numbers_question
    lab_check_block = Label(frame_checkblock_info, textvariable=var_name_block)
    lab_check_block.pack(fill=X)
    lab_number_questions = Label(frame_checkblock_info, textvariable=var_numbers_question, padx=5, pady=5)
    lab_number_questions.pack()
    frame_checkblock_info.grid(row=0, column=1, sticky=NSEW)

    frame_name_part_of_block = Frame(window, bd=2, relief="raised")
    lab_name_part_of_block = Label(frame_name_part_of_block, text="Введите название подраздела")
    entry_name_part = Entry(frame_name_part_of_block, width=40)
    lab_name_part_of_block.pack()
    entry_name_part.pack()
    frame_name_part_of_block.grid(row=2, column=0, sticky=NSEW)

    frame_new_question = Frame(window, bd=2, relief="raised")
    lab_new_question = Label(frame_new_question, text="Введите название  вопроса")
    entry_new_question = Entry(frame_new_question, width=80)
    lab_new_question.pack()
    entry_new_question.pack()
    frame_new_question.grid(row=2, column=1, columnspan=2, sticky=NSEW)

    frame_add_new_block = LabelFrame(window, text="Добавление нового блока вопросов")
    frame_add_new_block.grid(row=0, column=2, sticky=NSEW)
    lab_entry_name_block = Label(frame_add_new_block, text="Введите название блока", padx=5, pady=5)
    entry_name_block = Entry(frame_add_new_block)
    butt_new_block = Button(frame_add_new_block, text="Добавить блок", padx=5, pady=5, command=add_new_block)
    lab_entry_name_block.pack()
    entry_name_block.pack()
    butt_new_block.pack()

    
    lab_add_new_question = Label(window, text="Добавление нового вопроса в блок", font=("Arial", 16, "bold"), \
                                  fg="red", bd=3, relief="raise")
    lab_add_new_question.grid(row=1, column=0, columnspan=3)

    lab_enter_new_question = LabelFrame(window, text="Наберите в текстовое поле ответ на добавляемый вопрос")
    text_new_question = Text(lab_enter_new_question)
    text_new_question.pack()
    lab_enter_new_question.grid(row=3, rowspan=3, column=0, columnspan=3)

    button_save_file = Button(window, text="Сохранить в файл")
    button_add_to_base = Button(window, text="Добавить в БД")
    button_save_file.grid(row=6, column=0,sticky=NSEW)
    button_add_to_base.grid(row=6, column=1, sticky=NSEW)
    button_exit = Button(window, text="Закрыть", command=window.destroy)
    button_exit.grid(row=6, column=2, sticky=NSEW)
    window.mainloop()
    

dict_int_var = {}

for name  in list_name_pictures:
    dict_int_var[name] = IntVar(value=0)



def create_buttons(name_pictures):
    btn_list = []
    for name in name_pictures:
        chbtn = Checkbutton(lab_frame_basket_buttons, text=name, variable=dict_int_var[name], width=115, padx=2,\
                            pady=5, font=("Arial",14))
        #chbtn.configure(image=button_picture, compound=TOP)
        btn_list.append(chbtn)
        chbtn.pack(side=LEFT)
    return btn_list

lab_frame_basket_buttons = LabelFrame(root, text="Выберите нужный блок для изучения", height=0.5)
lab_frame_basket_buttons.pack(fill=X)
lab_check_buttons = Label(lab_frame_basket_buttons,text="Здесь будут кнопки-флажки для выбора блока изучения", height="10")
lab_check_buttons.pack()

lab_second_block = Frame(root)
lab_second_block.pack()

lab_frame_list_questions = LabelFrame(lab_second_block, text="Список вопросов:", height=1, width=200)
lab_frame_list_questions.pack(side=LEFT,padx=50)


list_quest_var = Variable(value=list_questions_from_buttons)
list_quest_listbox = Listbox(lab_frame_list_questions, height=20, width=100, listvariable=list_quest_var)
list_quest_listbox.pack(side=LEFT, fill=BOTH, expand=1)
scrollbar = Scrollbar(lab_frame_list_questions, orient="vertical", command=list_quest_listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
list_quest_listbox["yscrollcommand"]=scrollbar.set
create_list_questions = Button(text="Создать список вопросов", command=create_all_questions)
create_list_questions.place(x=240, y=677)


lab_frame_answer = LabelFrame(lab_second_block, text="Ответ на вопрос:")
lab_frame_answer.pack(side=LEFT, padx=50)
text_answer = Text(lab_frame_answer, font=("Arial", 14), height=15, wrap="none")

ans_scroll_x = Scrollbar(lab_frame_answer, orient=HORIZONTAL, command=text_answer.xview)
ans_scroll_x.pack(side=BOTTOM, fill=X)
text_answer["xscrollcommand"] = ans_scroll_x.set
ans_scroll_y = Scrollbar(lab_frame_answer, orient="vertical", command=text_answer.yview)
ans_scroll_y.pack(side=RIGHT, fill=Y)
text_answer.pack(fill=BOTH, expand=1)
text_answer["yscrollcommand"]=ans_scroll_y.set
answer_button = Button(lab_frame_answer,text="Показать ответ", command=view_question)
answer_button.pack()


lab_create_question = LabelFrame(root, text="Поле для создания вопроса")
lab_create_question.pack(fill=X, pady=30)
lab_create_txt = Label(lab_create_question,text="Поле для создания новых вопросов для блока")
lab_create_txt.pack(fill=X)

buttons=create_buttons(list_name_pictures)

main_menu = Menu()
add_question_menu = Menu(tearoff=0)
add_question_menu.add_command(label="Добавить", command=add_new_quest_wind)
add_question_menu.add_separator()
add_question_menu.add_command(label="Выход", command=exit)
main_menu.add_cascade(label="Меню", menu=add_question_menu)

root.config(menu=main_menu)

dict_photo_image = {}
for button in buttons:
    print(button.cget("text"))
    name_button = button.cget("text")

    if name_button in button_images:
        print("Yes!!!!")
        dict_photo_image[name_button] = PhotoImage(file=f"./pictures/{button_images[name_button]}")
        button.configure(image = dict_photo_image[name_button], compound=TOP)

print('вне функции: ', list_name_pictures)

root.mainloop()