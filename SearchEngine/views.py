from django.shortcuts import render
from django.shortcuts import redirect
from .models import Search, FeedbackMessage
from AnalysisEngine.models import Analysis
from PredictionEngine.models import Predictions


def searchView(request):
    query=request.GET.get('query')

    # w = (Q(summary__icontains=query)|Q(body__icontains=query))
    w=Analysis.objects.filter(body__icontains=query)
    q=Predictions.objects.filter(body__icontains=query)
    print(w)
    context={
        'y':w,
        'z':q,
    }
    return render(request,'searchtest.html',context)

def feedbackView(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    message=request.POST.get('message')
    obj = FeedbackMessage.objects.create(Name=name, Email=email, Message=message)
    obj.save()

    context={
        'name':name,
        'email':email,    
        'message':message,
    }
    return render(request,'feedback.html',context)