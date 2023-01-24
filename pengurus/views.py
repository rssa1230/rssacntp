from django.shortcuts import render, redirect, HttpResponse
from pengurus.models import Data
from pengurus.forms import FormData
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from pengurus.resource import DataResource

def export_xls(request):
    data = DataResource()
    dataset = data.export()
    response = HttpResponse(dataset.xls, content_type = 'application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="laporan data.xls"'
    return response

@login_required(login_url = settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User berhasil dibuat!")
            return redirect('signup')
        else:
            messages.error(request, "Terjadi kesalahan!")
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form':form,
        }
    return render(request, 'signup.html', konteks)

@login_required(login_url = settings.LOGIN_URL)
def hapus_data(request, id_data):
    data = Data.objects.filter(id=id_data)
    data.delete()

    messages.success(request, "Data berhasil dihapus!")
    return redirect('data')

@login_required(login_url = settings.LOGIN_URL)
def ubah_data(request, id_data):
    data = Data.objects.get(id=id_data)
    template = 'ubah-data.html'
    if request.POST:
        form = FormData(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect('ubah_data', id_data=id_data)
    else:
        form = FormData(instance=data)
        konteks = {
            'form': form,
            'data': data,
        }
        return render(request, template, konteks)

# @login_required(login_url = settings.LOGIN_URL)
def data(request):
        dataa = Data.objects.filter(keterangan__nama='OSIS')

        konteks = {
            'dataa' : dataa,

        }
        return render(request, 'data.html', konteks)

def index(request):
    dataa = Data.objects.filter(keterangan__nama='OSIS')

    konteks={
        'dataa': dataa,
    }
    return render(request, 'index.html', konteks)

def lupa(request):
    
    return render(request, 'lupa.html')

@login_required(login_url = settings.LOGIN_URL)
def tambah_data(request):
    if request.POST:
        form = FormData(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # form = FormData()
            # pesan = "Data berhasil disimpan"

            # konteks = {
            #     'form' : form,
            #     'pesan' : pesan,
            # }
            # return render(request, 'tambah-data.html', konteks)
            return redirect('/data')

    else: 
        form = FormData()

        konteks = {
            'form' : form,
        }

    return render(request, 'tambah-data.html', konteks)

def mpk(request):
        mpkk = Data.objects.filter(keterangan__nama='MPK')

        konteks = {
            'mpkk' : mpkk,

        }
        return render(request, 'mpk.html', konteks)

def indexmpk(request):
    mpkk = Data.objects.filter(keterangan__nama='MPK')
    konteks={
        'mpkk': mpkk,
    }
    return render(request, 'indexmpk.html', konteks)

