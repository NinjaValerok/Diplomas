from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.template.loader import get_template
from django.template import Context
from PCA_stuff.PCA import *
from forms.forms import *

@csrf_protect
@csrf_exempt
def set_sizes(request):
    '''метод POST для отправленных  размеров матрицы'''

    error = []
    if request.method == 'GET':
        form = MatrixSizesForm()
        return render_to_response('input_matrix_web/set_sizes_form.html', {'form': form},)

    form = MatrixSizesForm(request.POST)
    template = 'input_matrix_web/'
    if form.is_valid():
        form = form.cleaned_data
        template += 'input_matrix_form.html'
    else:
        error.append('Data is not valid')
        template += 'set_sizes_form.html'

    return render_to_response(template, {'matrix': form, 'errors': error },)



@csrf_protect
@csrf_exempt
def set_matrix(request):
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
            m.append(int(request.POST[id]))
        matrix.append(m)
    T,P,R = calculate_PCA_SVD(matrix)
    matrix_dict = {
        'Source': matrix,
        'Scores (T)': T,
        'Loadings (P)': P,
    }
    html = ''
    t = get_template('input_matrix_web/matrix.html')
    for key in sorted(matrix_dict):
        c = Context({
            'matrix': matrix_dict[key],
            'matrix_name': key,
        })
        html += t.render(c)

    return HttpResponse(html)





def test(request):
    name = 'valera'
    return render_to_response('test.html',locals())