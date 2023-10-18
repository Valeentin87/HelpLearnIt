class Question:
    '''класс описывает вопросы с их заголовками, формулировками и ответами'''
    def __init__(self, number_question, title, question, answer) -> None:
        self.number_question = number_question
        self.title = title
        self.question = question
        self.answer = answer
    
    def __str__(self) -> str:
        return f"Вопрос {self.number_question} Раздел: {self.title} Формулировка: {self.question}"





def parser_file(file_path) -> list:
    '''функция принимает относительный путь к файлу, позволяет парсить файл на отдельные вопросы'''
    list_questions = list()
    with open(f"{file_path}", "r", encoding="utf-8") as file:
        text_file = file.read()
    list_questions = text_file.split("--@&--")
    return list_questions




def create_questions(list):
    '''создает список объектов типа Questions принимая в качестве параметра распарсенный файл'''
    questions = []
    for item in list:
        item_list = item.split("/&*/")
        while(len(item_list) == 5):
            questions.append(Question(item_list[0].strip(' \n . ^'), item_list[1], item_list[3], item_list[4]))
            break
    return questions

def add_to_base_questions(questions:list, dict_base, name_title):
    '''обновляет информацию для базы данных в виде словаря с вопросами на основе полученного листа с объектами типа Questions'''
    dict_base.setdefault(name_title, questions)
    return dict_base

dict_qustions = {}
list_name_files = ["JAVA+.txt", "Python.txt", "HTML_CSS.txt","Базы_данных.txt","Компьютерные_сети.txt","Linux.txt"]

if __name__ == "__main__":

    

    
    for item in list_name_files:
        item_parser = parser_file(f"Files_from_parse/{item}")
        item_qustions = create_questions(item_parser)
        dict_qustions = add_to_base_questions(item_qustions, dict_qustions, item)



    
    for key in dict_qustions:
        print(key)




    