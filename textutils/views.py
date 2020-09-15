# I have created this file -- DIPAK
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    params={'about':'This is about me.\nHow are they interesting?'}
    return render(request,'about.html',params)

def contact(request):
    params={'contact':'My gmail:ghtyu@gmail.com\nMy phone:0987655432'}
    return render(request,'contact.html',params)

def analyze(request):
    analyzed=request.POST.get('text','default')
    raw=analyzed.split('\n')
    removepunc=request.POST.get('removepunc','off')
    capitalizefirst = request.POST.get('capitalizefirst', 'off')
    extraspaceremover= request.POST.get('extraspaceremover', 'off')
    if (removepunc == 'off' and extraspaceremover == 'off' and capitalizefirst == 'off'):
        params = {'purpose': 'Nothing!ERROR!', 'analyzed_text': 'something wrong,please try again.'}
        return render(request, 'analyze.html', params)
    if removepunc=='on':
       bl=''
       punctuations='''!@#$%^&*()_'";:,.<>[]{}\|?/'''
       for char in analyzed:
           if char not in punctuations:
              bl+=char
       analyzed=bl

    if extraspaceremover == 'on':
        l=[]
        for d in analyzed.split('\n'):
          dj = ''
          for i in range(len(d)-1):
            if d[i] != ' ':
                dj += d[i]
            elif d[i] == ' ' and d[i + 1] != ' ':
                dj += d[i]
          if d[-1]!='':
              dj+=d[-1]
          dj=list(dj)
          for char in dj:
              if char==' ':
                 dj.remove(char)
              else:
                  break
          dj=''.join(dj)
          l.append(dj)
        analyzed='\n'.join(l)

    if capitalizefirst == 'on':
        l=[]
        for ele in analyzed.split('\n'):
            cap = ele[0].upper() + ele[1:]
            l.append(cap)
        analyzed='\n'.join(l)

    params = {'purpose': '(after analyzing)-', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)



