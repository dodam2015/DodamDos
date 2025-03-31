import time
from tqdm import tqdm
import curses
import os
import subprocess
import requests

cd = os.path.join(os.path.dirname(os.path.abspath(__file__)), "user").replace("\\", "/")

print('loaded.')
time.sleep(2)
print('[한국어]')

def loading_bar(total):
    for i in tqdm(range(total), desc="Loading", unit="step"):
        time.sleep(0.01)

if __name__ == "__main__":
    total_steps = 100
    loading_bar(total_steps)

def blinking_text(stdscr):
    curses.curs_set(0)
    text = "|"
    blink = True

    for _ in range(5):
        stdscr.clear()

        if blink:
            stdscr.addstr(0, 0, text)
        else:
            stdscr.addstr(0, 0, " " * len(text))

        stdscr.refresh()
        blink = not blink

        time.sleep(0.5)

if __name__ == "__main__":
    curses.wrapper(blinking_text)

for i in range(10):
    print()

print('dodam OS 부팅 완료')
time.sleep(2)
cmd = ""
while cmd != 'end':
    cmd = input(cd + "/")
    
    if cmd == 'dir':
        def list_files_and_dirs():
            items = os.listdir(cd)
            for item in items:
                if os.path.isdir(item):
                    print(item + "/")
                    sub_items = os.listdir(os.path.join(cd, item))
                    for sub_item in sub_items:
                        print("-> " + sub_item)
                else:
                    print(item)
        list_files_and_dirs()

    elif cmd == 'dir+':
        def list_files_and_dirs_with_parent(base_path):
            items = os.listdir(base_path)
            for item in items:
                full_path = os.path.join(base_path, item)
                if os.path.isdir(full_path):
                    print(item + "/")
                    sub_items = os.listdir(full_path)
                    for sub_item in sub_items:
                        print("-> " + sub_item)
                else:
                    print(item)

        print('al')
        list_files_and_dirs_with_parent(cd)  # user 폴더 내용 출력
        list_files_and_dirs_with_parent(os.path.dirname(cd))  # 부모 폴더 내용 출력


    elif cmd.startswith('open-'):
        print('이 작업은 외부 프로그램을 사용하기 때문에 관리자 권한이 필요합니다. 수락 하시겠습니까? (네, 아니요)')
        yesorno = input(':')
        if yesorno == '네':
            file_name = cmd[5:]  # 'open-' 이후의 파일 이름 추출
            full_path = os.path.join(cd, file_name)
            if os.path.isfile(full_path):
                if full_path.endswith('.py'):
                    subprocess.Popen(['cmd.exe', '/c', 'start', 'python', full_path])
                else:
                    subprocess.Popen(['notepad.exe', full_path])
            else:
                print("파일을 찾을 수 없습니다.")
        elif yesorno == '아니요':
            print('작업이 취소되었습니다.')
        else:
            print('작업이 취소되었습니다.')


    elif cmd.startswith('open+'):
        print('이 작업은 부모 폴더인 시스템 폴더까지 표시하기 때문에 dodam dos시스템을 손상시킬수 있습니다. 수락하시겠습니까? (네, 아니요)')
        yesorno=input(':')
        if yesorno=='네':
            print('이 작업은 외부 프로그램을 사용하기 때문에 관리자 권한이 필요합니다. 수락 하시겠습니까? (네, 아니요)')
            yesorno = input(':')
            if yesorno == '네':
                file_name = cmd[5:]  # 'open+' 이후의 파일 이름 추출
                full_path_user = os.path.join(cd, file_name)
                full_path_parent = os.path.join(os.path.dirname(cd), file_name)

                if os.path.isfile(full_path_user):
                    if full_path_user.endswith('.py'):
                        subprocess.Popen(['cmd.exe', '/c', 'start', 'python', full_path_user])
                    else:
                        subprocess.Popen(['notepad.exe', full_path_user])
                elif os.path.isfile(full_path_parent):
                    if full_path_parent.endswith('.py'):
                        subprocess.Popen(['cmd.exe', '/c', 'start', 'python', full_path_parent])
                    elif full_path_user.endswith('.dodamsystempy'):
                        print('이 파일은 터미널로 열수 없지만 어디선가 무언가 들립니다.')
                        time.sleep(2)
                        print(' A A I w  ㄴ ㅐ 까   쩜 려 ㅇ 햿  다,,,')
                    else:
                        subprocess.Popen(['notepad.exe', full_path_parent])
                else:
                    print("파일을 찾을 수 없습니다.")
            elif yesorno == '아니요':
                print('작업이 취소되었습니다.')
            else:
                print('작업이 취소되었습니다.')
        else:
            print('작업이 취소 되었습니다.')


    elif cmd == 'maketextfile':
        file_name = input("파일이름:")
        file_name += '.txt'  # 기본 확장명 .txt 추가
        full_path = os.path.join(cd, file_name)
        content = []
        print("내용을 입력하세요. '끝'을 입력하면 종료됩니다.")
        while True:
            line = input()
            if line == '끝':
                break
            content.append(line)

        # 파일 저장
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(content))

        print(f"'{file_name}' 파일이 '{cd}'에 저장되었습니다.")
    elif cmd.startswith('del-'):
        file_name = cmd[4:]  # 'del-' 이후의 파일 이름 추출
        full_path = os.path.join(cd, file_name)
        if os.path.isfile(full_path):
            os.remove(full_path)  # 파일 삭제
            print(f"'{file_name}' 파일이 삭제되었습니다.")
        else:
            print("파일을 찾을 수 없습니다.")
    elif cmd=='allofasciicode':
        for i in range(0, 0x10FFFF + 1):
            # 서로게이트 영역을 제외
            if not (0xD800 <= i <= 0xDFFF):
                try:
                    print(chr(i))
                except Exception as e:
                    print(f"Error at {i}: {e}")
    elif cmd=='store':
        print('이 앱은 배타 버전이므로, 오류가 있을수 있습니다. 그래도 진행 하시겠습니까? (네 아니요요)')
        yesorno=input(':')
        if yesorno=='네':
            # GitHub 파일 URL
            url = 'https://raw.githubusercontent.com/dodam2015/dy-do-dos-app-Repository/main/app.notepad/notepad.py'

            # 현재 스크립트가 있는 폴더 경로
            current_folder = os.path.dirname(os.path.abspath(__file__))

            # 저장할 파일 경로
            file_name = 'notepad.py'  # 원하는 파일 이름
            file_path = os.path.join(current_folder, file_name)

            # 파일 다운로드
            response = requests.get(url)

            # 요청이 성공했는지 확인
            if response.status_code == 200:
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                print(f"{file_name} 파일이 저장되었습니다.")
            else:
                print("파일 다운로드에 실패했습니다.")
