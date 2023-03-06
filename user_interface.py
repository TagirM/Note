import time
import crud as cr
from datetime import datetime


print('\nВас приветствует приложение "Заметки"')


def ls_menu():
    while True:
        print('\nМЕНЮ')
        print('1. Показать все заметки.')
        print('2. Найти заметки по заголовку.') 
        print('3. Найти заметки по id.')
        print('4. Найти заметки по дате и времени (в формате "2019-12-13 19:44:25").')
        print('5. Добавить новую заметку.')
        print('6. Изменить существующую заметку.')
        print('7. Удалить заметку.')
        print('8. Закрыть программу.\n')
        n = сhecking_the_number(input('Выберите пункт меню: '))

        if n == 1:
            print(cr.retrive())

        elif n == 2:
            search = input('Введите заголовок заметки: ')
            print(cr.retrive(header=search))

        elif n == 3:
            search = input('Введите id заметки: ')
            print(cr.retrive(id=search))

        elif n == 4:
            search = input('Введите дату и время заметки (в формате "2019-12-13 19:44:25"): ')
            print(cr.retrive(date=search))

        elif n == 5:
            header = input('Введите заголовок заметки: ')
            date = str(datetime.fromtimestamp(round(time.time())))
            content = input('Введите содержание заметки: ')
            cr.create(header, date, content)

        elif n == 6:
            print('1. Найти заметку по заголовку.')
            print('2. Найти заметку по id.')
            print('3. Найти заметку по дате и времени (в формате "2019-12-13 19:44:25").')
            change = сhecking_the_number(input('Введите номер пункта: '))

            if change == 1:
                search = input('Введите заголовок заметки: ')
                if (search != ''):                    
                    if cr.retrive(header=search)!='Заметка не найдена':
                        print(cr.retrive(header=search))
                        new_id = input('Введите измененный id заметки: ')
                        new_header = input('Введите измененный заголовок заметки: ')
                        new_content = input('Введите измененное содержание заметки: ')
                        new_date = str(datetime.fromtimestamp(round(time.time())))
                        cr.update(header=search, new_id=new_id, new_header=new_header,
                            new_date=new_date, new_content=new_content)
                        print(cr.retrive(header=new_header))
                    else: 
                        print('Указанный заголовок отсутствует')                        
                else: print('Не ввели заголовок для изменения')

            elif change == 2:
                search = input('Введите id заметки: ')
                if (search != ''):                    
                    if cr.retrive(id=search)!='Заметка не найдена':
                        print(cr.retrive(id=search))
                        new_id = input('Введите измененный id заметки: ')
                        new_header = input('Введите измененный заголовок заметки: ')
                        new_content = input('Введите измененное содержание заметки: ')
                        new_date = str(datetime.fromtimestamp(round(time.time())))
                        cr.update(id=search, new_id=new_id, new_header=new_header,
                                new_date=new_date, new_content=new_content)
                        print(cr.retrive(id=new_id))
                    else: 
                        print('Указанный id отсутствует')                        
                else: print('Не ввели id для изменения')

            elif change == 3:
                search = input('Введите дату и время заметки (в формате "2019-12-13 19:44:25"): ')
                if (search != ''):                    
                    if cr.retrive(date=search)!='Заметка не найдена':
                        print(cr.retrive(date=search))
                        new_id = input('Введите измененный id заметки: ')
                        new_header = input('Введите измененный заголовок заметки: ')
                        new_content = input('Введите измененное содержание заметки: ')
                        new_date = str(datetime.fromtimestamp(round(time.time())))
                        cr.update(date=search, new_id=new_id, new_header=new_header,
                                new_date=new_date, new_content=new_content)
                        print(cr.retrive(date=new_date))
                    else: 
                        print('Указанная дата и время отсутствует')                        
                else: print('Не ввели дату и время для изменения')

            else:
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

        elif n == 7:
            print('1. Найти заметку по заголовку.')
            print('2. Найти заметку по id.')
            print('3. Найти заметку по дате и времени (в формате "2019-12-13 19:44:25").')
            deleting = сhecking_the_number(input('Введите номер пункта: '))

            if deleting == 1:
                search = input('Введите заголовок заметки: ')
                if (search != ''):
                    if cr.retrive(header=search)!='Заметка не найдена':
                        print(cr.retrive(header=search))
                        check = input('Подтвердите удаление yes/no: ')
                        if (check != ''):
                            if (check == 'yes'):
                                cr.delete(header=search)
                            elif (check == 'no'):
                                print("Вы отменили удаление")
                            else:
                                print("Вы ввели некорреткную операцию")
                        else:
                            print("Вы не ввели подтверждение")                        
                    else: 
                        print('Указанный заголовок отсутствует')                        
                else: print('Не ввели заголовок для удаления')

            elif deleting == 2:
                search = input('Введите id заметки: ')
                if (search != ''):
                    if cr.retrive(id=search)!='Заметка не найдена':
                        print(cr.retrive(id=search))
                        check = input('Подтвердите удаление yes/no: ')
                        if (check != ''):
                            if (check == 'yes'):
                                cr.delete(id=search)
                            elif (check == 'no'):
                                print("Вы отменили удаление")
                            else:
                                print("Вы ввели некорреткную операцию")
                        else:
                            print("Вы не ввели подтверждение")                        
                    else: 
                        print('Указанный id отсутствует')                        
                else: print('Не ввели id для удаления')


            elif deleting == 3:
                search = input('Введите дату и время заметки (в формате "2019-12-13 19:44:25"): ')
                if (search != ''):
                    if cr.retrive(date=search)!='Заметка не найдена':
                        print(cr.retrive(date=search))
                        check = input('Подтвердите удаление yes/no: ')                
                        if (check != ''):
                            if (check == 'yes'):
                                cr.delete(date=search)
                            elif (check == 'no'):
                                print("Вы отменили удаление")
                            else:
                                print("Вы ввели некорреткную операцию")
                        else:
                            print("Вы не ввели подтверждение")                        
                    else: 
                        print('Указанные дата и время отсутствуют')                        
                else: print('Не ввели дату и время для удаления')

            else:
                print(
                    '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

        elif n == 8:
            print('Спасибо за работу!')
            break

        else:            
            print(
                '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

def сhecking_the_number(arg):
    while arg.isdigit() != True:        
        print('\nВы ввели не число.')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)
