from django.shortcuts import render

# Create your views here.
def home(request):
    context={
        'user':request.user,
        'toker':'mysecrete'
    }
    return render(request, 'home.html',context=context)