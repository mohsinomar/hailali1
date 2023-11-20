from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

cat_choice = (
		('Ammonitrate', 'Ammonitrate'),
		('Sulfat_potasse', 'Sulfat_potasse'),
		('MAP', 'MAP'),
    ('Nitrat_potasse', 'Nitrat_potasse'),
		('Calcium', 'Calcium'),
		('Complet', 'Complet'),
                    ('Acide', 'Acide'),
                    ('Sequestrine', 'Sequestrine'),
                    ('Uree_46', 'Uree_46'),
                    ('Kimia', 'Kimia'),
	)

entree_choice = (
    ('KG', 'KG'),
  	('Litre', 'Litre'),
  	('Sachet', 'Sachet'),
    ('Autre', 'Autre'),
)
class Engrais(models.Model):
          date=models.DateTimeField(auto_now=True,blank=True)
          categorie = models.CharField(max_length=50, blank=True, null=True,choices=cat_choice)                 
          stock=models.CharField(max_length=100, blank=True)
          mesure= models.CharField(max_length=100, blank=True,choices=entree_choice)
          class Meta:
                    abstract = True
          def __str__(self):
                    return self.categorie
          
class Engrais_berhil(Engrais):
          pass

class Engrais_Aoulouz(Engrais):
          pass

class Engrais_Mariem(Engrais):
          pass



#**********************************************************************
catag_choice = (
    ('Karaté', 'Karaté'),
  	('Blouz', 'Blouz'),
  	('AG3', 'AG3'),
    ('Agrale', 'Agrale'),
  	('Coperniko', 'Coperniko'),
  	('Confidor', 'Confidor'),
    ('Valmec', 'Valmec'),
    ('Joker', 'Joker'),
    ('Pixel', 'Pixel'),
    ('Coperide', 'Coperide'),
    ('Mospelan', 'Mospelan'),
    ('Rodo', 'Rodo'),
    ('Fozika', 'Fozika'),
    ('Movento', 'Movento'),
    ('enfidor-speed', 'enfidor-speed'),
    ('Magnome', 'Magnome'),
    ('Samba', 'Samba'),
    ('Fozika_ca', 'Fozika_ca'),
    ('Soufre', 'Soufre'),
    ('Nissorun', 'Nissorun'),
    ('Tridicorp Jaguar', 'Tridicorp Jaguar'),
    ('Twinteck zin+mn', 'Twinteck zin+mn'),
    ('Fengib', 'Fengib'),
    ('Ariatox', 'Ariatox'),
    ('Kimia', 'Kimia'),
    ('Proximo', 'Proximo'),




)
choix = (
    ('Od_berhil', 'Od_berhil'),
  	('Od_drisse', 'Od_drisse'),
  	('Aoulouz', 'Aoulouz'),
    ('Meryem1', 'Meryem1'),
  	('Meryem2', 'Meryem2'),
  	('Plombier', 'Plombier'),
    ('Zbirate', 'Zbirate'),
    ('Raisinier', 'Raisinier'),
    ('Lglidi', 'Lglidi'),
    ('Ben mbarek/jkini/mhijib', 'Ben mbarek/jkini/mhijib'),
    ('Bananier1', 'Bananier1'),
    ('Bananier2', 'Bananier2'),
 

)

group_choix = (
    ('Pesticide', 'Pesticide'),
  	('Fongicide', 'Fongicide'),
  	('Herbicide', 'Herbicide'),
    ('Autre', 'Autre'),)   
class Pesticide(models.Model):          
          date=models.DateTimeField(auto_now=True,blank=True)
          category = models.CharField(max_length=50, blank=True, null=True,choices=catag_choice) 
          groupe=models.CharField(max_length=50, blank=True, null=True,choices=group_choix)                           
          stock=models.CharField(max_length=100, blank=True)
          mesure= models.CharField(max_length=50, blank=True, null=True,choices=entree_choice)
          
          class Meta:
                    abstract = True

          def __str__(self):
                    return self.category
          
class Pesticide_berhil(Pesticide):
          pass
      
class Pesticide_Aoulouz(Pesticide):
          pass
class Pesticide_Mariem(Pesticide):
          pass

#************************************************************************************
    

#**************************************************************************************
class Caisse(models.Model):
          user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
          libelle=models.CharField(max_length=100,blank=True)
          recette=models.CharField(max_length=100,blank=True)
          cumul_recette=models.CharField(max_length=100,blank=True)
          depense=models.CharField(max_length=100,blank=True)
          cumul_depense=models.CharField(max_length=100,blank=True)
          solde=models.CharField(max_length=100,blank=True)                  
          class Meta:
                    abstract = True
          def __str__(self):
                    return self.libelle        
class caisse_berhil(Caisse):
          pass
class caisse_Mariem(Caisse):
          pass

###############################################################
###############################################################

