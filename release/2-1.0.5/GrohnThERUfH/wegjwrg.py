print('개발자 모드에 들어옴...')
import sys,os
dir_=os.path.dirname(os.path.realpath(__file__)) #dir
print('신분 확인 중...')
try:
    f = open((dir_+'\\'+'systemfile.txt'), "r", encoding="utf-8")
    templist = f.readlines()
    f.close()
    if templist[3]=='developer__True':
        print('developer mode True')
        ifdeveloper=True
    else:
        sys.exit()
except Exception as error:
    ifdeveloper=False
    sys.exit()
if ifdeveloper:
    print('신분이 확인돼었습니다. developer=True')
else:
    print('신분이 ㅎㄱ더ㅗ가 인도 댓ㅈㅂ-ㅏ 못 ㅈㄱ핻습 3덩아 ㅓ')