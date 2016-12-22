from django.shortcuts import render

def aloha_python(request):
    return render(request, 'exciting_message/exciting_message.html', {})