
from django import forms
from .models import *






class ArticleForm(forms.ModelForm):
              class Meta:
                    model = Article
                    fields = ['date','titre',  'description']
                    labels = {'date':'Date','titre': 'Domaine','description': 'Description'}
                    widgets = {
                     'date': forms.TextInput(attrs={'class': 'form-control mt-20'}),
                     'titre': forms.Select(attrs={'class': 'form-control'}),
                     'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),

                       }








class DesktopFormo(forms.ModelForm):
          class Meta:
              model = Achat_berhil
              fields =('Date','desg', 'Qté','unite', 'pu', 'Observation')
              labels = {'Date':'Date','desg': 'Désignation','Qté': 'Quntité','pu': 'Prix unitaire'}
              

class LaptopFormo(forms.ModelForm):
          class Meta :
              model= Achat_drisse
              fields=('Date','desg', 'Qté','unite', 'pu', 'Observation')
              labels = {'Date':'Date','desg': 'Désignation','Qté': 'Quntité','pu': 'Prix unitaire'}


class MobileFormo(forms.ModelForm):
          class Meta :
              model= Achat_Aoulouz
              fields=('Date','desg', 'Qté','unite', 'pu', 'Observation')
              labels = {'Date':'Date','desg': 'Désignation','Qté': 'Quntité','pu': 'Prix unitaire'}


class MariemFormo(forms.ModelForm):
          class Meta :
              model= Achat_Mariem
              fields=('Date','desg', 'Qté','unite', 'pu', 'Observation')
              labels = {'Date':'Date','desg': 'Désignation','Qté': 'Quntité','pu': 'Prix unitaire'}


class RgaigueFormo(forms.ModelForm):
          class Meta :
              model= Achat_rgaigue
              fields=('Date','desg', 'Qté','unite', 'pu', 'Observation')
              labels = {'Date':'Date','desg': 'Désignation','Qté': 'Quntité','pu': 'Prix unitaire'}

class LglidiFormo(forms.ModelForm):
          class Meta :
              model= Achat_lglidi
              fields=('Date','desg', 'Qté','unite', 'pu', 'Observation')
              labels = {'Date':'Date','desg': 'Désignation','Qté': 'Quntité','pu': 'Prix unitaire'}

class BenmbarkFormo(forms.ModelForm):
          class Meta :
              model= Achat_benmbark
              fields=('Date','desg', 'Qté','unite', 'pu', 'Observation')
              labels = {'Date':'Date','desg': 'Désignation','Qté': 'Quntité','pu': 'Prix unitaire'}

class RaisinFormo(forms.ModelForm):
          class Meta :
              model= Achat_raisin
              fields=('Date','desg', 'Qté','unite', 'pu', 'Observation')
              labels = {'Date':'Date','desg': 'Désignation','Qté': 'Quntité','pu': 'Prix unitaire'}

class Banan1Formo(forms.ModelForm):
          class Meta :
              model= Achat_bananier1
              fields=('Date','desg', 'Qté','unite', 'pu', 'Observation')
              labels = {'Date':'Date','desg': 'Désignation','Qté': 'Quntité','pu': 'Prix unitaire'}

class Banan2Formo(forms.ModelForm):
          class Meta :
              model= Achat_bananier2
              fields=('Date','desg', 'Qté','unite', 'pu', 'Observation')
              labels = {'Date':'Date','desg': 'Désignation','Qté': 'Quntité','pu': 'Prix unitaire'}

class ZbirateFormo(forms.ModelForm):
          class Meta :
              model= Achat_zbirate
              fields=('Date','desg', 'Qté','unite', 'pu', 'Observation')
              labels = {'Date':'Date','desg': 'Désignation','Qté': 'Quntité','pu': 'Prix unitaire'}

class Mariem2Formo(forms.ModelForm):
          class Meta :
              model= Achat_Maryem2
              fields=('Date','desg', 'Qté','unite', 'pu', 'Observation')
              labels = {'Date':'Date','desg': 'Désignation','Qté': 'Quntité','pu': 'Prix unitaire'}

class MurcottFormo(forms.ModelForm):
          class Meta :
              model= Achat_murcott
              fields=('Date','desg', 'Qté','unite', 'pu', 'Observation')
              labels = {'Date':'Date','desg': 'Désignation','Qté': 'Quntité','pu': 'Prix unitaire'}

class CaisseForm(forms.ModelForm):
          class Meta :
              model= Caisse              
              fields =('libelle','recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde')



class EngraisBRForm(forms.ModelForm):
          class Meta :
              model= Engrais_berhil                         
              fields =('categorie', 'stock','mesure')

class EngraisawForm(forms.ModelForm):
          class Meta :
              model= Engrais_Aoulouz                    
              fields =('categorie', 'stock','mesure')  

class EngraishwForm(forms.ModelForm):
          class Meta :
              model= Engrais_Mariem           
              fields =('categorie', 'stock','mesure')             


