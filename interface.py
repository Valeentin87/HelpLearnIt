from tkinter import *
import help_learn_system as hls

root = Tk()
root.title("Окно тестирования приложения")
root.geometry("1800x700")
root.resizable(False,False)
for c in range(6): root.columnconfigure(index=c, weight=1)
for r in range(3): root.rowconfigure(index=r,weight=1)

lab_header = Label(text = "Выберите блок данных с которым хотите работать", font=("Arial", 14), bg="#9ACD32")
add_question = Button(text="Добавить вопрос", bg="#FFFF00")
list_button = hls.list_name_files
list_name_pictures = ["java.png", "python3.png", "html.png","db.png","KS.png","linux.png"]
start = 0
global picture
ls_btn = []
for i in range(1,4):
    for j in range(3):
        if start > len(list_button)-1:
            ch_btn = Checkbutton(text="Пусто поле")
        else:
            picture_name = "./pictures/"+list_name_pictures[start]
            picture = PhotoImage(file=f"{picture_name}")
            ch_btn = Checkbutton(text=list_button[start],compound="bottom")
            
            ls_btn.append(ch_btn)
        
        
        ch_btn.grid(row=i, column=j, sticky="ew")
        start+=1
first_button = ls_btn[0]
second_button = ls_btn[1]
third_button = ls_btn[2]
fourth_button = ls_btn[3]
five_button = ls_btn[4]
six_button = ls_btn[5]
 

pict1 = PhotoImage(file="./pictures/java.png")
pict2= PhotoImage(file="./pictures/python3.png")       
pict3 = PhotoImage(file="./pictures/html.png")
pict4 = PhotoImage(file="./pictures/db.png")
pict5 = PhotoImage(file="./pictures/KS.png")
pict6 = PhotoImage(file="./pictures/linux.png")

first_button.config(image=pict1)
second_button.config(image=pict2)
third_button.config(image=pict3)
fourth_button.config(image=pict4)
five_button.config(image=pict5)
six_button.config(image=pict6)

        


add_question.grid(row=1, column=3, columnspan=4, rowspan=1, sticky="n", padx=2, pady=2)

lab_header.grid(column=0, row=0, columnspan=7, padx=4, pady=4, ipadx=5, ipady=5, sticky="nsew", )
root.mainloop()