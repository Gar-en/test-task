from file_interaction import FileInteraction

def main():

    f_inter = input("Выберите действие(Получить всю информацию(r); Добавить новую запись(a); Получить одну запись(r1); Редактирование строки(e); Выход(exit)):" )

    match f_inter:
        case "r":
            FileInteraction.read_all()
            main()
        case "a":
            text = input("Введите ФИО, название компанни, номер телефона компании, и личный номер телефона сотрудника: ")
            FileInteraction.add_contact(text)
            main()
        case "r1":
            text = input("Введите ФИО сотрудника или название компании: ")
            FileInteraction.read_one(text)
            main()
        case "e":
            string = input("Введите ФИО сотрудника или название компании: ")
            old_text = input("Введите что вы хотите изменить: ")
            new_text = input("Введите новую информацию: ")
            FileInteraction.edit_file(string, old_text, new_text)
            main()
        case "exit":
            exit()
        case _:
            print("Ошибка ввода. Попробуйте ещё раз")
            main()

main()