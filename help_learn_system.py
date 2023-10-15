def parser_file(file_path) -> list:
    '''функция принимает относительный путь к файлу, позволяет парсить файл на отдельные вопросы'''
    list_questions = list()
    with open(f"{file_path}", "r", encoding="utf-8") as file:
        text_file = file.read()
    list_questions = text_file.split("--@&--")
    return list_questions

HTML_questions = parser_file("HTML_CSS/HTML_CSS_Создание_сайтов.txt")
print(HTML_questions)