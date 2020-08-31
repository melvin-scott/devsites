from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import CSVFile
from .fileForm import FileForm

import pandas as pd
import numpy as np

# Create your views here.
def csvList(request):
    latest_file_list = CSVFile.objects.all()
    context = {'current_file_list': latest_file_list}
    return render(request, 'csvdata/index.html', context)

def dashboard(request, file_id):    
    # Return the file Details
    fileRep = CSVFile.objects.get(pk=file_id)
    context = {'csvFile': fileRep}

    data = pd.read_csv(fileRep.file_path, iterator=True, chunksize=20000)
    df = pd.concat(data, ignore_index=True)
    df["state"].replace({np.NaN: "BLANK"}, inplace = True) 

    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    listGroups = list(df.groupby([df['date'].dt.year]).groups.keys())
    dfGBCount = df.groupby([df['date'].dt.year]).agg({'count'})[['date']]
    npReport = dfGBCount.to_numpy()

    listReport = npReport.tolist()

    context= {
              'fileid': file_id,
              'filepath': fileRep.file_path,
              'filename': fileRep.file_name,
              'list_data': listReport,
              'list_groups': listGroups,
              }    

    return render(request, 'csvdata/dashboard.html', context)

def CSVView(request, file_id):
    # Return the file Details
    fileRep = CSVFile.objects.get(pk=file_id)
    context = {'csvFile': fileRep}

    data = pd.read_csv(fileRep.file_path, iterator=True, chunksize=20000)
    df = pd.concat(data, ignore_index=True)
    df["state"].replace({np.NaN: "BLANK"}, inplace = True) 
    data_html = df.to_html()

    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    listGroups = list(df.groupby([df['date'].dt.year]).groups.keys())
    dfGBCount = df.groupby([df['date'].dt.year]).agg({'count'})[['date']]
    npReport = dfGBCount.to_numpy()

    listReport = npReport.tolist()

    report_html = dfGBCount.to_html()

    context= {
              'fileid': file_id,
              'filepath': fileRep.file_path,
              'filename': fileRep.file_name,
              'loaded_data': data_html,
              'report_data': report_html,
              'list_data': listReport,
              'list_groups': listGroups,
              }    

    return render(request, 'csvdata/view.html', context)

def upload(request):

    lastfile= CSVFile.objects.last()

    filepath = lastfile.file_path

    filename = lastfile.file_name

    form= FileForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('csvdata:Home'))
    else:
        form = FileForm()
            
    context= {
              'filepath': filepath,
              'form': form,
              'filename': filename,
              }    
      
    return render(request, 'csvdata/upload.html', context)