class EngraisAOForm(forms.ModelForm):
          class Meta :
              model = Engrais_Aoulouz                         
              fields =('categorie', 'stock','mesure')


class EngraisMRForm(forms.ModelForm):
          class Meta :
              model = Engrais_Mariem                        
              fields =('categorie', 'stock','mesure')





class StockSearchForm(forms.ModelForm):
              class Meta:
                  model = Engrais_berhil
                  fields = ['categorie']
                  
class ArticleSearchForm(forms.ModelForm):
              class Meta:
                  model = Article
                  fields = ['titre','date']
                  labels = {'date':'Date','titre': 'Domaine'}
class PesticideBRForm(forms.ModelForm):
          class Meta :
              model= Pesticide_berhil                         
              fields =('category','groupe', 'stock','mesure')





class PesticideAOForm(forms.ModelForm):
          class Meta :
              model= Pesticide_Aoulouz                    
              fields =('category','groupe', 'stock','mesure')

class PesticideMRForm(forms.ModelForm):
          class Meta :
              model= Pesticide_Mariem               
              fields =('category','groupe', 'stock','mesure')



class StockSearchPSForm(forms.ModelForm):
              class Meta:
                  model = Pesticide_berhil
                  fields = ['category']
                  labels = { 'category': 'Produits'}
                  


class MouvementForm436(forms.ModelForm):
              class Meta:
                    model = Mouvement_436
                    fields = ['Date','Zone',  'Verger','NBR_caisses_Entrée','Bon_caisserie','Véhicule_entré',
                    'NBR_caisses_Sortie','Bon_livraison','Véhicule_sorti','Varieté','Poids','Observation']
                    
                    widgets = {
                     'Date': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Zone': forms.Select(attrs={'class': 'form-control'}),
                     'Verger': forms.Select(attrs={'class': 'form-control'}),
                     'NBR_caisses_Entrée': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Bon_caisserie': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Véhicule_entré': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'NBR_caisses_Sortie': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Bon_livraison': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Véhicule_sorti': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Varieté': forms.Select(attrs={'class': 'form-control'}),
                     'Poids': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Observation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                       }

class MouvementForm4660(forms.ModelForm):
              class Meta:
                    model = Mouvement_4660
                    fields = ['Date','Zone',  'Verger','NBR_caisses_Entrée','Bon_caisserie','Véhicule_entré',
                    'NBR_caisses_Sortie','Bon_livraison','Véhicule_sorti','Varieté','Poids','Observation']
                    
                    widgets = {
                     'Date': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Zone': forms.Select(attrs={'class': 'form-control'}),
                     'Verger': forms.Select(attrs={'class': 'form-control'}),
                     'NBR_caisses_Entrée': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Bon_caisserie': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Véhicule_entré': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'NBR_caisses_Sortie': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Bon_livraison': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Véhicule_sorti': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Varieté': forms.Select(attrs={'class': 'form-control'}),
                     'Poids': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Observation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                       }

class MouvementForm3434(forms.ModelForm):
              class Meta:
                    model = Mouvement_3434
                    fields = ['Date','Zone',  'Verger','NBR_caisses_Entrée','Bon_caisserie','Véhicule_entré',
                    'NBR_caisses_Sortie','Bon_livraison','Véhicule_sorti','Varieté','Poids','Observation']
                    
                    widgets = {
                     'Date': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Zone': forms.Select(attrs={'class': 'form-control'}),
                     'Verger': forms.Select(attrs={'class': 'form-control'}),
                     'NBR_caisses_Entrée': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Bon_caisserie': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Véhicule_entré': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'NBR_caisses_Sortie': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Bon_livraison': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Véhicule_sorti': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Varieté': forms.Select(attrs={'class': 'form-control'}),
                     'Poids': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Observation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                       }


class MouvementForm2200(forms.ModelForm):
              class Meta:
                    model = Mouvement_2200
                    fields = ['Date','Zone',  'Verger','NBR_caisses_Entrée','Bon_caisserie','Véhicule_entré',
                    'NBR_caisses_Sortie','Bon_livraison','Véhicule_sorti','Varieté','Poids','Observation']
                    
                    widgets = {
                     'Date': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Zone': forms.Select(attrs={'class': 'form-control'}),
                     'Verger': forms.Select(attrs={'class': 'form-control'}),
                     'NBR_caisses_Entrée': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Bon_caisserie': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Véhicule_entré': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'NBR_caisses_Sortie': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Bon_livraison': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Véhicule_sorti': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Varieté': forms.Select(attrs={'class': 'form-control'}),
                     'Poids': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Observation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                       }

class MouvementForm1286(forms.ModelForm):
              class Meta:
                    model = Mouvement_1286
                    fields = ['Date','Zone',  'Verger','NBR_caisses_Entrée','Bon_caisserie','Véhicule_entré',
                    'NBR_caisses_Sortie','Bon_livraison','Véhicule_sorti','Varieté','Poids','Observation']
                    
                    widgets = {
                     'Date': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Zone': forms.Select(attrs={'class': 'form-control'}),
                     'Verger': forms.Select(attrs={'class': 'form-control'}),
                     'NBR_caisses_Entrée': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Bon_caisserie': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Véhicule_entré': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'NBR_caisses_Sortie': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Bon_livraison': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Véhicule_sorti': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Varieté': forms.Select(attrs={'class': 'form-control'}),
                     'Poids': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Observation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                       }
