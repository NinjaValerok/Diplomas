from django.http import Http404
from django.template.loader import get_template
from django.template import Context
from PCA_stuff.PCA import *

#это не представление. Это функция возвращающаяя матрицы T и P в виде html

def present_matrix_as_html(T,P):
    try:
        matrix_dict = {
            'Scores (T)': T,
            'Loadings (P)': P,
        }
        html = ''
        t = get_template('matrix.html')
        for key in sorted(matrix_dict):
            c = Context({
                'matrix': matrix_dict[key],
                'matrix_name': key,
            })
            html += t.render(c)
        return html
    except BaseException:
        raise Http404()