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

def add_to_base_questions(list_names_file):
    '''возвращает словарь, в котором ключами являются названия файлов а значениями список объектов класса questions'''
    pars_file = []
    questions_list = []
    list_list_questions = []
    dict_result = {}
    dict_from_each_file = {}
    for name_file in list_names_file:
        pars_file = parser_file(f"Files_from_parse/{name_file}")
        questions_list = create_questions(pars_file)
        
        dict_result.setdefault(name_file, questions_list)
    return dict_result



dict_qustions = {}
list_name_files = ["JAVA+.txt", "Python.txt", "HTML_CSS.txt","Базы_данных.txt","Компьютерные_сети.txt","Linux.txt"]

if __name__ == "__main__":
    result = add_to_base_questions(list_name_files)
    print(result)




    