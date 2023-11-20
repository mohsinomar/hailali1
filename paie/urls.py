from django.urls import re_path
from . views import *
from app_admin.views import export_Article
urlpatterns=[
          re_path(r'^$',home,name='home'),
          
          re_path(r'^detail/(?P<pk>\d+)$',detail,name='detail'),
          re_path(r'^add-pub$',AddArticle.as_view(),name='add-pub'),
          re_path(r'^index$',index,name='index'),
          
          re_path(r'^caisse$',caisse,name='caisse'),                   
          re_path(r'^display1$',display1,name='display1'),
          re_path(r'^display2$',display2,name='display2'),
          re_path(r'^display3$',display3,name='display3'),
          re_path(r'^display4$',display4,name='display4'),
          re_path(r'^display5$',display5,name='display5'),
          re_path(r'^display6$',display6,name='display6'),
          re_path(r'^display7$',display7,name='display7'),
          re_path(r'^display8$',display8,name='display8'),
          re_path(r'^display9$',display9,name='display9'),
          re_path(r'^displayban2$',displayban2,name='displayban2'),
          re_path(r'^displayzbi$',displayzbi,name='displayzbi'),
          re_path(r'^displaymar$',displaymar,name='displaymar'),          
          re_path(r'^display22$',display22,name='display22'),
          re_path(r'^display33$',display33,name='display33'),
          re_path(r'^displaymurcott$',displaymurcott,name='displaymurcott'),          
          re_path(r'^delete_desktop1/(?P<pk>\d+)$',delete_desktop1,name='delete_desktop1'),
          re_path(r'^delete_laptop1/(?P<pk>\d+)$',delete_laptop1,name='delete_laptop1'),
          re_path(r'^delete_mobile1/(?P<pk>\d+)$',delete_mobile1,name='delete_mobile1'),
          #######################################################
          re_path(r'^caisse1$',caisse1,name='caisse1'),
          
          re_path(r'^caisse4$',caisse4,name='caisse4'),
          
          #####################################################
         
          re_path(r'^ajouter-employé11$',add_desktop1.as_view(),name='ajouter-employé11'),
          re_path(r'^ajouter-employé22$',add_laptop1.as_view(),name='ajouter-employé22'),
          re_path(r'^ajouter-employé33$',add_mobile1.as_view(),name='ajouter-employé33'),
          re_path(r'^ajouter-employé44$',add_Mariema.as_view(),name='ajouter-employé44'),
          re_path(r'^ajouter-employé55$',add_Rgaiguea.as_view(),name='ajouter-employé55'),
          re_path(r'^ajouter-employé66$',add_Lglidi.as_view(),name='ajouter-employé66'),
          re_path(r'^ajouter-employé77$',add_Benmbark.as_view(),name='ajouter-employé77'),
          re_path(r'^ajouter-employé88$',add_Raisin.as_view(),name='ajouter-employé88'),
          re_path(r'^ajouter-employé99$',add_Banan1.as_view(),name='ajouter-employé99'),
          re_path(r'^ajouter-entré_to_bananier2$',add_Banan2.as_view(),name='ajouter-entré_to_bananier2'),
          re_path(r'^ajouter-entré_to_zbirate$',add_Zbirate.as_view(),name='ajouter-entré_to_zbirate'),
          re_path(r'^ajouter-entré_to_meriem2$',add_Mariem2.as_view(),name='ajouter-entré_to_meriem2'),
          re_path(r'^ajouter-entré_to_murcott$',add_Murcott.as_view(),name='ajouter-entré_to_murcott'),

          re_path(r'^modifier--depense436/(?P<pk>\d+)$',Achat_berhil436.as_view(),name='modifier--depense436'),         
          re_path(r'^modifier--depense4660/(?P<pk>\d+)$',Achat_drisse4660.as_view(),name='modifier--depense4660'),
          re_path(r'^modifier--depense1286/(?P<pk>\d+)$',Achat_aoulouz1286.as_view(),name='modifier--depense1286'),                  
          re_path(r'^modifier-depense3434/(?P<pk>\d+)$',Achat_mariem3434.as_view(),name='modifier-depense3434'),
          re_path(r'^modifier-depense2200/(?P<pk>\d+)$',Achat_rgauiegue.as_view(),name='modifier-depense2200'),          
          re_path(r'^modifier-depense2453/(?P<pk>\d+)$',Achat_mariem1.as_view(),name='modifier-depense2453'),
          re_path(r'^modifier-depense2805/(?P<pk>\d+)$',Achat_banane1.as_view(),name='modifier-depense2805'),          
          re_path(r'^modifier--depense774/(?P<pk>\d+)$',Achat_banane2.as_view(),name='modifier--depense774'),
          re_path(r'^modifier--depense2463/(?P<pk>\d+)$',Achat_lglidi1.as_view(),name='modifier--depense2463'),
          re_path(r'^modifier--depense1574/(?P<pk>\d+)$',Achat_bnmbark1.as_view(),name='modifier--depense1574'),
          re_path(r'^modifier--depenseRais/(?P<pk>\d+)$',Achat_raisin1.as_view(),name='modifier--depenseRais'),
          re_path(r'^modifier--depense_murcott/(?P<pk>\d+)$',Achat_murcot1.as_view(),name='modifier--depense_murcott'),
          re_path(r'^modifier--depensezbirate/(?P<pk>\d+)$',Achat_zbirate1.as_view(),name='modifier--depensezbirate'),

          re_path(r'^supprimer--depense436/(?P<pk>\d+)$',deletion_berhil.as_view(),name='supprimer--depense436'),         
          re_path(r'^supprimer--depense4660/(?P<pk>\d+)$',deletion_drisse.as_view(),name='supprimer--depense4660'),
          re_path(r'^supprimer--depense1286/(?P<pk>\d+)$',deletion_aoulouz.as_view(),name='supprimer--depense1286'),                  
          re_path(r'^supprimer-depense3434/(?P<pk>\d+)$',deletion_mariem3434.as_view(),name='supprimer-depense3434'),
          re_path(r'^supprimer-depense2200/(?P<pk>\d+)$',deletion_rgauiegue.as_view(),name='supprimer-depense2200'),          
          re_path(r'^supprimer-depense2453/(?P<pk>\d+)$',deletion_maryem2.as_view(),name='supprimer-depense2453'),
          re_path(r'^supprimer-depense2805/(?P<pk>\d+)$',deletion_banane1.as_view(),name='supprimer-depense2805'),          
          re_path(r'^supprimer--depense774/(?P<pk>\d+)$',deletion_banane2.as_view(),name='supprimer--depense774'),
          re_path(r'^supprimer--depense2463/(?P<pk>\d+)$',deletion_lglidi.as_view(),name='supprimer--depense2463'),
          re_path(r'^supprimer--depense1574/(?P<pk>\d+)$',deletion_benmbark.as_view(),name='supprimer--depense1574'),
          re_path(r'^supprimer--depenseRais/(?P<pk>\d+)$',deletion_raisin.as_view(),name='supprimer--depenseRais'),
          re_path(r'^supprimer--depensezbirate/(?P<pk>\d+)$',deletion_zbirate.as_view(),name='supprimer--depensezbirate'),
          re_path(r'^supprimer--depense_murcott/(?P<pk>\d+)$',deletion_murcott.as_view(),name='supprimer--depense_murcott'),

          



          re_path(r'^edit_mobile1/(?P<pk>\d+)$',edit_mobile1,name='edit_mobile1'),
          
          re_path(r'^export_436$',export_436,name='export_436'),
          re_path(r'^export_3434$',export_3434,name='export_3434'),
          re_path(r'^export_4660$',export_4660,name='export_4660'),
          re_path(r'^export_2453$',export_2453,name='export_2453'),
          re_path(r'^export_2200$',export_2200,name='export_2200'),
         
          
          re_path(r'^export_mobile111$',export_excel111,name='export_mobile111'),
          re_path(r'^export_mobile222$',export_excel222,name='export_mobile222'),
          re_path(r'^export_mobile333$',export_excel333,name='export_mobile333'),
          re_path(r'^export_mobile444$',export_excel444,name='export_mobile444'),
          re_path(r'^export_mobile555$',export_excel555,name='export_mobile555'),
          re_path(r'^export_Article$',export_Article,name='export_Article'),
          
          re_path(r'^export_mobile1111$',export_excel1111,name='export_mobile1111'),
          
          re_path(r'^export_mobile3333$',export_excel3333,name='export_mobile3333'),
          re_path(r'^export_mobile4444$',export_excel4444,name='export_mobile4444'),
          
          re_path(r'^export_mobile11$',export_excel11,name='export_mobile11'),
          
          re_path(r'^export_mobile33$',export_excel33,name='export_mobile33'),
           re_path(r'^export_mobile44$',export_excel44,name='export_mobile44'),
          


          
          re_path(r'^export_achatgli$',export_achatgli,name='export_achatgli'),
          
          re_path(r'^export_achatbenm$',export_achatbenm,name='export_achatbenm'),
          
          re_path(r'^export_achatzbi$',export_achatzbi,name='export_achatzbi'),
          
          re_path(r'^export_achatmer$',export_achatmer,name='export_achatmer'),
          
          re_path(r'^export_achatban1$',export_achatban1,name='export_achatban1'),
          
          re_path(r'^export_achatban2$',export_achatban2,name='export_achatban2'),
          
          re_path(r'^export_achatrais$',export_achatrais,name='export_achatrais'),


          re_path(r'^export_caisse1$',export_caisse1,name='export_caisse1'),
          
          re_path(r'^export_caisse4$',export_caisse4,name='export_caisse4'),
          


          re_path(r'^affiche$',affiche,name='affiche'),


          re_path(r'^engrais$',engrais,name='engrais'),
          re_path(r'^display111$',display111,name='display111'),
          re_path(r'^ajouter-produits_berhil$',engrais_berhil436.as_view(),name='ajouter-produits_berhil'),
          re_path(r'^edit-etat-stock-berhil/(?P<pk>\d+)$',modifengrais436.as_view(),name='edit-etat-stock-berhil'),
          re_path(r'^supprimer-produits_berhil/(?P<pk>\d+)$',deletionengrais436.as_view(),name='supprimer-produits_berhil'),
          re_path(r'^display333$',display333,name='display333'),
          re_path(r'^ajouter-produits_aoulouz$',engrais_aoulouz1286.as_view(),name='ajouter-produits_aoulouz'),
          re_path(r'^edit-etat-stock-aoulouz/(?P<pk>\d+)$',modifengrais1286.as_view(),name='edit-etat-stock-aoulouz'),
          re_path(r'^supprimer-produits_aoulouz/(?P<pk>\d+)$',deletionengrais1286.as_view(),name='supprimer-produits_aoulouz'),
          re_path(r'^display444$',display444,name='display444'),
          re_path(r'^ajouter-produits_hwara$',engrais_hwara3434.as_view(),name='ajouter-produits_hwara'),
          re_path(r'^edit-etat-stock-hwara/(?P<pk>\d+)$',modifengrais3434.as_view(),name='edit-etat-stock-hwara'),
          re_path(r'^supprimer-produits_hwara/(?P<pk>\d+)$',deletionengrais3434.as_view(),name='supprimer-produits_hwara'),
          re_path(r'^ajouter-employé111$',add_desktop111,name='ajouter-employé111'),
          
          re_path(r'^ajouter-employé333$',add_mobile111,name='ajouter-employé333'),
        


          re_path(r'^pesticide$',pesticide,name='pesticide'),
          re_path(r'^display1111$',display1111,name='display1111'),
          re_path(r'^ajouter-pesticide_berhil$',pestice_berhil436.as_view(),name='ajouter-pesticide_berhil'),
          re_path(r'^edit-etat-pesticide-berhil/(?P<pk>\d+)$',modifpestice436.as_view(),name='edit-etat-pesticide-berhil'),
          re_path(r'^supprimer-pesticide_berhil/(?P<pk>\d+)$',deletionpestice436.as_view(),name='supprimer-pesticide_berhil'),

          re_path(r'^display3333$',display3333,name='display3333'),
          re_path(r'^ajouter-pesticide_aoulouz$',pestice_aoulouz1286.as_view(),name='ajouter-pesticide_aoulouz'),
          re_path(r'^edit-etat-pesticide-aoulouz/(?P<pk>\d+)$',modifpestice1286.as_view(),name='edit-etat-pesticide-aoulouz'),
          re_path(r'^supprimer-pesticide_aoulouz/(?P<pk>\d+)$',deletionpestice1286.as_view(),name='supprimer-pesticide_aoulouz'),

          re_path(r'^display4444$',display4444,name='display4444'),
          re_path(r'^ajouter-pesticide_hwara$',pestice_hwara3434.as_view(),name='ajouter-pesticide_hwara'),
          re_path(r'^edit-etat-pesticide-hwara/(?P<pk>\d+)$',modifpestice3434.as_view(),name='edit-etat-pesticide-hwara'),
          re_path(r'^supprimer-pesticide_hwara/(?P<pk>\d+)$',deletionpestice3434.as_view(),name='supprimer-pesticide_hwara'),
         


          re_path(r'^cooperative_mabrouka$',Mabrouka,name='cooperative_mabrouka'),
          re_path(r'^tous_domaines_hailali$',Domaines,name='tous_domaines_hailali'),
          
          re_path(r'^mouvement-des-caisses-cuillette_436$',mbrouka436,name='mouvement-des-caisses-cuillette_436'),
          re_path(r'^mouvement-des-caisses-cuillette_4660$',mbrouka4660,name='mouvement-des-caisses-cuillette_4660'),
          re_path(r'^mouvement-des-caisses-cuillette_774$',mbrouka774,name='mouvement-des-caisses-cuillette_774'),
          re_path(r'^mouvement-des-caisses-cuillette_2200$',mbrouka2200,name='mouvement-des-caisses-cuillette_2200'),
          re_path(r'^mouvement-des-caisses-cuillette_3434$',mbrouka3434,name='mouvement-des-caisses-cuillette_3434'),
          re_path(r'^mouvement-des-caisses-cuillette_2805$',mbrouka2805,name='mouvement-des-caisses-cuillette_2805'),
          re_path(r'^mouvement-des-caisses-cuillette_1574$',mbrouka1574,name='mouvement-des-caisses-cuillette_1574'),
          re_path(r'^mouvement-des-caisses-cuillette_2463$',mbrouka2463,name='mouvement-des-caisses-cuillette_2463'),
          re_path(r'^mouvement-des-caisses-cuillette_2453$',mbrouka2453,name='mouvement-des-caisses-cuillette_2453'),
          re_path(r'^mouvement-des-caisses-cuillette_1286$',mbrouka1286,name='mouvement-des-caisses-cuillette_1286'),
          re_path(r'^ajouter-mouvement436$',mouvement436.as_view(),name='ajouter-mouvement436'),
          re_path(r'^ajouter-mouvement4660$',mouvement4660.as_view(),name='ajouter-mouvement4660'),
          re_path(r'^ajouter-mouvement3434$',mouvement3434.as_view(),name='ajouter-mouvement3434'),
          re_path(r'^ajouter-mouvement2200$',mouvement2200.as_view(),name='ajouter-mouvement2200'),
          re_path(r'^ajouter-mouvement1286$',mouvement1286.as_view(),name='ajouter-mouvement1286'),
          re_path(r'^ajouter-mouvement2453$',mouvement2453.as_view(),name='ajouter-mouvement2453'),
          re_path(r'^ajouter-mouvement2805$',mouvement2805.as_view(),name='ajouter-mouvement2805'),
          re_path(r'^ajouter-mouvement774$',mouvement774.as_view(),name='ajouter-mouvement774'),
          re_path(r'^ajouter-mouvement2463$',mouvement2463.as_view(),name='ajouter-mouvement2463'),
          re_path(r'^ajouter-mouvement1574$',mouvement1574.as_view(),name='ajouter-mouvement1574'),
          re_path(r'^modifier--situation436/(?P<pk>\d+)$',modification436.as_view(),name='modifier--situation436'),
          re_path(r'^modifier--situation4660/(?P<pk>\d+)$',modification4660.as_view(),name='modifier--situation4660'),
          re_path(r'^modifier--situation1286/(?P<pk>\d+)$',modification1286.as_view(),name='modifier--situation1286'),
          re_path(r'^modifier--situation774/(?P<pk>\d+)$',modification774.as_view(),name='modifier--situation774'),
          re_path(r'^modifier--situation2463/(?P<pk>\d+)$',modification2463.as_view(),name='modifier--situation2463'),
          re_path(r'^modifier--situation1574/(?P<pk>\d+)$',modification1574.as_view(),name='modifier--situation1574'),        
          re_path(r'^modifier-situation3434/(?P<pk>\d+)$',modification3434.as_view(),name='modifier-situation3434'),
          re_path(r'^modifier-situation2200/(?P<pk>\d+)$',modification2200.as_view(),name='modifier-situation2200'),          
          re_path(r'^modifier-situation2453/(?P<pk>\d+)$',modification2453.as_view(),name='modifier-situation2453'),
          re_path(r'^modifier-situation2805/(?P<pk>\d+)$',modification2805.as_view(),name='modifier-situation2805'),          
          
          re_path(r'^supprimer--situation436/(?P<pk>\d+)$',deletion436.as_view(),name='supprimer--situation436'),
          re_path(r'^supprimer--situation4660/(?P<pk>\d+)$',deletion4660.as_view(),name='supprimer--situation4660'),
          re_path(r'^supprimer--situation774/(?P<pk>\d+)$',deletion774.as_view(),name='supprimer--situation774'),
          re_path(r'^supprimer--situation2463/(?P<pk>\d+)$',deletion2463.as_view(),name='supprimer--situation2463'),
          re_path(r'^supprimer--situation1574/(?P<pk>\d+)$',deletion1574.as_view(),name='supprimer--situation1574'),
          re_path(r'^supprimer--situation1286/(?P<pk>\d+)$',deletion1286.as_view(),name='supprimer--situation1286'),
          re_path(r'^supprimer-situation3434/(?P<pk>\d+)$',deletion3434.as_view(),name='supprimer-situation3434'),
          re_path(r'^supprimer-situation2200/(?P<pk>\d+)$',deletion2200.as_view(),name='supprimer-situation2200'),          
          re_path(r'^supprimer-situation2453/(?P<pk>\d+)$',deletion2453.as_view(),name='supprimer-situation2453'),
          re_path(r'^supprimer-situation2805/(?P<pk>\d+)$',deletion2805.as_view(),name='supprimer-situation2805'),
          
     
]
