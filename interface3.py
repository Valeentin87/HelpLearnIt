from tkinter import *
import inspect
root = Tk()

list_name_pictures = ["JAVA+.txt", "Python.txt", "HTML_CSS.txt","Базы_данных.txt","Компьютерные_сети.txt","Linux.txt"]
button_images = {"Базы_данных.txt":"db.png",
                 "Компьютерные_сети.txt":"KS.png",
                 "HTML_CSS.txt":"html.png",
                 "JAVA+.txt":"java.png",
                 "Linux.txt":"linux.png",
                 "Python.txt":"python3.png"}

buttons_frame = LabelFrame(text="Выберите блок или несколько для изучения:", width=700)
buttons_frame.pack(side=TOP, padx=5, pady=5)
label_buttons = Label(buttons_frame, text="Отметте флажки возле блоков, которые хотите изучать:")
label_buttons.pack()


def check_status_button():
    list_status_button = []
    for key, value in dict_int_var.items():
        list_status_button.append((key, value.get()))
    #     if value.get():
    #         list_status_button.append(key)
    # print(list_status_button)
    # return list_status_button
    print(list_status_button)




dict_int_var = {}

for name  in list_name_pictures:
    dict_int_var[name] = IntVar()



def create_buttons(name_pictures):
    btn_list = []
    dict_name_directory = {}
    for key in button_images:
        dict_name_directory[key]= f"pictures/{button_images[key]}"
    
    global button_picture
    for name in name_pictures:
        
        button_picture = PhotoImage(file=dict_name_directory[name])
        chbtn = Checkbutton(buttons_frame, text=name, variable=dict_int_var[name])
        chbtn.configure(image=button_picture, compound=TOP)
        btn_list.append(chbtn)
        chbtn.pack(side=LEFT)
    return btn_list

buttons = create_buttons(list_name_pictures)




check_buttons = Button(buttons_frame, text="Проверить статус кнопок", command=check_status_button)
check_buttons.pack(anchor=S)

print(inspect.isclass(PhotoImage))

root.mainloop()