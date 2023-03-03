from ftplib import FTP
import key


ftp = FTP(key.FTP)
ftp.login(key.Login, key.password)

def get_file_list(path='/adm'):

    f_a_f = []
    dirs = []
    f_a_f.extend(ftp.nlst(path))
    print('faf_1', f_a_f)

    for i in range(len(f_a_f)):
        if len(f_a_f[i].split('.')) < 2:
            dirs.append(f_a_f[i])
            print('dirs_1', dirs)


    print('faf_2', f_a_f)

def get_path_file_to_add_widget():
    Temporary_array = []
    files_and_folder = []
    files = ftp.nlst()

    for i in range(len(files)):
        if len(files[i].split('.')) > 1:
            current_directory = ftp.pwd()
            Temporary_array.append(f"[{current_directory}]/{files[i]}")

        else:
            ftp.cwd(files[i]) #!!!!!Пытается получить доступ к файлам
            current_directory = ftp.pwd()
            Temporary_array.append(f"/{files[i]}")
            ftp.cwd('../')

    print(Temporary_array)

ftp.quit()