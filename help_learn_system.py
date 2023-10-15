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
            questions.append(Question(item_list[0], item_list[1], item_list[3], item_list[4]))
            break
    return questions


HTML_parser = parser_file("HTML_CSS/HTML_CSS_Создание_сайтов.txt")

HTML_questions = create_questions(HTML_parser)

for item in HTML_questions:
    print(item)