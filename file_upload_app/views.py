from django.shortcuts import render,HttpResponse

from .forms import MyFileuploadForm
from .models import file_upload

# Create your views here.


def index(request):
    if request.method == "POST":
        c_form=MyFileuploadForm(request.POST,request.FILES)
        if c_form.is_valid():
            name = c_form.cleaned_data['file_name']
            files = c_form.cleaned_data['files']
            file_upload(file_name=name,my_file=files).save()

            return HttpResponse("file upload")
        else:
            return HttpResponse("Error")    
    
    
    else:
        context = {
             'form':MyFileuploadForm()
        }
        return render(request,"index.html",context)

def show_file(request):
    all_data = file_upload.objects.all()
    context={
        'data':all_data
        }
    return render(request,'view.html',context)    
      