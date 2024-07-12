from django.shortcuts import render, redirect

def counter(request):
    if request.method =='POST':
        text = request.POST['texttocount']
        if text != '':
            word = len(text.split())
            i = True
            redirect('counter')
            return render(request, 'counter.html',
                          {'word':word,
                           'text':text,
                           'i':i,
                           'on':'active'})

        else:
            redirect('counter')
            return render(request, 'counter.html', {'on':'active'})
    else:
        redirect('counter')
        return render(request, 'counter.html', {'on':'activ'})
