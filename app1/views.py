from django.shortcuts import render

# Create your views here.
def fun1(request):
    data='This is Pavi'
    d={'dataa':data,'newdata':'Hey I\'came recently'}
    return render(request,'myfile.html',context=d)
