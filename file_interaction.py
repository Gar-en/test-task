class FileInteraction:

# Функция read_all выводит всю информацию из текстового файла
    def read_all():
        with open('test.txt', 'r', encoding='utf-8') as file: # Открываем файл для чтения
            print(file.read()) # Вывод всего что находится в файле

# Функция add_contact создаёт новую запись в файле
    def add_contact(text):
        with open('test.txt', 'a', encoding='utf-8') as file: # Открываем файл для изменения
            file.write(text, '\n') # Записываем в файл текст который ввёл пользователь

# Функция read_one выводит из файла одну запись по указаным подстрокам(ФИО, название компании)
    def read_one(text):
        with open('test.txt', 'r', encoding='utf-8') as file: # Открываем файл для чтения
            for line in file: # В цикле перебираем все строки в файле. Если введённый текст есть в рассматриваемой строке, то выводим строку
                if text in line:
                    print(line)

# Функция edit_file позволяет редактировать файл
    def edit_file(string, old_text, new_text): # string - строка в которой ищем, old_text - подстрока которую нужно заменить, 
                                                # new_text - новая подстрока на которую нужно заменить старый текст
        with open('test.txt', 'r', encoding='utf-8') as file: # Открываем файл для чтения
            file_data = file.read() # В переменную записываем то, что считали из файла
            file_data = file_data.replace(old_text, new_text) # В переменной file_data заменяем старую подстроку на новую
        with open('test.txt', 'w', encoding='utf-8') as file: # Открыаем файл для записи
            file.write(file_data) # Записываем в файл изменённые данные