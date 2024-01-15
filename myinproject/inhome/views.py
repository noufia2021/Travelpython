from django.shortcuts import render
from django.http import HttpResponse
from . models import Place,Team

# Create your views here.



def home(request):
      obj = Place.objects.all()
      team_obj=Team.objects.all()
      return render(request,"index_new.html",{'result':obj,'res_team':team_obj})

#def about(request):
#    return HttpResponse("Hi this is about page")
#def contact(request):
#    return HttpResponse("Hi this is contact page")
#def details(request):
#    return render(request,"details.html")
#def thanks(request):
#    return render(request,"thanks.html")
#def operation(request):
#    x1=int(request.GET['number1'])
#    x2=int(request.GET['number2'])
#    res1=x1+x2
#    res2=x1-x2
#   res3=x1*x2
#    res4=x1/x2
#    return render(request,"result.html",{'result1':res1,'result2':res2,'result3':res3,'result4':res4})
