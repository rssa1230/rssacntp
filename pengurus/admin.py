from django.contrib import admin
from pengurus.models import *

class DataAdmin(admin.ModelAdmin):
    list_display = ['nis', 'nama', 'jabatan', 'proker']
    search_fields = ['nis', 'nama', 'jabatan', 'proker']
    list_filter = ('keterangan_id', 'kelas_id')
    list_per_page = 4

admin.site.register(Data, DataAdmin)
admin.site.register(Siswa)
admin.site.register(Keterangan)
admin.site.register(Kelas)

