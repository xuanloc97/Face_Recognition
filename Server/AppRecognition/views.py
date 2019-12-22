from django.shortcuts import render
from django.http import HttpResponse ,StreamingHttpResponse

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .test import main
from .train import main_train

def index(request):
    return HttpResponse("Hello")

def simple_upload(request):
    # if request.method == 'POST' and 'button1' in request.POST:
    #     myfile = request.FILES['myfile']
    #     fs = FileSystemStorage()
    #     filename = fs.save(myfile.name, myfile)
    #     uploaded_file_url = fs.url(filename)
    #     return render(request, 'upload/simpleupload.html', {
    #         'uploaded_file_url': uploaded_file_url
    #     })
    if request.method == 'POST' and 'button2' in request.POST:
        main_train()
    if request.method == 'POST' and 'button1' in request.POST:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload/simpleupload.html', {
            'uploaded_file_url': uploaded_file_url
        })

    return render(request, 'upload/simpleupload.html')

def video_feed(request):
    return StreamingHttpResponse(main(), content_type='multipart/x-mixed-replace; boundary=frame')