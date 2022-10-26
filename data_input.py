def get_surname():
    surname = input('Введите фамилию: ')
    return surname

def get_name():
    name = input('Введите имя: ')
    return name

def get_phone():
    phone = input('Введите номер телефона: ')
    return phone

def get_description():
    description = input('Введите описание: ')
    return description

def get_record(sname, nm, ph, descr):
    new_record = {}
    new_record['surname'] = sname
    new_record['name'] = nm
    new_record['phone'] = ph
    new_record['description'] = descr
    return new_record