from import_export import resources
from pengurus.models import Data
from import_export.fields import Field

class DataResource(resources.ModelResource):
    kelas_id__kelas = Field(attribute='kelas_id', column_name='kelas')
    keterangan_id__nama = Field(attribute='keterangan_id', column_name='keterangan')


    class Meta:
        model = Data
        fields = ['tanggal', 'nis', 'nama', 'kelas_id__nama', 'keterangan_id_nama', 'jabatan', 'proker']
        export_order = ['tanggal', 'nis', 'nama', 'kelas_id__nama', 'keterangan_id__nama', 'jabatan', 'proker']