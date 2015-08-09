from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response,redirect
from forms.forms import *
import controller as c
import csv
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from datetime import datetime
from load_matrix.models import File


@login_required(login_url='/accounts/login/')
def upload_file(request):
    try:
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                user = request.user
                title = request.POST['title']
                now = datetime.now()
                f = File(user_name=user,
                         title=title,
                         load_date=now)
                f.save()
                f = File.objects.filter(user_name=user)[0]

                handle_uploaded_file(request.FILES['file'],f)
                T,P = c.Controller.load_file_and_calculate_PCA(f)
                # t,p = c.Controller.get_matrix_T_P(f)

                contex = {
                    'matrix_T': T[:,:2].tolist(),
                    'matrix_P': P[:,:2].tolist(),
                    'rows_T': T.shape[0],
                    'rows_P': P.shape[0],
                    'column_in_row_T': 5,
                    'column_in_row_P': 5
                }
                contex.update(csrf(request))
                user = request.user
                contex['user'] = user
                return render_to_response('plot_and_subsystem.html',contex)

        else:
            form = UploadFileForm()
            contex = {'form': form}
            contex.update(csrf(request))
            user = request.user
            contex['user'] = user
        return render_to_response('load.html', contex)
    except BaseException:
        raise Http404()



def handle_uploaded_file(file,name):
    try:
        file_name = name.__str__()
        with open('files/' + file_name, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
    except BaseException:
        raise Http404()

@login_required(login_url='/accounts/login/')
def download_file(request):
    try:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="PCA.csv"'
        writer = csv.writer(response)
        user = request.user
        f = File.objects.filter(user_name=user)[0]
        T,P = c.Controller.get_matrix_T_P(f)
        row = []
        for i in range(T.shape[1]):
            row.append('PCA'+str(i))
        writer.writerow(row)
        writer.writerows(T.tolist())
        writer.writerow('')
        writer.writerows(P.tolist())
        return response
    except BaseException:
        raise Http404()
