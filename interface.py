from tkinter import *
import help_learn_system as hls

root = Tk()
root.title("Окно тестирования приложения")
root.geometry("1200x700")
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
            ch_btn = Checkbutton(text="Пусто поле", borderwidth=2)
        else:
            picture_name = "./pictures/"+list_name_pictures[start]
            picture = PhotoImage(file=f"{picture_name}")
            ch_btn = Checkbutton(text=list_button[start])
            
            ls_btn.append(ch_btn)
        
        ch_btn.config(image=picture, compound="bottom")
        ch_btn.grid(row=i, column=j, sticky="n")
        start+=1

        


add_question.grid(row=1, column=3, columnspan=4, rowspan=3, sticky="n", padx=2, pady=2)

lab_header.grid(column=0, row=0, columnspan=7, padx=4, pady=4, ipadx=5, ipady=5, sticky="nsew", )
root.mainloop()