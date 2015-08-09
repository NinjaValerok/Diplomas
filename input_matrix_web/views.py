from django.shortcuts import render_to_response
from django.template.loader import get_template
from forms.forms import *
from django.core.context_processors import csrf
from PCA_stuff.PCA import calculate_PCA_SVD
from django.http import Http404, HttpResponse
from matrix_view.views import *

def set_sizes(request):
    '''метод POST для отправленных  размеров матрицы'''
    try:
        c = {}
        c.update(csrf(request))
        user = request.user
        c['user'] = user
        error = []
        if request.method == 'GET':
            form = MatrixSizesForm()
            c['form'] = form
            return render_to_response('input_matrix_web/set_sizes_form.html', c)

        form = MatrixSizesForm(request.POST)
        template = 'input_matrix_web/'
        if form.is_valid():
            form = form.cleaned_data
            template += 'input_matrix_form.html'
        else:
            error.append('Data is not valid')
            template += 'input_matrix_web/set_sizes_form.html'
        c['matrix'] = form
        c['errors'] = error
        return render_to_response(template,c)
    except BaseException:
        raise Http404()


def set_matrix(request):
    try:
        columns = 0
        while True:
            id = '_matrix_0_' + str(columns)
            if id in request.POST:
                columns += 1
            else:
                break
        rows = int(len(request.POST.keys())/columns)
        matrix=[]
        for i in range(rows):
            m=[]
            for j in range(columns):
                id = '_matrix_'+ str(i) + '_' + str(j)
                m.append(float(request.POST[id]))
            matrix.append(m)
        T,P = calculate_PCA_SVD(matrix)
        user = request.user
        c = {
            'matrix_T': T[:,:2].tolist(),
            'matrix_P': P[:,:2].tolist(),
            'rows_T': T.shape[0],
            'rows_P': P.shape[0],
            'column_in_row_T': 5,
            'column_in_row_P': 5,
            }

        c['user'] = user
        return render_to_response('plot_and_subsystem.html',c)
    except BaseException:
        raise Http404()