class MouvementForm2453(forms.ModelForm):
              class Meta:
                    model = Mouvement_2453
                    fields = ['Date','Zone',  'Verger','NBR_caisses_Entrée','Bon_caisserie','Véhicule_entré',
                    'NBR_caisses_Sortie','Bon_livraison','Véhicule_sorti','Varieté','Poids','Observation']
                    
                    widgets = {
                     'Date': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Zone': forms.Select(attrs={'class': 'form-control'}),
                     'Verger': forms.Select(attrs={'class': 'form-control'}),
                     'NBR_caisses_Entrée': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Bon_caisserie': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Véhicule_entré': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'NBR_caisses_Sortie': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Bon_livraison': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Véhicule_sorti': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Varieté': forms.Select(attrs={'class': 'form-control'}),
                     'Poids': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Observation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                       }

class MouvementForm2805(forms.ModelForm):
              class Meta:
                    model = Mouvement_2805
                    fields = ['Date','Zone',  'Verger','NBR_caisses_Entrée','Bon_caisserie','Véhicule_entré',
                    'NBR_caisses_Sortie','Bon_livraison','Véhicule_sorti','Varieté','Poids','Observation']
                    
                    widgets = {
                     'Date': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Zone': forms.Select(attrs={'class': 'form-control'}),
                     'Verger': forms.Select(attrs={'class': 'form-control'}),
                     'NBR_caisses_Entrée': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Bon_caisserie': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Véhicule_entré': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'NBR_caisses_Sortie': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Bon_livraison': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Véhicule_sorti': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Varieté': forms.Select(attrs={'class': 'form-control'}),
                     'Poids': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Observation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                       }


class MouvementForm774(forms.ModelForm):
              class Meta:
                    model = Mouvement_774
                    fields = ['Date','Zone',  'Verger','NBR_caisses_Entrée','Bon_caisserie','Véhicule_entré',
                    'NBR_caisses_Sortie','Bon_livraison','Véhicule_sorti','Varieté','Poids','Observation']
                    
                    widgets = {
                     'Date': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Zone': forms.Select(attrs={'class': 'form-control'}),
                     'Verger': forms.Select(attrs={'class': 'form-control'}),
                     'NBR_caisses_Entrée': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Bon_caisserie': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Véhicule_entré': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'NBR_caisses_Sortie': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Bon_livraison': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Véhicule_sorti': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Varieté': forms.Select(attrs={'class': 'form-control'}),
                     'Poids': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Observation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                       }

class MouvementForm2463(forms.ModelForm):
              class Meta:
                    model = Mouvement_2463
                    fields = ['Date','Zone',  'Verger','NBR_caisses_Entrée','Bon_caisserie','Véhicule_entré',
                    'NBR_caisses_Sortie','Bon_livraison','Véhicule_sorti','Varieté','Poids','Observation']
                    
                    widgets = {
                     'Date': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Zone': forms.Select(attrs={'class': 'form-control'}),
                     'Verger': forms.Select(attrs={'class': 'form-control'}),
                     'NBR_caisses_Entrée': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Bon_caisserie': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Véhicule_entré': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'NBR_caisses_Sortie': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Bon_livraison': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Véhicule_sorti': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Varieté': forms.Select(attrs={'class': 'form-control'}),
                     'Poids': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Observation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                       }

class MouvementForm1574(forms.ModelForm):
              class Meta:
                    model = Mouvement_1574
                    fields = ['Date','Zone',  'Verger','NBR_caisses_Entrée','Bon_caisserie','Véhicule_entré',
                    'NBR_caisses_Sortie','Bon_livraison','Véhicule_sorti','Varieté','Poids','Observation']
                    
                    widgets = {
                     'Date': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Zone': forms.Select(attrs={'class': 'form-control'}),
                     'Verger': forms.Select(attrs={'class': 'form-control'}),
                     'NBR_caisses_Entrée': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Bon_caisserie': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Véhicule_entré': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'NBR_caisses_Sortie': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Bon_livraison': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Véhicule_sorti': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Varieté': forms.Select(attrs={'class': 'form-control'}),
                     'Poids': forms.TextInput(attrs={'class': 'form-control mt-2'}),
                     'Observation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                       }


class MouvementSearchForm(forms.ModelForm):
              class Meta:
                  model = Mouvement_caisse
                  fields = ['Date','Zone','Verger','Varieté']
                     

class engraisbrForm(forms.ModelForm):
          class Meta:
              model = Engrais_berhil
              fields =('categorie','stock', 'mesure')
              labels = {'categorie':'Categorie','stock': 'Stock','mesure': 'Unité'}