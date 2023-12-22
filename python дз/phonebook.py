def show_all(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
        print("".join(data))
        

def remove(file_name: str):
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    data = ""
    with open(file_name, 'r', encoding='utf-8') as f:
            data = f.readlines()
            s = f'{last_name}, {first_name}, {patronymic}, {phone_number}\n'
            data.remove(s)
    with open(file_name, 'w') as f:
        f.writelines(data)
            
def modify(file_name: str):
    # print("Введите данные для поиска:\n")
    # last_name = input('Введите фамилию: ')
    # first_name = input('Введите имя: ')
    # patronymic = input('Введите отчество: ')
    # phone_number = input('Введите номер телефона: ')
    old_data = find(file_name, True)

    print("Введите новые данные:")
    new_last_name = input('Введите новую фамилию: ')
    new_first_name = input('Введите новое имя: ')
    new_patronymic = input('Введите новое отчество: ')
    new_phone_number = input('Введите новый номер телефона: ')
    data = ""
    with open(file_name, 'r', encoding='utf-8') as f:
            data = f.readlines()
            i = data.index(old_data)
            data[i] = f'{new_last_name}, {new_first_name}, {new_patronymic}, {new_phone_number}\n'
    with open(file_name, 'w', encoding='utf-8') as f:
            f.writelines(data)



def find(file_name: str, option: bool):
    a = input("Введите 1 для поиска по фамилии, 2 для поиска по имени: ")
    opt = 0
    if a =='1':
        opt = 0
    elif a =='2':
        opt = 1
    
    attr = input("Введите имя/фамилия для поиска: ")
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f. readlines()
        data = list(filter(lambda x: x.split(', ')[opt] == attr,data))
        print(list(zip(range(1, len(data) + 1), data)))
        if option:
            id = input("Введите id нужного пользователя для изменения данных: ")
        else:
             id = input("Введите id нужного пользователя: ")
        return data[int(id)-1]

def copy_file(source_file: str, destination_file: str):
    with open(source_file, 'r', encoding='utf-8') as source:
        with open(destination_file, 'w', encoding='utf-8') as destination:
            for line in source:
                destination.write(line)
    print("Файл успешно скопирован.")



def add_new(file_name: str):
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    # f = open(file_name, 'a', encoding='utf-8')
    # f.close()
    with open(file_name, 'a', encoding='utf-8') as fd:
        fd.write(f'{last_name}, {first_name}, {patronymic}, {phone_number}\n')
# Иванов , Иван, Иванович, 12345
# Петров, Петя, Сидорович, 361
# Пупкин, Иван, Сидорович, 98765
# Иванов, Иван, Иванович, 1234
# Пупкин, Вася, Романович, 4321

def main():
    file_name = 'phonebook.txt'
    flag_exit = False
    while not flag_exit:
        print('1 - показать все записи')
        print('2 - добавить записи')
        print('3 - удалить запись')
        print('4 - изменить запись')
        print('5 - поиск запись по фамилии\имени: ')
        print('6 - копирование файла')
        answer = input('Введите операцию или * для выхода: ')
        if answer == '1':
            show_all(file_name)
        elif answer == '2':
            add_new(file_name)
        elif answer == '3':
            remove(file_name)
        elif answer == '4':
            modify(file_name)
        elif answer == '5':
            print(find(file_name, False))
        elif answer == '6':
            source_file = input("Введите имя исходного файла: ")
            destination_file = input("Введите имя файла назначения: ")
            copy_file(source_file, destination_file)    
        elif answer == '*':
            flag_exit = True


if __name__ == '__main__':
    main()