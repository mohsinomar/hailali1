from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


admin.site.register(Article)
admin.site.register(Mouvement_caisse)

class OuledberhilAdmin(ImportExportModelAdmin):
          pass

@admin.register(caisse_berhil,caisse_Mariem)
class CaisseAdmin(ImportExportModelAdmin):
          pass

@admin.register(Engrais_berhil,Engrais_Aoulouz,Engrais_Mariem)
class ViewAdmin(ImportExportModelAdmin):
          pass

@admin.register(Pesticide_berhil,Pesticide_Aoulouz,Pesticide_Mariem)
class ViewAdmin(ImportExportModelAdmin):
          
          pass
@admin.register(Achat_berhil,Achat_drisse,Achat_Aoulouz, Achat_Mariem, Achat_rgaigue,Achat_Maryem2,Achat_zbirate,Achat_raisin,Achat_bananier1,Achat_bananier2,Achat_lglidi,Achat_benmbark,Achat_murcott)
class ViewAdmin(ImportExportModelAdmin):
          pass

@admin.register(Mouvement_436,Mouvement_4660,Mouvement_1286, Mouvement_3434, Mouvement_2453,Mouvement_2463,Mouvement_2200,Mouvement_774,Mouvement_1574,Mouvement_2805)
class ViewAdmin(ImportExportModelAdmin):
          pass


