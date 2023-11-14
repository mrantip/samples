 # Пример кода, который позволяет указать путь к файлу 'file.txt',
 # находящемуся в той же папке, что и скрипт, который вы запускаете:
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
element.send_keys(file_path)