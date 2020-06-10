from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.
# request: requests와는 다름
def index(request):
    return render(request, 'index.html')

def hello(request):
    menu = ['닭갈비', '탕수육', '초밥', '스파게티돈까스']
    pick = random.choice(menu)

    # render: html에게 변수를 넘겨줄 때 html에서 사용할 수 있게 dictionary 형태로 넘겨준다.
    return render(request, 'hello.html', {'pick':pick})

def name(request):
    my_name = '김현정'
    # 장고가 각 어플리케이션마다 templates 폴더를 찾아서 html을 찾으므로 
    # templates/ 경로를 쓰지 않아도 된다.
    return render(request, 'name.html', {'my_name':my_name})

def introduce(request):
    my_info = ['김현정', '26'] # html에서 리스트의 index로 각각 원소에 접근할 수 없다.
    name = '김현정'
    age = 100
    github = 'https://github.com/sonic247897/django_mysite'
    menu = ['닭갈비', '탕수육', '초밥', '스파게티돈까스']
    pick = random.choice(menu)
    
    # return 코드 길어지지 않게 dictionary 정의해서 그대로 넘겨줌
    context = {
        'name' : name,
        'age' : age,
        'github' : github,
        'pick' : pick
    }
    return render(request, 'introduce.html', context)

def classroom(request):
    members = ['박누리', '곽혜란', '황제윤', '문준우', '이정윤']
    who = random.choice(members)
    # convention
    context = {
        'who' : who
    }
    return render(request, 'classroom.html', context)

# name: URL에서 넘겨주는 변수
def yourname(request, name):
    context = {
        'name' : name
    }
    return render(request, 'yourname.html', context)

def myinfo(request, name, age):
    context = {
        'name' : name,
        'age' : age
    }
    return render(request, 'myinfo.html', context)

def multi(request, num1, num2):
    result = num1*num2
    context = {
        'num1' : num1,
        'num2' : num2,
        'result' : result
    }
    return render(request, 'multi.html', context)

# 구구단을 list에 담아서 list 자체를 출력
def gugu(request, cnt, dan):
    gugudan = []
    # 파이썬에서는 교환하기 쉽게 다음과 같은 표현을 제공한다.
    if cnt > dan :
        cnt, dan = dan, cnt

    for i in range(1, cnt+1):
        gugudan.append(i*dan)
    context = {
        'cnt': cnt,
        "dan" : dan,
        "gugudan" : gugudan
    }
    return render(request, 'gugu.html', context)

def dtl(request):
    my_list = ['짜장면', '차돌짬뽕', '탕수육', '콩국수']
    empty_list = []
    my_string = "Life is short, You need Python"
    today = datetime.now()
    context = {
        'my_list' : my_list,
        'empty_list' : empty_list,
        'my_string' : my_string,
        'today' : today
    }
    return render(request, 'dtl.html', context)

def forif(request, tmp):
    my_list = [100, 50, 30, 20, 10]
    my_string = '간단한 문자열'
    data_a = '첫번째 데이터'
    data_b = '두번째 데이터'
    data_a, data_b = data_b, data_a
    context = {
        'my_list' : my_list,
        'my_string' : my_string,
        'data_a' : data_a,
        'data_b' : data_b,
        'tmp':tmp
    }
    return render(request, 'forif.html', context)