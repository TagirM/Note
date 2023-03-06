import csv
import os.path

db_file_name = ''
db = []
global_id = 0


def init_data_base(file_name='db.csv'):
    global global_id
    global db
    global db_file_name
    db_file_name = file_name
    db.clear()
    if os.path.exists(db_file_name):
        with open(db_file_name, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            for row in reader:
                if (row[0] != ''):
                    db.append(row)
                    if (int(row[0]) > global_id):
                        global_id = int(row[0])
    else:
        open(db_file_name, 'w', newline='').close()


def create(header='', date='', content=''):
    global global_id
    global db
    global db_file_name
    if (header == ''):
        print('Не заполнено поле "Заголовок"')
        return
    if (content == ''):
        print('Не заполнено поле "Содержание"')
        return

    for row in db:
        if (row[1] == header.title() or row[3] == content.title()):
            print("Такая заметка уже существует")
            return

    global_id += 1
    new_row = [str(global_id), header.title(), date.title(), content.title()]
    db.append(new_row)
    with open(db_file_name, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_row)


# поиск (если нужно выгрузить все: result = retrive())
def retrive(id='', header='', date='', content=''):
    global global_id
    global db
    global db_file_name
    result = []
    for row in db:
        if (id != '' and row[0] != id):
            continue
        if (header != '' and row[1] != header):
            continue
        if (date != '' and row[2] != date):
            continue
        if (content != '' and row[3] != content):
            continue
        result.append(row)
    if len(result) == 0:
        return f'Заметка не найдена'
    else:        
        return result


def update(id='', header='', date='', new_id='', new_header='', new_date='', new_content=''):
    global global_id
    global db
    global db_file_name
    
    for row in db:
        if (row[0] == id or row[1] == header or row[2] == date):            
            if (new_id != ''):
                row[0] = new_id.title()
            if (new_header != ''):
                row[1] = new_header.title()
            if (new_date != ''):
                row[2] = new_date.title()
            if (new_content != ''):
                row[3] = new_content.title()
                
    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)        
        for row in db:
            writer.writerow(row)           


def delete(id='', header='', date=''):
    global global_id
    global db
    global db_file_name
    if (id == '' and header =='' and date == ''):
        print('Не заполнено поле')
        return

    for row in db:
        if (row[0] == id):
            db.remove(row)
            break
        if (row[1] == header):
            db.remove(row)
            break
        if (row[2] == date):
            db.remove(row)
            break

    with open(db_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';',
                            quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        for row in db:
            writer.writerow(row)

