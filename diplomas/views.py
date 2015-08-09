import csv
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from load_matrix.models import File
import controller as c
import os
__author__ = 'ninjavalerok'


def start_view(request):
    contex = {}
    contex.update(csrf(request))
    user = request.user
    contex['user'] = user
    return render_to_response('start_view.html',contex)

@login_required(login_url='/accounts/login/')
def profile(request):
    try:
        contex = {}
        user = request.user
        contex['user'] = user
        files = File.objects.filter(user_name=user)
        contex['files'] = files
        return render_to_response('registration/profile.html', contex)
    except BaseException:
        raise Http404()


@login_required(login_url='/accounts/login/')
def download_PCA_file_by_id(request, id):
    try:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="PCA.csv"'
        writer = csv.writer(response)
        id = int(id)
        f = File.objects.get(id=id)
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

@login_required(login_url='/accounts/login/')
def delete_file_by_id(request, id):
    try:
        id = int(id)
        f = File.objects.get(id=id)
        files = []

        files.append('files/'+ f.__str__())
        files.append('files/'+ f.get_name_PCA_file_T())
        files.append('files/'+ f.get_name_PCA_file_P())
        for file in files:
            os.remove(file)
        f.delete()
        return redirect('/accounts/profile/')
    except BaseException:
        raise Http404()