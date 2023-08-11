from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<h1>Hello! This is Django Trial</h1> <a href="https://goku.sx/"> Watch Movies for free </a>''')

# def about(request):
#     return HttpResponse("About Django")

def index(request):
    
    #dict={'name':'Aniket', 'place': 'Mumbai'}
    return render(request, 'index.html')
    #return HttpResponse("HOME")

def analyze(request):

    
    #GETTING TEXT
    text = request.GET.get('text1', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremove = request.GET.get('newlineremove', 'off')
    spaceremove = request.GET.get('spaceremove', 'off')
    charcount = request.GET.get('charcount', 'off')
    
    #print(text)
    # print(removepunc)
    # print(fullcaps)

    #ANALYZING TEXT

    if removepunc =="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed =""
        for char in text:
            if char not in punctuations:
                analyzed=analyzed + char
        params = {'purpose':'Remove Punctuations','analyzed_text':analyzed}
        text=analyzed
        #return render(request, 'analyze.html', params)

    if(fullcaps =="on"):
        analyzed=""
        for char in text:
            analyzed = analyzed + char.upper()

        params = {'purpose':'Capitalized Text','analyzed_text':analyzed}
        text=analyzed
        #return render(request, 'analyze.html', params)
        
    if(newlineremove =="on"):
        analyzed=""
        for char in text:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose':'New Line Removed','analyzed_text':analyzed}
        text=analyzed
        #return render(request, 'analyze.html', params)

    if(charcount =="on"):
        #analyzed=""
        for char in text:
                analyzed = +len(text)

        params = {'purpose':'Charcter Count','analyzed_text':analyzed}
        text=analyzed
        #return render(request, 'analyze.html', params)

    if(spaceremove =="on"):
        analyzed=""
        for index, char in enumerate(text):
            if text[index]== " " and text[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose':'Space Removed','analyzed_text':analyzed}
        text=analyzed
    if(removepunc !="on" and fullcaps!="on" and newlineremove!="on" and charcount!="on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)
