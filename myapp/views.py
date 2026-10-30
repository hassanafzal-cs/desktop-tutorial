from django.shortcuts import render
from .models import Visitor
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def hello(request, name="Dost"):
    if name.lower() == "favicon.ico":
        name ="Dost"
    if request.method == "POST":
        new_name = request.POST.get('username')
        if new_name and new_name.lower() != "favicon.ico":
            Visitor.objects.create(name=new_name)
            name=new_name
    elif name != "Dost" and name.lower() != "favicon.ico":
        Visitor.objects.create(name=name)
    all_visitors = Visitor.objects.all().order_by('-id')[:10]
    return render(request, 'hello.html', {'name':name, 'visitors': all_visitors})