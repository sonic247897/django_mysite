"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages import views 

# list -> 쉼표로 분리/ path함수 이용해서 주소 정의
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index), 
    # URL, 함수(함수명만 넘겨준다는 것=> 바로 실행하지 않고 함수명을 넘겨주면 내부에서 처리)
    path('hello/', views.hello),
    path('name/', views.name),
    path('introduce/', views.introduce),
    path('classroom/', views.classroom),
    # 숫자만 허용하려면 int:name 으로 (예외를 입력하면 주소 자체가 없는 것으로 뜬다)
    path('yourname/<str:name>/', views.yourname),
    path('myinfo/<str:name>/<int:age>/', views.myinfo),
    path('multi/<int:num1>/<int:num2>/', views.multi),
    path('gugu/<int:cnt>/<int:dan>/', views.gugu),
    path('dtl/', views.dtl),
    path('forif/<str:tmp>/', views.forif)
]
