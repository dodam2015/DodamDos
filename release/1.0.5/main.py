
print("\033[37mDodam OS make by L.Doyun\033[37m")
import os,sys,subprocess,datetime,requests
from tempfile import TemporaryFile
from datetime import time
version='1.0.5'
dir_=os.path.dirname(os.path.realpath(__file__)) #dir
dir__=dir_+'\\'
sysdir = os.path.join(dir__, 'systemfile.txt')  # ✅ 올바른 문자열 경로
pyver=sys.version[0:6]
temp=''
templist=[]
ifdeveloper=False

fp=TemporaryFile('w+t')
fp.write('|DodamDos Temp|\n')
fp.write('|load end|\n')

def plus(*a):
    temp=0
    for i in range(0,len(a)+1):
        temp=temp+i
    return temp
def modify_line_in_file(file_path, line_number, new_content):
    if not os.path.exists(file_path):
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if line_number < 1 or line_number > len(lines):
        print("error line defind")
        return

    lines[line_number - 1] = new_content + '\n'

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

try:
    f = open((dir_+'\\'+'systemfile.txt'), "r", encoding="utf-8")
    templist = f.readlines()
    f.close()
    if templist[3]=='developer__True':
        print('developer mode True')
        ifdeveloper=True
    else:
        pass
except Exception as error:
    ifdeveloper=False
    pass


print('한국어')
temp=os.path.isfile((dir_+'\\'+'systemfile.txt'))
if temp:
    pass
    fp.write('|isfile systemfile|\n')
else:
    f=open((dir_+'\\'+'systemfile.txt'),'w')
    temp=input('이름을 입력하시오:')
    f.write(f'osname_____Dodam OS\nosversion__{version}\nname_______{temp}\ndeveloper__False\nPersinfor__False')
    print('installed')
    f.close

#read ver
f = open((dir_+'\\'+'systemfile.txt'), "r", encoding="utf-8")
templist = f.readlines()
f.close()
if templist[1][11:-1]!=version:
    print(templist[1][11:-1])
    print('에러 코드100: 파일 버전 맞지 않음.')
    pass
else:
    pass
print(f'파이썬 버전:{sys.version[0:6]}')
fp.write(f'|Python Version: {sys.version[0:6]}|\n')
cmd=''
while cmd!='exit()':
    try: #AI
        with open(os.path.join(dir_, 'systemfile.txt'), "r", encoding="utf-8") as f:
            templist = f.readlines()
        print(templist[4][11:].strip())  # 🔹 개행 문자 및 공백 제거 후 출력
        if templist[4][11:].strip() == 'False':  # 🔹 strip() 사용하여 비교
            cmd = input(f"{dir_}\\")
        elif templist[4][11:].strip() == 'True':
            cmd = input(f">")
        else:
            cmd = input('error>')
        fp.write('user inputting...\n')
    except Exception as error:
        print(f"오류 발생: {error}")  # 🔹 오류 메시지를 더 명확하게 출력

    if cmd.startswith('help'):
        if cmd.startswith('help_help'):
            print('1.output([outputtext])')
            print('2.is_')
            print('->var([varname])')
            print('3.run_')
            print('->py_[filename]')
            print('->app_[appname]')
            print('4.dir_')
            print('->_app')
            print('->')
            print('5.store_[you_want_download_appname]')
            print('6.time')
            print('7.settings_')
            print('->settings_Persinfor_')
            print('->->True')
            print('->->False')
        elif cmd.startswith('help_system'):
            print('시스템 정보:')
            print('made by L.Doyun')
            f = open((dir_+'\\'+'systemfile.txt'), "r", encoding="utf-8")
            templist = f.readlines()
            f.close()
            print(f'DodamDOS버전: {templist[1][11:-1]}')
            print(f'파이썬 버전: {pyver}')
            print(f'사용자 이름: {templist[2][11:]}')
    
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
        elif cmd.startswith('dir_'):
            print('main의 앱들')
            folder_path=(f'{dir_}')
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)

                if os.path.isfile(file_path):
                    # 확장자 제거
                    file_name_without_ext = os.path.splitext(file_name)[0]

                    # 마지막 수정 날짜 가져오기
                    timestamp = os.path.getmtime(file_path)
                    formatted_date = datetime.datetime.fromtimestamp(timestamp).strftime("%Y%m%d")

                    # 출력
                    print(f"{file_name_without_ext} 만든 날짜:{formatted_date}")
    elif cmd.startswith('store_'):
        #AI
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
            print(f"파일 다운로드 완료:")
        else:
            print(f"다운로드 실패! 상태 코드: {response.status_code}")
    elif cmd == 'time':
        now = datetime.datetime.now()
        print (now.strftime("%Y%m%d"))
    elif cmd=='developer':
        if ifdeveloper:
            print('app loading')
            subprocess.run(["python", f"{dir__}GrohnThERUfH\\wegjwrg.py"])  # Python 3
        else:
            pass
    elif cmd.startswith('settings_'):
        #AI
        if cmd.startswith('settings_Persinfor_'):
            print(cmd[19:])
            if cmd[19:]=='True':
                modify_line_in_file(sysdir, 5, 'Persinfor__True')  # 문자열 경로 전달
            elif cmd[19:]=='False':
                modify_line_in_file(sysdir, 5, 'Persinfor__False')  # 문자열 경로 전달

    else:
        if cmd=='' or cmd==' ':
            pass
        else:
            print(f'{cmd}는/은 유효한 명령어가 아닙니다.')