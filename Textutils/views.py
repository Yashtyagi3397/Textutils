
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
   
    return render(request, 'index2.html')
def analyze(request):
    djtext= request.POST.get('text', 'default')
    removepunc= request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    print(removepunc)
    print(djtext)

    if removepunc=="on":
        analyzed=""
        punctuation= '''!@#$%^&*()_+{}:"<>?|\][';.,/~'''
        for char in djtext:
            if char not in punctuation:
                analyzed=analyzed+char

        params={'purpose':'remove punctuation' ,'analyzed_text':analyzed}
        djtext= analyzed
    
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+ char.upper()
        params={'purpose':'Change to upercase' ,'analyzed_text':analyzed}
        djtext=analyzed

    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char != "\n" and char!= "\r":
                analyzed=analyzed+char
        params={'purpose':'Change to upercase' ,'analyzed_text':analyzed}
        djtext=analyzed

    if extraspaceremover=="on":
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params={'purpose':'Remove extra spaces' ,'analyzed_text':analyzed}
        djtext=analyzed
       
    if charcounter=="on":
        analyzed=""
        i=0
        for char in djtext:
            i=i+1
        params={'purpose':'Character counter' ,'analyzed_text': i}
        djtext=analyzed

    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and charcounter!="on"):
        return HttpResponse("Please select any operation and try again")
    
    return render(request, 'analyze2.html', params)
    

    


