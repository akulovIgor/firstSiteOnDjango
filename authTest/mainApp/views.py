from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/home.html')


def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Если есть вопосы, звони, порешаем!', '(937) 755-16-18'
                                                             , 'gototicket@igor.ru']})
