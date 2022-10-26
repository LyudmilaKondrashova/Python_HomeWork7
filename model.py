import data_input
import control

def read_file_csv(flname):
    data = []
    fields = ["surname", "name", "phone", "description"]
    with open(flname, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    fin.close()
    return data

def all_phonebook():
    data_csv = read_file_csv('phonebook.csv')
    for line in data_csv:
        print(line)
    control.button_click()

def find_subscriber_surname():
    print('\nВведите фамилию абонента полностью или несколько первых букв:')
    surname = input()
    data = read_file_csv('phonebook.csv')
    fl_ab = False
    for el in data:
        if surname.lower() in el['surname'].lower():
            if not fl_ab:
                print('Найдены следующие абоненты:')
            print(el)
            fl_ab = True
    if not fl_ab:
        print('Такого абонента в справочнике нет!')
    control.button_click()

def find_subscriber_phone():
    print('\nВведите телефон абонента полностью или несколько цифр:')
    phone = input()
    data = read_file_csv('phonebook.csv')
    fl_ab = False
    for el in data:
        if phone.lower() in el['phone'].lower():
            if not fl_ab:
                print('Найдены следующие абоненты:')
            print(el)
            fl_ab = True
    if not fl_ab:
            print('Такого абонента в справочнике нет!')
    control.button_click()

def new_subscriber():
    new_subs = data_input.get_record(data_input.get_surname(),
                          data_input.get_name(), data_input.get_phone(),
                          data_input.get_description())
    
    write_file_csv('phonebook.csv', new_subs)
        
def write_file_csv(flname, new_record):
    filescv = open(flname, 'a', encoding='utf-8')
    filescv.write('\n' + new_record['surname'] + ',' + new_record['name'] + ',' + new_record['phone'] + ',' + new_record['description'])
    print('Абонент добавлен в справочник')
    filescv.close()
    control.button_click()

def save_to_text():
    data = read_file_csv('phonebook.csv')
    filetxt = open('phonebook.txt', 'w', encoding='utf-8')
    for line in data:
        filetxt.write(line['surname'] + ',' + line['name'] + ',' + line['phone'] + ',' + line['description'] + '\n')
    filetxt.close()
    print('Справочник сохранен в файл phonebook.txt')
    control.button_click()
        
    
def finish_work():
    print('Работа приложения завершена!')