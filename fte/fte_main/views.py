#from django.http import HttpResponse
#from fte_main.forms import FTEMainForm
from django.shortcuts import render

from fte_main.converter import Convert_fasta_header

def index(request):
    if request.method == 'POST':

        #form = FTEMainForm(request.POST, request.FILES)
        #if form.is_valid():
        #    custom_label = form.cleaned_data['custom_label']
        #    x = request.FILES['infile']
            #print custom_label, x
        #print request

        ct = request.POST["ct"]
        x = request.FILES['exampleInputFile']
        c = Convert_fasta_header(x,'out.txt', ct)
        c.conv_gsp()
        print "1"
        return render(request, 'index_result.html', {'a':2})

    else:
        print "2"
        form = FTEMainForm()
    #return render(request, 'fte_init.html', {'a':2, 'form':form})
    #return render(request, 'index.html', {'a':2, 'form':form})
    print "3"
    return render(request, 'index.html', {'a':2})
    
