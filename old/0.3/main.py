print("\033[37mDodam OS make by L.Doyun\033[37m")
import os,time,sys,tkinter, tempfile
from tempfile import TemporaryFile
version='0.3'
dir_=os.path.dirname(os.path.realpath(__file__))
temp=''
def file_read_all(file_name):
    f = open((dir_+'\\'+file_name), "r", encoding="utf-8")
    data = f.read()
    print(data)
    f.close()

fp=TemporaryFile('w+t')
fp.write('|DodamDos Temp|\n')
fp.write('|load end|\n')





print('made by Air.')
print('한국어')
temp=os.path.isfile((dir_+'\\'+'systemfile.txt'))
if temp:
    pass
    fp.write('|isfile systemfile|\n')
else:
    f=open((dir_+'\\'+'systemfile.txt'),'w')
    f.write(f'osname_____Dodam OS\nosversion__{version}\n')
    print('installed')
    f.close

#read
f = open((dir_+'\\'+'systemfile.txt'), "r", encoding="utf-8")
temp = f.read()
f.close()
if temp[31:-1:]!=version:
    print('에러 코드100: 파일 버전 맞지 않음.')
    sys.exit()
else:
    pass
print(f'파이썬 버전:{sys.version[0:6]}')
fp.write(f'|Python Version: {sys.version[0:6]}|\n')
cmd=''
while cmd!='exit()':
    cmd=input(f"{dir_+'\\'}")
    fp.write('user inputing...\n')
    if cmd.startswith('output(')and cmd[-1]==')':
        fp.write(f'user enter: {cmd}')
        print(f'{cmd[7:-1]}')
    elif cmd.startswith('is'):
        fp.write(f'user enter: {cmd}\n')
        if cmd[2:6]=='var(' and cmd[-1]==')':
            if cmd[6:-1] in locals():
                print(f'{cmd[6:-1]} 변수는 존재합니다.')
            else:
                print(f'{cmd[6:-1]} 변수는 존재하지 않습니다.')
    elif cmd.startswith('temp'):
        if cmd[4:]=='_open':
            fp.write(f'user enter: {cmd}\n')
            fp.seek(0)
            temp=fp.read()
            print('data:')
            print(temp) 
    else:
        if cmd=='' or cmd==' ':
            pass
        else:
            print(f'{cmd}는/은 유효한 명령어가 아닙니다.')