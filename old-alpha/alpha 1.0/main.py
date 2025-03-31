import time
from tqdm import tqdm
import curses
import os
import subprocess

cbs = [f for f in os.listdir(os.path.dirname(os.path.abspath(__file__))) if os.path.isfile(f)]

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
    current_directory = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
    cmd = input(current_directory + "/")
    
    if cmd == 'dir':
        def list_files_and_dirs():
            items = os.listdir()
            for item in items:
                if os.path.isdir(item):
                    print(item + "/")
                    for sub_item in os.listdir(item):
                        print("-> " + sub_item)
                else:
                    print(item)
        list_files_and_dirs()

    elif cmd.startswith('open-'):
        print('이 작업은 외부 프로그램을 사용하기 떄문에 관리자 권한이 필요합니다. 수락 하시겠습니까? (네, 아니요)')
        yesorno=input(':')
        if yesorno=='네':
            file_name = cmd[5:]  # 'open ' 이후의 파일 이름 추출
            full_path = os.path.join(current_directory, file_name)
            if os.path.isfile(full_path):
                subprocess.Popen(['cmd.exe', '/c', 'start', 'python', full_path])
            else:
                print("파일을 찾을 수 없습니다.")
        elif yesorno=='아니요':
            print('작업이 취소되었습니다.')
        else:
            print('작업이 취소되었습니다.')

    elif cmd=='maketextfile':
        file_name = input("파일이름: ")
        file_name += '.txt'  # 기본 확장명 .txt 추가
        current_directory = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_directory, file_name)
        content = []
        while True:
            line = input()
            if line == '끝':
                break
            content.append(line)

        # 파일 저장
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(content))

        print(f"'{file_name}' 파일이 저장되었습니다.")
    elif cmd.startswith('del-'):
        file_name = cmd[4:]  # 'delete-' 이후의 파일 이름 추출
        print(file_name)
        full_path = os.path.join(current_directory, file_name)
        if os.path.isfile(full_path):
            os.remove(full_path)  # 파일 삭제
            print(f"'{file_name}' 파일이 삭제되었습니다.")
        else:
            print("파일을 찾을 수 없습니다.")
