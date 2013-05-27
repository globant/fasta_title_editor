from django.http import HttpResponse
from fte_main.forms import FTEMainForm
from django.shortcuts import render, redirect

from fte_main.converter import Convert_fasta_header

def index(request):
    if request.method == 'POST':
        form = FTEMainForm(request.POST, request.FILES)
        if form.is_valid():
            custom_label = form.cleaned_data['custom_label']
            x = request.FILES['infile']
            #print custom_label, x
            c = Convert_fasta_header(x,'out.txt', custom_label)
            c.conv_gsp()
    else:
        form = FTEMainForm()
    #return render(request, 'fte_init.html', {'a':2, 'form':form})
    return render(request, 'index.html', {'a':2, 'form':form})
