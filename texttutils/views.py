# Hare Krishna Hare Krishna Krishna Krishna Hare Hare Hare Ramo Hare Ramo Ramo Ramo Hare Hare

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")


def Analyse(request):
    # Get the text
    text = request.POST.get('text','default')

    # Get switch input
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charectercounter = request.POST.get('charectercounter', 'off')

    # remove punctuations
    if removepunc == "on":
        punctuation_list = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analysed=""
        for char in text:
            if char not in punctuation_list:
                analysed = analysed+char

        params = {'Remove':'Remove punctuations', 'analysed_text':analysed}
        text = analysed

    # capitalize
    if capitalize == 'on':
        analysed = ""
        for char in text:
            analysed = analysed+char.upper()
        params = {'cap':'Capitalized', 'analysed_text':analysed}
        text = analysed


    # new line remover
    if newlineremover == 'on':
        analysed = ""
        for char in text:
            if char!="\n" and char!="\r":
                analysed = analysed+char
        params = {'removenewline':'Removed New lines', 'analysed_text':analysed}
        text = analysed

    if extraspaceremover == 'on':
        analysed = ""
        for index,char in enumerate(text):
            if not(text[index]==' ' and text[index+1]==' '):
                analysed = analysed+char

        params = {'removeextraspace':'Removed extra space', 'analysed_text':analysed}
        text = analysed

    if charectercounter == 'on':
        analysed = ""
        i = 0
        for char in text:
            analysed = analysed + char
            i = i+1

        params = {'total':'Total character', 'Total':f'Total {i} characters in this text.','analysed_text':analysed}
    if (removepunc != "on" and capitalize != 'on' and newlineremover != 'on' and extraspaceremover != 'on'and charectercounter != 'on'):
        return HttpResponse("Please select a action.")


    return render(request, 'analyse.html', params)






