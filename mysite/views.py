# I have created this file- Suraj
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # a = """
    # <button><a href="/about">About</a></button>
    # <button><a href="/gallery">Gallery</a></button>
    # <button><a href="/contact">Contact Us</a></button>
    # <button><a href="/services">Services</a></button>
    #
    # """
    # return HttpResponse(a)
    a={'name':'Suraj','place':'Mumbai'}
    return render(request, "index.html",a)

def about(request):
    a = """
    <h1>About </h1>
    <button><a href="/">Back</a></button>
    """

    return HttpResponse(a)

def gallery(request):
    a = """
    <h1>Gallery</h1>
    <button><a href="/">Back</a></button>
    """

    return HttpResponse(a)

def contact(request):
    a = """
    <h1>8975845685 </h1>
    <button><a href="/">Back</a></button>
    """

    return HttpResponse(a)
def services(request):
    a = """
    <h1> services </h1>
    <button><a href="/">Back</a></button>
    """
    # get the text
    djtext=request.GET.get('text','default')
    print(djtext)
    # analyaze the text
    return HttpResponse(a)

def analyze(request):

    # get the text
    djtext = request.POST.get('text','default')
    #  check the checkbox value
    removepunc = request.POST.get('services', 'off')
    caps = request.POST.get('caps', 'off')
    nlr = request.POST.get('nlr', 'off')
    esr = request.POST.get('esr','off')
    cc = request.POST.get('cc', 'off')
    # check value is on
    if removepunc == "on":
        # analyzed= djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$^&*~_'''
        analyzed= ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed + char + ""

        params = {'purpose':'Remove Punctuation', 'analyzed_text':analyzed}
        djtext = analyzed
    if(caps=="on"):
        analyzed1  = ""
        for char in djtext:
            analyzed1 = analyzed1 + char.upper()
            params = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed1}

        djtext = analyzed1
    if(nlr=="on"):
        analyzed2 = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed2 = analyzed2 + char
                params = {'purpose': 'New Line Remove', 'analyzed_text':analyzed2}
        djtext = analyzed2


    if(esr=="on"):
        analyzed3 = ""
        for index , char in enumerate(djtext):
            if not (djtext[index] ==" " and djtext[index+1]==" "):
                analyzed3 = analyzed3 + char
                params = {'purpose':'Extra Space Remove','analyzed_text':analyzed3}
        djtext = analyzed3


    if (cc=="on"):

        count = (djtext+ "\n Length of statement is :-"+str(len(djtext)))
        params = {'purpose':'Count Characters', 'analyzed_text':count}

    if (removepunc == "off" and caps == "off" and nlr == "off" and esr == "off" and cc == "off"):
        return HttpResponse("Please enable atleast one option.")

    return render(request, 'analyze.html', params)

