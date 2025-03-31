
print("\033[37mDodam OS make by L.Doyun\033[37m")
import os,time,sys,tkinter, tempfile,subprocess,fileinput,ctypes,dpt,datetime,requests
from tempfile import TemporaryFile
version='0.8'
dir_=os.path.dirname(os.path.realpath(__file__)) #dir
dir__=dir_+'\\'
pyver=sys.version[0:6]
temp=''
templist=[]

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
        #AI
        if cmd.startswith('run_py_'):
            subprocess.run(["python", f"{cmd[11:]}"])  # Python 3
        elif cmd.startswith('run_app_'):
            print((f'{dir_}\\app'))
            subprocess.run(["python", f"{cmd[8:]}.py"], cwd=(f'{dir_}\\app'))
    elif cmd.startswith('dir_'):
        #AI
        if cmd.startswith('dir_app'):
            print('app의 앱들')
            folder_path=(f'{dir_}\\app')
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)

                if os.path.isfile(file_path):
                    # 확장자 제거
                    file_name_without_ext = os.path.splitext(file_name)[0]

                    # 마지막 수정 날짜 가져오기
                    timestamp = os.path.getmtime(file_path)
                    formatted_date = datetime.datetime.fromtimestamp(timestamp).strftime("%Y%m%d")

                    # 출력
                    print(f"앱 이름:{file_name_without_ext} 설치된 날짜:{formatted_date}")
    elif cmd.startswith('store_'):

        # 🔹 GitHub RAW URL로 변환 (중요!!)
        github_raw_url = f"https://raw.githubusercontent.com/dodam2015/DodamDosApps/main/{cmd[6:]}.py"

        # 🔹 저장할 폴더 경로 설정
        save_folder = os.path.join(dir_, "app")  # OS 호환성 고려
        os.makedirs(save_folder, exist_ok=True)  # 폴더가 없으면 생성

        # 🔹 저장할 파일 경로
        file_name = f"{cmd[6:]}.py"  # 파일명 설정
        save_path = os.path.join(save_folder, file_name)

        # 🔹 파일 다운로드
        response = requests.get(github_raw_url)

        if response.status_code == 200:  # 다운로드 성공 여부 확인
            with open(save_path, "wb") as file:
                file.write(response.content)
            print(f"✅ 파일 다운로드 완료: {save_path}")
        else:
            print(f"❌ 다운로드 실패! 상태 코드: {response.status_code}")

    else:
        if cmd=='' or cmd==' ':
            pass
        else:
            print(f'{cmd}는/은 유효한 명령어가 아닙니다.')