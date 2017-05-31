from django.shortcuts import render, HttpResponse

# Create your views here.



def main_view(request):
    return HttpResponse('음 빨리 음 음...')

def main_view2(request):
    return HttpResponse('아침을 안먹어서 배가 고프다....')