class Achat(models.Model):
          user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
          Date=models.CharField(max_length=50,null=True,blank=True)                   
          desg=models.CharField(max_length=100, blank=False)
          Qté=models.FloatField(default=0)
          pu=models.FloatField(default=0)
          pt=models.FloatField(default= None,null=True,blank=True)
          unite=models.CharField(max_length=50, blank=False, null=True,choices=entree_choice)
          Observation=models.CharField(max_length=50,blank=True)
          class Meta:
                    abstract = True

          def __str__(self):
                    return self.desg
          
          

                 
class Achat_berhil(Achat):
          pass

class Achat_drisse(Achat):
          pass

class Achat_Aoulouz(Achat):
          pass

class Achat_Mariem(Achat):
          pass

class Achat_rgaigue(Achat):
          pass

class Achat_Maryem2(Achat):
               
          pass
class Achat_zbirate(Achat):
               
          pass
class Achat_raisin(Achat):
          pass

class Achat_bananier1(Achat):
          pass

class Achat_bananier2(Achat):
          pass

class Achat_lglidi(Achat):
          pass

class Achat_benmbark(Achat):
          pass

class Achat_murcott(Achat):
          pass
##########################################################
##########################################################





catagoray_choice = (
		('Ouled_berhil', 'Ouled_berhil'),
		('Ouled_drisse', 'Ouled_drisse'),
		('Aoulouz', 'Aoulouz'),
        ('Mariem', 'Mariem'),
		('Maryem2', 'Maryem2'),
        ('Plombier', 'Plombier'),
        ('Zbirate', 'Zbirate'),
        ('Glidi', 'Glidi'),
        ('Ben_mbarek', 'Ben_mbarek'),
        ('Raisin', 'Raisin'),
        ('Bananier1', 'Bananier1'),
        ('Bananier2', 'Bananier2'),

	)
class Article(models.Model):         
          user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
          date=models.CharField(max_length=100, blank=True)
          titre=models.CharField(max_length=50, blank=True, null=True,choices=catagoray_choice)
          description=models.TextField()
          created_at = models.DateTimeField(auto_now_add=True)
          update_at = models.DateTimeField(auto_now=True)
          times = models.DateTimeField(auto_now_add=True, auto_now=False)
          

          def __str__(self):
               return self.titre
          def get_absolute_url(self):
                  return reverse("my_articles")


variete_choice = (
    ('Nules', 'Nules'),
  	('Bruno', 'Bruno'),
    ('Orograndé', 'Orograndé'),
    ('Clémentine','Clémentine'),
  	('Nour', 'Nour'),
    ('Laarache', 'Laarache'),
    ('Nadorcott', 'Nadorcott'),
  	('Navel', 'Navel'),
    ('Maroc_late', 'Maroc_late'),
    ('Salustiana', 'Salustiana'),
    ('Citron', 'Citron'),    
    ('W.sanguine', 'W.sanguine'),
    ('Pomelo', 'Pomelo'),

)

zone_choice=(
  ('Hwara', 'Hwara'),
  	('Od_berhil', 'Od_berhil'),
    ('Aoulouz', 'Aoulouz'),

)
verger_choice = (
    ('436', '436'),
  	('4660', '4660'),
    ('3434', '3434'),
    ('2805','2805'),
  	('2200', '2200'),
    ('2453', '2453'),
    ('1286', '1286'),
  	('2463', '2463'),
    ('774', '774'),
    ('1574', '1574'),
    ('Autre', 'Autre'),  
)

class Mouvement_caisse(models.Model):
            user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
            Date=models.CharField(max_length=50,null=True,blank=True)
            Zone=models.CharField(max_length=50,blank=True, null=True,choices=zone_choice)
            Verger=models.CharField(max_length=50, blank=False, null=True,choices=verger_choice)
            NBR_caisses_Entrée=models.IntegerField(default=0)
            Bon_caisserie=models.CharField(max_length=50,blank=True)
            Véhicule_entré=models.CharField(max_length=50,blank=True)
            NBR_caisses_Sortie=models.IntegerField(default=0)           
            Bon_livraison=models.CharField(max_length=50,blank=True)
            Véhicule_sorti=models.CharField(max_length=50,blank=True)
            Varieté=models.CharField(max_length=50, blank=False,choices=variete_choice)
            Poids=models.IntegerField(default=0)
            Observation=models.CharField(max_length=50,blank=True)
            
        

            def __str__(self):
               return self.Verger

            def get_absolute_url(self):
                        return reverse("cooperative_mabrouka")


               
class Mouvement_436(Mouvement_caisse):
          pass

class Mouvement_4660(Mouvement_caisse):
          pass

class Mouvement_1286(Mouvement_caisse):
          pass

class Mouvement_3434(Mouvement_caisse):
          pass

class Mouvement_2453(Mouvement_caisse):
          pass

class Mouvement_2463(Mouvement_caisse):
               
          pass
class Mouvement_2200(Mouvement_caisse):
               
          pass

class Mouvement_774(Mouvement_caisse):
          pass

class Mouvement_1574(Mouvement_caisse):
          pass
class Mouvement_2805(Mouvement_caisse):
          pass
