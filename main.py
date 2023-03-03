from ftplib import FTP
import os


ftp = FTP('ftp.smoff.ru')
ftp.login('FTP-SemenovI2', 'VYX9tGnV')

Temporary_array = []
files_and_folder = []
files = ftp.nlst()

for i in range(len(files)):
    if len(files[i].split('.')) > 1:
        Temporary_array.append(files[i])

    else:
        ftp.cwd(files[i]) #!!!!!Пытается получить доступ к файлам
        Temporary_array.append(ftp.nlst())
        ftp.cwd('../')

for i in range(len(Temporary_array)):
    for j in range(len(Temporary_array[i])):
        files_and_folder.append(Temporary_array[i][j])

print(files_and_folder)

ftp.quit()