from django.shortcuts import render, redirect
from dashboard.models import UploadedFile

def home(request):
    return render(request, 'dashboard/home.html')

def upload_file(request):
    if request.method == 'POST' and request.FILES.get('excel_file'):
        file = request.FILES['excel_file']
        UploadedFile.objects.create(file=file)
        print(f"File uploaded: {file.name}")
        return redirect('home')
    #return render(request, 'dashboard/upload.html') 
    print(f"NO FILE UPLOADED")
    return render(request, 'dashboard/home.html') 
