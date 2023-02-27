import Notice



def run():
    n = Notice.Notice()
    while True:
        com = input("Ввведите команду(DELETE, UPDATE, INSERT, READ, EXIT)")
        if com == 'DELETE':
            id = input("Если вы хотите удалить заметку, напишите его ID:")
            n.delete_notice(int(id))
        elif com == 'UPDATE':
            id = int(input("Если вы хотите изменить заметку, напишите его ID:"))
            n.read_notice(id=id)
            title = input("Если хотите заменить заголовок, напишите его:")
            body = input("Если хотите заменить текст заметки, напишите его:")
            n.update_line(id, title, body)
        elif com == 'READ':
            n.read_all()
        elif com == 'INSERT':
            title = input("Напишите заголовок:")
            body = input("Напишите текст заметки:")
            n.insert_notice(title=title, body=body)
        elif com == 'UPDATE':
            id = int(input("Если вы хотите прочитать заметку, напишите его ID:"))
            n.read_notice(id=id)
        elif com == 'EXIT':
            break
        else:
            print("Я не понимаю Вашей команды, пожалуйста повторите(DELETE, UPDATE, ALL, INSERT, READ, EXIT):")