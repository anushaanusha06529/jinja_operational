from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'name':'Anusha','age':22}
    return render(request,'conditions.html',context=d)