#dpy.py
import tkinter as tk
from tkinter import messagebox
import os,subprocess

def iseven(a):
    try:
        if a%2==0:
            return True
        elif a%3==0:
            return False
        else:
            return 'error'
    except Exception as error:
        return 'error:',error

def plus(*a):
    cnt=0
    try:
        for i in range(0,len(a)):
            cnt+=a[i]
        return cnt
    except Exception as error:
        return 'error:',error
def ispalindrome(a):
    try:
        if a==a[::-1]:
            return True
        else:
            return False
    except Exception as error:
        return 'error', error
def gugudan(a):
    try:
        for i in range(1,9):
            print(a,'*',i,'=',a*i)
    except Exception as error:
        return 'error', error
def pw(a):
    a=0
    pp=0
    for i in range(0,len(a)):
        a=chr(a[i])
        pp=ord((ord(a)+534))
def isvowel(a):
    vowel_set={'a','e','i','o','u'}
    cnt=0
    for c in a:
        if c in vowel_set:
            cnt+=1
    return cnt
def file_read_all(file_name):
    dir_=os.path.dirname(os.path.realpath(__file__)) #dir
    f = open((dir_+'\\'+file_name), "r", encoding="utf-8")
    data = f.read()
    print(data)
    f.close()
def isvar(a):
    if a in locals():
        print(f'{a} 변수는 존재합니다.')
    else:
        print(f'{a} 변수는 존재하지 않습니다.')
def runthis(a):
    subprocess.run(["python", a])  # Python 3