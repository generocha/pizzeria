from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
from .models import PizzaType, Pizza

# Create your views here.


def index(request):
    return render(request, 'pizzeria/index.html')


def gettypes(request):
    type_list = PizzaType.objects.all()
    return render(request, 'pizzeria/types.html', {'type_list': type_list})


def getpizzas(request):
    pizzas_list = Pizza.objects.all()
    return render(request, 'pizzeria/pizzas.html', {'pizzas_list': pizzas_list})


def pizzadetails(request, id):
    pizz = get_object_or_404(Pizza, pk=id)
    discount = pizz.memberdiscount
    context = {
        'pizz': pizz,
        'discount': discount,
    }
    return render(request, 'pizzeria/pizzdetails.html', context=context)


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
    return render(request, 'pizzeria/upload.html')
