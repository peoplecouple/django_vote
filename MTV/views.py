from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request): #request에 사용자의 요청정보가 저장
  return render(request, 'MTV/index.html') #render쓸때 꼭 요청정보를 request로 받아와 알맞는 렌더링페이지를 연결)

