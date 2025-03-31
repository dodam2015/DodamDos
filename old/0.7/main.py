


print("\033[37mDodam OS make by L.Doyun\033[37m")
import os,time,sys,tkinter, tempfile,subprocess,fileinput,ctypes
from tempfile import TemporaryFile
version='0.7'
dir_=os.path.dirname(os.path.realpath(__file__)) #dir
dir__=dir_+'\\'
pyver=sys.version[0:6]
temp=''
templist=[]

def file_read_all(file_name):
    f = open((dir_+'\\'+file_name), "r", encoding="utf-8")
    data = f.read()
    print(data)
    f.close()

fp=TemporaryFile('w+t')
fp.write('|DodamDos Temp|\n')
fp.write('|load end|\n')

def plus(*a):
    temp=0
    for i in range(0,len(a)+1):
        temp=temp+i
    return temp



print('made by Air.')
print('한국어')
temp=os.path.isfile((dir_+'\\'+'systemfile.txt'))
if temp:
    pass
    fp.write('|isfile systemfile|\n')
else:
    f=open((dir_+'\\'+'systemfile.txt'),'w')
    temp=input('이름을 입력하시오:')
    f.write(f'osname_____Dodam OS\nosversion__{version}\nname_______{temp}\nsys_yes____yes\nsys_no_____no')
    print('installed')
    f.close

#read ver
f = open((dir_+'\\'+'systemfile.txt'), "r", encoding="utf-8")
templist = f.readlines()
f.close()
if templist[1][11:-1]!=version:
    print(templist[1][11:-1])
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

    if cmd.startswith('help_'):
        if cmd.startswith('help'):
            print('1.output()')
            print('2.is')
            print('|->var()')
            print('3.run')
            print('|->_temp_open')
            print('|->_[programname.py]')
        elif cmd.startswith('help_system'):
            print('시스템 정보:')
            f = open((dir_+'\\'+'systemfile.txt'), "r", encoding="utf-8")
            templist = f.readlines()
            f.close()
            print(f'DodamDOS버전: {templist[1][11:-1]}')
    elif cmd.startswith('output(')and cmd[-1]==')':
        fp.write(f'user enter: {cmd}\n')
        print(f'{cmd[7:-1]}')

    elif cmd.startswith('is'):
        fp.write(f'user enter: {cmd}\n')
        if cmd[2:6]=='var(' and cmd[-1]==')':
            if cmd[6:-1] in locals():
                print(f'{cmd[6:-1]} 변수는 존재합니다.')
            else:
                print(f'{cmd[6:-1]} 변수는 존재하지 않습니다.')

    elif cmd.startswith('run_'):
        if cmd.startswith('temp_open'):
            fp.write(f'user enter: {cmd}\n')
            fp.seek(0)
            temp=fp.read()
            print('data:')
            print(temp)
        else: 
            #아니 진짜 왜안되(돼)!!!! 걍 AI불러와(chatgpt)
            #Tl 야 그냥 다시 해!!!! [6:]
            #다시함(인터냇보고)
            subprocess.run(args=[dir__,cmd[6:]])
            print(f'\n파이썬 프로그램 실행이 끝났습니다. 이름:{cmd[6:]}')
    elif cmd.startswith('L.Doyun'):
        print('I am so sad becaus my this program is not real OS....')
    else:
        if cmd=='' or cmd==' ':
            pass
        else:
            print(f'{cmd}는/은 유효한 명령어가 아닙니다.')