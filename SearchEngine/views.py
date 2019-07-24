from django.shortcuts import render


def searchView(request):
    context={
        'query': request.POST.get('query'),
        'message':"Hey What are you searching",
    }

    return render(request,'searchtest.html',context)
