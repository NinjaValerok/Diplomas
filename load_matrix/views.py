from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render_to_response
from forms.forms import *



@csrf_protect
@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse('ok')
    else:
        form = UploadFileForm()
    return render_to_response('load.html', {'form': form})



def handle_uploaded_file(f):
    with open('files/' + f.__str__(), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def set_subsystem(request):
    sizes = {'number_rows': 3, 'number_column': 5}
    return render_to_response('test.html',locals())
