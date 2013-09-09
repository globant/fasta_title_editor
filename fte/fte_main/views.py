from django.http import HttpResponse
from tempfile import NamedTemporaryFile, mkstemp

from fte_main.forms import FTEMainForm
from django.shortcuts import render

from fte_main.converter import Convert_fasta_header

from django.conf import settings
import os


def index(request):
    if request.method == 'POST':
        form = FTEMainForm(request.POST, request.FILES)
        if form.is_valid():
            custom_label = form.cleaned_data['custom_label']
            tmpfile = NamedTemporaryFile(prefix='tmp', 
                                         dir=settings.TMP_DIR, 
                                         delete=False)
            tmpfile_name = tmpfile.name
            x = request.FILES['infile']
            c = Convert_fasta_header(x, tmpfile_name, custom_label)
            c.conv_gsp()
            f_name = os.path.split(tmpfile.name)[1]
            t_name = settings.TMP_DIR + f_name
            d = {'t_name':t_name, 'f_name':f_name}
        return render(request, 'index_result.html', d)

    else:
        form = FTEMainForm()
    return render(request, 'index.html', {'a':2})
    
def downloadstatic(request, download_file=''):
    f = os.path.join(settings.PROJECT_ROOT, 
                     'fte/fte_main/outfiles/',
                     download_file)
    response = HttpResponse(open(f).read(), 
                            content_type="text/plain")
    return response


