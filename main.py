from ftplib import FTP
import os


ftp = FTP('ftp.smoff.ru')
ftp.login('FTP-SemenovI2', 'VYX9tGnV')

all_files = []
files_arr = []
files = ftp.nlst()

for i in range(len(files)):
    try:
        ftp.cwd(files[i]) #!!!!!Пытается получить доступ к файлам
        all_files.append(ftp.nlst())
        ftp.cwd('../')

    except:
        pass

for i in range(len(all_files)):
    for j in range(len(all_files[i])):
        check_extension = all_files[i][j].split('.')
        file = []
        folders = []
        print(check_extension)
        if len(check_extension) >= 2:
            file.append(all_files[i][j])
            print('file', file)

        elif len(check_extension) <= 1:
            folders.append(all_files[i][j])
            print(folders)
            print('file', folders)

        files_arr.append(file)
        files_arr.append(folders)

print(files_arr)
ftp.quit()