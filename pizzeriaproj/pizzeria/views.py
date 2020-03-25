from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.


def index(request):
    return render(request, 'pizzeria/index.html')


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
    return render(request, 'pizzeria/upload.html')
