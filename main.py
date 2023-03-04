from ftplib import FTP
import key
import os


ftp = FTP(key.FTP)
ftp.login(key.Login, key.password)

def get_file_list(path='/test_folder'):
    files = []
    dirs = []
    all_in_path = []
    all_in_path.extend(ftp.nlst(path))

    for i in range(len(all_in_path)):
        if len(all_in_path[i].split('.')) == 1:
            dirs.append(all_in_path[i])

        else:
            files.append(all_in_path[i])

    print('files', files)
    print('dirs_2', dirs)

def get_path_file_to_add_widget():
    files_and_folder = []
    files = ftp.nlst()

    for i in range(len(files)):
        if len(files[i].split('.')) > 1:
            current_directory = ftp.pwd()
            files_and_folder.append(f"[{current_directory}]/{files[i]}")

        else:
            ftp.cwd(files[i])
            files_and_folder.append(f"/{files[i]}")
            ftp.cwd('../')

    print(files_and_folder)

def add_foler(path='/test_folder'):
    ftp.cwd(path)
    for i in range(10):
        ftp.mkd(f'some_folder_{i}')

def old_get_path_file_to_add_widget():
    Temporary_array = []
    ftp.cwd('/test_folder')
    files = ftp.nlst()

    for i in range(len(files)):
        if len(files[i].split('.')) > 1:
            print(files[i].split('.'))
            current_directory = ftp.pwd()
            Temporary_array.append(f"[{current_directory}]/{files[i]}")

        else:
            ftp.cwd(files[i]) #!!!!!Пытается получить доступ к файлам
            current_directory = ftp.pwd()
            Temporary_array.append(f"/{files[i]}")
            ftp.cwd('../')

    print(Temporary_array)

get_file_list()

ftp.quit()