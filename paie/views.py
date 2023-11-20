

from django.db.models.aggregates import Avg, Sum, Count, Min, Max
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponse
import datetime
import xlwt
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from paie.forms import*
from django.shortcuts import get_object_or_404, render, redirect
from.models import*
from.forms import*
from django.views.generic.base import TemplateView
from django.db.models import F ,Subquery

#class Error404View(TemplateView):
          
   # template_name = 'errors/404.html'

def home(request):
    title = 'Groupe Hailali'
    my_template = 'home.html'
    if request == 'mobile':
        my_template = 'mobile_template.html'
    return render(request, my_template, {'title': title})


@login_required
def index(request):
    if not request.user.is_authenticated:
        return redirect('home')
    title = 'Liste des produits reçus'

    return render(request, 'index.html', {'title': title})


def index(request):
    title = 'Liste des produits reçus'
    return render(request, 'index.html', {'title': title})


def pesticide(request):
    if not request.user.is_authenticated:
        return redirect('home')
    return render(request, 'pesticide.html')


def affiche(request):
    if not request.user.is_authenticated:
        return redirect('home')
    title = 'Gestion de la caisse'
    items = Caisse.objects.all()
    return render(request, 'caisse.html', {'items': items, 'title': title})
from django import template

register = template.Library()



def display1(request):
    if not request.user.is_authenticated:
        return redirect('home')
   
     
    title = 'Liste des produits reçus'     
    subjects = Achat_berhil.objects.all().order_by('id')
    ziz = 0
    for subject in subjects:
                  maint_payable = (subject.Qté * subject.pu)
                  ziz += maint_payable
                  
                  
    context = {
         
            'title': title,         
            'subjects': subjects,
            'header': "Ouled_berhils",
              'ziz':ziz,
        }
   
    return render(request, 'index.html', context)





def display111(request):
    if not request.user.is_authenticated:
        return redirect('home')
    title = 'Stock des engrais'
    form = StockSearchForm(request.POST or None)
    elements = Engrais_berhil.objects.all()
    context = {
        "title": title,
        'elements': elements,
        'header': "Engrais_berhils",
        "form": form,
    }
    if request.method == 'POST':
        elements = Engrais_berhil.objects.filter(categorie__icontains=form['categorie'].value(),

                                                 )
        context = {
            "form": form,
            "title": title,
            "elements": elements,
            'header': "Engrais_berhils",

        }

    return render(request, 'engrais.html', context)

class engrais_berhil436(LoginRequiredMixin,CreateView):
    model = Engrais_berhil
    form_class = engraisbrForm
    template_name = 'add_engrais.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('display111')
    

class modifengrais436(LoginRequiredMixin, UpdateView):
    model = Engrais_berhil
    form_class = engraisbrForm
    template_name = 'modifier-engrais.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('display111')

class deletionengrais436(LoginRequiredMixin, DeleteView):
    model = Engrais_berhil
    

    
    def get_success_url(self):
        return reverse('display111')

def display1111(request):
    if not request.user.is_authenticated:
        return redirect('home')
    title = 'Stock des pesticides'
    form = StockSearchPSForm(request.POST or None)
    orderes = Pesticide_berhil.objects.all()
    context = {
        "title": title,
        'orderes': orderes,
        'header': "Pesticide_berhils",
        "form": form,
    }
    if request.method == 'POST':
        orderes = Pesticide_berhil.objects.filter(category__icontains=form['category'].value(),
        )
        context = {
            "form": form,
            "title": title,
            "orderes": orderes,
            'header': "Pesticide_berhils",
        }
    return render(request, 'pesticide.html', context)


class pestice_berhil436(LoginRequiredMixin,CreateView):
    model = Pesticide_berhil
    form_class = PesticideBRForm
    template_name = 'add_engrais.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('display1111')
    

class modifpestice436(LoginRequiredMixin, UpdateView):
    model = Pesticide_berhil
    form_class = PesticideBRForm
    template_name = 'modifier-engrais.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('display1111')

class deletionpestice436(LoginRequiredMixin, DeleteView):
    model = Pesticide_berhil
  
    def get_success_url(self):
        return reverse('display1111')




def caisse1(request):

    if not request.user.is_authenticated:
        return redirect('home')
    has_perm = True
    if request.user.has_perm('paie.view caisse_berhil'):
        items = caisse_berhil.objects.all()
        title = 'Gestion de la caisse'

        context = {

            'items': items,
            'title': title,
            'header': "OD_berhil --"
            "OD_drisse --"
            "Aoulouz ",
            'has_perm': has_perm

        }
    else:

        return redirect('home')

    return render(request, 'caisse.html', context)





def delete_desktop1(request, pk):
    if not request.user.is_authenticated:
        return redirect('home')
    Achat_berhil.objects.filter(id=pk).delete()
    subjects = Achat_berhil.objects.all()
    context = {
        'subjects': subjects
    }
    return render(request, 'index.html', context)


def export_436(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Ouled_berhil' + \
        str(datetime.datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Ouled_berhil')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['user','Date', 'Zone', 'Verger', 'NBR_caisses_Entrée', 'Bon_caisserie', 'Véhicule_entré', 'NBR_caisses_Sortie', 'Bon_livraison', 'Véhicule_sorti',
               'Varieté', 'Poids', 'Observation']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Mouvement_436.objects.all().values_list(
        'user','Date', 'Zone', 'Verger', 'NBR_caisses_Entrée', 'Bon_caisserie', 'Véhicule_entré', 'NBR_caisses_Sortie', 'Bon_livraison', 'Véhicule_sorti',
               'Varieté', 'Poids', 'Observation')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response


def export_excel11(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Engrais_Ouled_berhil' + \
        str(datetime.datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Engrais_Ouled_berhil')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['categorie', 'stock', 'mesure']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Engrais_berhil.objects.all().values_list(
        'categorie', 'stock', 'mesure')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response


def export_excel1111(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Pesticide_Ouled_berhil' + \
        str(datetime.datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Pesticide_Ouled_berhil')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['category', 'groupe', 'stock', 'mesure']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Pesticide_berhil.objects.all().values_list(
        'category', 'groupe', 'stock', 'mesure')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response


def export_caisse1(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=caisse_berhil' + \
        str(datetime.datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('caisse_berhil')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['libelle', 'recette', 'cumul_recette',
               'depense', 'cumul_depense', 'solde']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = caisse_berhil.objects.all().values_list(
        'libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response


def export_excel111(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Achat_berhil' + \
        str(datetime.datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Achat_Ouled_berhil')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['desg', 'Qté', 'pu', 'pt']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Achat_berhil.objects.all().values_list(
        'desg', 'Qté', 'pu', 'pt')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response


########################################################
##########################################################
# ********************OULED DRISSE*******************************************


def display2(request):
    if not request.user.is_authenticated:
        return redirect('home')
    
    title = 'Liste des produits reçus'
       
    subjects = Achat_drisse.objects.all().order_by('id')
    ziz = 0
    for subject in subjects:
                  maint_payable = (subject.Qté * subject.pu)
                  ziz += maint_payable
    context = {
             'ziz':ziz,
            'title': title,
          
            'subjects': subjects,
            'header': "Ouled_drisses"
        }
    
    return render(request, 'index.html', context)





def delete_laptop1(request, pk):
    if not request.user.is_authenticated:
        return redirect('home')
    Achat_drisse.objects.filter(id=pk).delete()
    subjects = Achat_drisse.objects.all()
    context = {
        'subjects': subjects
    }
    return render(request, 'index.html', context)


def display22(request):
    if not request.user.is_authenticated:
        return redirect('home')
    subjects = Achat_drisse.objects.all()
    context = {
        'subjects': subjects,
        'header': "Od_drisses"
    }
    return render(request, 'index.html', context)

















                                                 
        


def export_excel222(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Achat_Ouled_drisse.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Achat_Ouled_drisse')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['desg', 'Qté', 'pu', 'pt']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Achat_drisse.objects.all().values_list(
        'desg', 'Qté', 'pu', 'pt')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response



############################################################################
# ********************AOULOUZ*******************************************


def display3(request):
    if not request.user.is_authenticated:
        return redirect('home')
   
    subjects = Achat_Aoulouz.objects.all().order_by('id')
    title = 'Liste des produits reçus'
    ziz = 0
    for subject in subjects:
                  maint_payable = (subject.Qté * subject.pu)
                  ziz += maint_payable
    context = {
            'ziz':ziz,
            'title': title,         
            'subjects': subjects,
            'header': "Aoulouzs"
        }
   
    return render(request, 'index.html', context)


def display333(request):
    if not request.user.is_authenticated:
        return redirect('home')
    title = 'Stock des engrais'
    form = StockSearchForm(request.POST or None)
    elements = Engrais_Aoulouz.objects.all()
    context = {
        "title": title,
        'elements': elements,
        'header': "Engrais_Aoulouzs",
        "form": form,
    }
    if request.method == 'POST':
        elements = Engrais_Aoulouz.objects.filter(categorie__icontains=form['categorie'].value(),

                                                  )
        context = {
            "form": form,
            "title": title,
            "elements": elements,
            'header': "Engrais_Aoulouzs",


        }
    return render(request, 'engrais.html', context)


class engrais_aoulouz1286(LoginRequiredMixin,CreateView):
    model = Engrais_Aoulouz
    form_class = EngraisawForm
    template_name = 'add_engrais.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('display333')
    

class modifengrais1286(LoginRequiredMixin, UpdateView):
    model = Engrais_Aoulouz
    form_class = EngraisawForm
    template_name = 'modifier-engrais.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('display333')
    

class deletionengrais1286(LoginRequiredMixin, DeleteView):
    model = Engrais_Aoulouz    
    def get_success_url(self):
        return reverse('display333')

def display3333(request):
    if not request.user.is_authenticated:
        return redirect('home')
    title = 'Stock des pesticides'
    form = StockSearchPSForm(request.POST or None)
    orderes = Pesticide_Aoulouz.objects.all()
    context = {
        "title": title,
        'orderes': orderes,
        'header': "Pesticide_Aoulouzs",
        "form": form,
    }
    if request.method == 'POST':
        orderes = Pesticide_Aoulouz.objects.filter(category__icontains=form['category'].value(),
                                                   )
        context = {
            "form": form,
            "title": title,
            "orderes": orderes,
            'header': "Pesticide_Aoulouzs",

        }
    return render(request, 'pesticide.html', context)






class pestice_aoulouz1286(LoginRequiredMixin,CreateView):
    model = Pesticide_Aoulouz
    form_class = PesticideAOForm
    template_name = 'add_engrais.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('display3333')
    

class modifpestice1286(LoginRequiredMixin, UpdateView):
    model = Pesticide_Aoulouz
    form_class = PesticideAOForm
    template_name = 'modifier-engrais.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('display3333')

class deletionpestice1286(LoginRequiredMixin, DeleteView):
    model = Pesticide_Aoulouz
   
    def get_success_url(self):
        return reverse('display3333')


def display33(request):
    if not request.user.is_authenticated:
        return redirect('home')
    subjects = Achat_Aoulouz.objects.all()
    context = {
        'subjects': subjects,
        'header': "Aoulozs"
    }
    return render(request, 'index.html', context)








def delete_mobile1(request, pk):
    if not request.user.is_authenticated:
        return redirect('home')
    Achat_Aoulouz.objects.filter(id=pk).delete()
    subjects = Achat_Aoulouz.objects.all()
    context = {
        'subjects': subjects
    }
    return render(request, 'index.html', context)




def export_excel33(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Engrais_Aoulouz.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Engrais_Aoulouz')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['categorie', 'stock', 'mesure']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Engrais_Aoulouz.objects.all().values_list(
        'categorie', 'stock', 'mesure')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response


def export_excel333(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Achat_Aoulouz.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Achat_Aoulouz')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['desg', 'Qté', 'pu', 'pt']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Achat_Aoulouz.objects.all().values_list(
        'desg', 'Qté', 'pu', 'pt')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response


def export_excel3333(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Pesticide_Aoulouz.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Pesticide_Aoulouz')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['category', 'groupe', 'stock', 'mesure']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Pesticide_Aoulouz.objects.all().values_list(
        'category', 'groupe', 'stock', 'mesure')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response





def edit_mobile1(request, pk):
    return edit_achat(request, pk, Achat_Aoulouz, MobileFormo)







def detail(request, pk):
    title = 'Detail de rapport'
    article = Article.objects.get(id=pk)
    return render(request, 'detail.html', {"article": article, 'title': title})


def display4(request):
    if not request.user.is_authenticated:
        return redirect('home')

    title = 'Liste des produits reçus'
    subjects = Achat_Mariem.objects.all()
    ziz = 0
    for subject in subjects:
                  maint_payable = (subject.Qté * subject.pu)
                  ziz += maint_payable
    context = {
         'ziz':ziz,
        'title': title,
    
        'subjects': subjects,
        'header': "Mariems"
    }
    return render(request, 'index.html', context)


def display5(request):
    if not request.user.is_authenticated:
        return redirect('home')
    title = 'Liste des produits reçus'
   
    subjects = Achat_rgaigue.objects.all()
    ziz = 0
    for subject in subjects:
                  maint_payable = (subject.Qté * subject.pu)
                  ziz += maint_payable
    context = {
         'ziz':ziz,
        'title': title,
        'subjects': subjects,
        'header': "Plombier"
    }
    return render(request, 'index.html', context)


def add_employé(request, cls):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls()
        return render(request, 'add_new.html', {'form': form})


###########################################################################
#def add_depense(request, cls):
 #         
  #  if request.method == "POST":
   #     form = cls(request.POST)
    #    if form.is_valid():
     #       form.save()
      #      return redirect('index')
    #else:
     #   form = cls()
    #return render(request, 'ajouter_nv.html', {'form': form})


#def add_desktop1(request):
    #return add_depense(request, DesktopFormo)
class add_desktop1(LoginRequiredMixin, CreateView):
              model = Achat_berhil
    
              form_class = DesktopFormo
              template_name = 'ajouter_nv.html'

              def get_success_url(self):
                 return reverse('display1')

              def form_valid(self, form):
                 form.instance.user = self.request.user
                 return super().form_valid(form)



class Achat_berhil436(LoginRequiredMixin, UpdateView):
    model = Achat_berhil
    form_class = DesktopFormo
    template_name = 'edit_depense.html'
    user=Achat_berhil.user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('display1')

class deletion_berhil(LoginRequiredMixin, DeleteView):
              model = Achat_berhil 
              def get_success_url(self):
                  return reverse('display1')   


    


#def add_laptop1(request):
              
    #return add_depense(request, LaptopFormo)
class add_laptop1(LoginRequiredMixin,CreateView):
              model = Achat_drisse
              form_class = LaptopFormo
              template_name = 'ajouter_nv.html'
   
              def get_success_url(self):
                return reverse('display2')

              def form_valid(self, form):
               form.instance.user = self.request.user
               return super().form_valid(form)

class Achat_drisse4660(LoginRequiredMixin, UpdateView):
    model = Achat_drisse
    form_class = LaptopFormo
    template_name = 'edit_depense.html'
    user=Achat_drisse.user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('display2')

class deletion_drisse(LoginRequiredMixin,DeleteView):
              model = Achat_drisse
              def get_success_url(self):
                  return reverse('display2')

#def add_mobile1(request):
   # return add_depense(request, MobileFormo)
class add_mobile1(LoginRequiredMixin,CreateView):
              model = Achat_Aoulouz
              form_class = MobileFormo
              template_name = 'ajouter_nv.html'
   
              def get_success_url(self):
                return reverse('display3')

              def form_valid(self, form):
               form.instance.user = self.request.user
               return super().form_valid(form)

class Achat_aoulouz1286(LoginRequiredMixin, UpdateView):
    model = Achat_Aoulouz
    form_class = MobileFormo
    template_name = 'edit_depense.html'
    user=Achat_Aoulouz.user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('display3')


class deletion_aoulouz(LoginRequiredMixin,DeleteView):
    model = Achat_Aoulouz

    def get_success_url(self):
        return reverse('display3')
#def add_Mariema(request):
   # return add_depense(request, MariemFormo)
class add_Mariema(LoginRequiredMixin,CreateView):
              model = Achat_Mariem
              form_class = MariemFormo
              template_name = 'ajouter_nv.html'
   
              def get_success_url(self):
                return reverse('display4')

              def form_valid(self, form):
               form.instance.user = self.request.user
               return super().form_valid(form)
              
class Achat_mariem3434(LoginRequiredMixin, UpdateView):   
    model = Achat_Mariem
    form_class = MariemFormo
    template_name = 'edit_depense.html'
    user=Achat_Mariem.user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('display4')
    

class deletion_mariem3434(LoginRequiredMixin,DeleteView):
    model = Achat_Mariem

    def get_success_url(self):
        return reverse('display4')
#def add_Rgaiguea(request):
   # return add_depense(request, RgaigueFormo)

class add_Rgaiguea(LoginRequiredMixin,CreateView):
              model = Achat_rgaigue
              form_class = RgaigueFormo
              template_name = 'ajouter_nv.html'
   
              def get_success_url(self):
                return reverse('display5')

              def form_valid(self, form):
               form.instance.user = self.request.user
               return super().form_valid(form)

class Achat_rgauiegue(LoginRequiredMixin, UpdateView):   
    model = Achat_rgaigue
    form_class = RgaigueFormo
    template_name = 'edit_depense.html'
    user=Achat_rgaigue.user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('display5')


class deletion_rgauiegue(LoginRequiredMixin,DeleteView):
    model = Achat_rgaigue
    def get_success_url(self):
        return reverse('display5')
    
class add_Lglidi(LoginRequiredMixin,CreateView):
              model = Achat_lglidi
              form_class = LglidiFormo
              template_name = 'ajouter_nv.html'
   
              def get_success_url(self):
                return reverse('display6')

              def form_valid(self, form):
               form.instance.user = self.request.user
               return super().form_valid(form)


class Achat_lglidi1(LoginRequiredMixin, UpdateView):   
    model = Achat_lglidi
    form_class = LglidiFormo
    template_name = 'edit_depense.html'
    user=Achat_lglidi.user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('display6')
    
class deletion_lglidi(LoginRequiredMixin,DeleteView):
    model = Achat_lglidi
    def get_success_url(self):
        return reverse('display6')

class add_Benmbark(LoginRequiredMixin,CreateView):
              model = Achat_benmbark
              form_class = BenmbarkFormo
              template_name = 'ajouter_nv.html'
   
              def get_success_url(self):
                return reverse('display7')

              def form_valid(self, form):
               form.instance.user = self.request.user
               return super().form_valid(form)



class Achat_bnmbark1(LoginRequiredMixin, UpdateView):   
    model = Achat_benmbark
    form_class = BenmbarkFormo
    template_name = 'edit_depense.html'
    user=Achat_benmbark.user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('display7')

class deletion_benmbark(LoginRequiredMixin,DeleteView):
    model = Achat_benmbark
    def get_success_url(self):
        return reverse('display7')
    
class add_Raisin(LoginRequiredMixin,CreateView):
              model = Achat_raisin
              form_class = RaisinFormo
              template_name = 'ajouter_nv.html'
   
              def get_success_url(self):
                return reverse('display8')

              def form_valid(self, form):
               form.instance.user = self.request.user
               return super().form_valid(form)


class Achat_raisin1(LoginRequiredMixin, UpdateView):   
    model = Achat_raisin
    form_class = RaisinFormo
    template_name = 'edit_depense.html'
    user=Achat_raisin.user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('display8')

class deletion_raisin(LoginRequiredMixin,DeleteView):
    model = Achat_raisin
    def get_success_url(self):
        return reverse('display8')
    
class add_Banan1(LoginRequiredMixin,CreateView):
              model = Achat_bananier1
              form_class = Banan1Formo
              template_name = 'ajouter_nv.html'
   
              def get_success_url(self):
                return reverse('display9')

              def form_valid(self, form):
               form.instance.user = self.request.user
               return super().form_valid(form)


class Achat_banane1(LoginRequiredMixin, UpdateView):   
    model = Achat_bananier1
    form_class = Banan1Formo
    template_name = 'edit_depense.html'
    user=Achat_bananier1.user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('display9')
    
class deletion_banane1(LoginRequiredMixin,DeleteView):
    model = Achat_bananier1
    def get_success_url(self):
        return reverse('display9')

class add_Banan2(LoginRequiredMixin,CreateView):
              model = Achat_bananier2
              form_class = Banan2Formo
              template_name = 'ajouter_nv.html'
   
              def get_success_url(self):
                return reverse('displayban2')

              def form_valid(self, form):
               form.instance.user = self.request.user
               return super().form_valid(form)

class Achat_banane2(LoginRequiredMixin, UpdateView):   
    model = Achat_bananier2
    form_class = Banan2Formo
    template_name = 'edit_depense.html'
    user=Achat_bananier2.user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('displayban2')

class deletion_banane2(LoginRequiredMixin,DeleteView):
    model = Achat_bananier2
    def get_success_url(self):
        return reverse('displayban2')
                  
class add_Zbirate(LoginRequiredMixin,CreateView):
              model = Achat_zbirate
              form_class = ZbirateFormo
              template_name = 'ajouter_nv.html'
   
              def get_success_url(self):
                return reverse('displayzbi')

              def form_valid(self, form):
               form.instance.user = self.request.user
               return super().form_valid(form)

class Achat_zbirate1(LoginRequiredMixin, UpdateView):   
    model = Achat_zbirate
    form_class = ZbirateFormo
    template_name = 'edit_depense.html'
    user=Achat_zbirate.user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('displayzbi')

class deletion_zbirate(LoginRequiredMixin,DeleteView):
    model = Achat_zbirate
    def get_success_url(self):
        return reverse('displayzbi')
                  
class add_Mariem2(LoginRequiredMixin,CreateView):
              model = Achat_Maryem2
              form_class = Mariem2Formo
              template_name = 'ajouter_nv.html'
   
              def get_success_url(self):
                return reverse('displaymar')

              def form_valid(self, form):
               form.instance.user = self.request.user
               return super().form_valid(form)

class Achat_mariem1(LoginRequiredMixin, UpdateView):   
    model = Achat_Maryem2
    form_class = Mariem2Formo
    template_name = 'edit_depense.html'
    user=Achat_Maryem2.user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('displaymar')    

class deletion_maryem2(LoginRequiredMixin,DeleteView):
    model = Achat_Maryem2
    def get_success_url(self):
        return reverse('displaymar')   
           
class add_Murcott(LoginRequiredMixin,CreateView):
              model = Achat_murcott
              form_class = MurcottFormo
              template_name = 'ajouter_nv.html'
   
              def get_success_url(self):
                return reverse('displaymurcott')

              def form_valid(self, form):
               form.instance.user = self.request.user
               return super().form_valid(form)
              
class Achat_murcot1(LoginRequiredMixin, UpdateView):   
    model = Achat_murcott
    form_class = MurcottFormo
    template_name = 'edit_depense.html'
    user=Achat_murcott.user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('displaymurcott')  
    
class deletion_murcott(LoginRequiredMixin,DeleteView):
    model = Achat_murcott
    def get_success_url(self):
        return reverse('displaymurcott') 
###########################################################################



def caisse(request):
    if not request.user.is_authenticated:
        return redirect('home')
    title = 'Gestion de la caisse'
    return render(request, 'caisse.html', {'title': title})





def export_excel44(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Engrais_Mariem.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Engrais_Mariem')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['categorie', 'stock', 'mesure']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Engrais_Mariem.objects.all().values_list(
        'categorie', 'stock', 'mesure')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response





def engrais(request):
    if not request.user.is_authenticated:
        return redirect('home')
    return render(request, 'engrais.html')


def display444(request):
    if not request.user.is_authenticated:
        return redirect('home')
    title = 'Stock des engrais'
    form = StockSearchForm(request.POST or None)
    elements = Engrais_Mariem.objects.all()
    context = {
        "title": title,
        'elements': elements,
        'header': "Engrais Hawara",
        "form": form,
    }
    if request.method == 'POST':
        elements = Engrais_Mariem.objects.filter(categorie__icontains=form['categorie'].value(),

                                                 )
        context = {
            "form": form,
            "title": title,
            "elements": elements,
            'header': "Engrais Hawara",

        }

    return render(request, 'engrais.html', context)


class engrais_hwara3434(LoginRequiredMixin,CreateView):
    model = Engrais_Mariem
    form_class = EngraishwForm
    template_name = 'add_engrais.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('display444')
    

class modifengrais3434(LoginRequiredMixin, UpdateView):
    model = Engrais_Mariem
    form_class = EngraishwForm
    template_name = 'modifier-engrais.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('display444')

class deletionengrais3434(LoginRequiredMixin, DeleteView):
    model = Engrais_Mariem

    def get_success_url(self):
        return reverse('display444')

def add_consomation(request, cls):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect('engrais')
    else:
        form = cls()
    return render(request, 'add_engrais.html', {'form': form})


def add_desktop111(request):
    return add_consomation(request, EngraisBRForm)





def add_mobile111(request):
    return add_consomation(request, EngraisAOForm)


def edit_consomation(request, pk, model, cls):
    if not request.user.is_authenticated:
        return redirect('home')
    subject = get_object_or_404(model, pk=pk)
    if request.method == "POST":
        form = cls(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('engrais')
    else:
        form = cls(instance=subject)
        return render(request, 'modifier-item.html', {'form': form})


"""""
#################################################################
#################################################################
#################################################################
"""""


def export_excel4444(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Pesticide_Mariem.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Pesticide_Mariem')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['category', 'groupe', 'entree', 'cumul_entree', 'sortie',
               'time', 'destination', 'cumul_sortie', 'stock', 'mesure']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Pesticide_Mariem.objects.all().values_list(
        'category', 'groupe', 'stock', 'mesure')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response





def display4444(request):
    if not request.user.is_authenticated:
        return redirect('home')
    title = 'Stock des pesticides'
    form = StockSearchPSForm(request.POST or None)
    orderes = Pesticide_Mariem.objects.all()
    context = {
        "title": title,
        'orderes': orderes,
        'header': "Pesticide Hawara",
        "form": form,
    }
    if request.method == 'POST':
        orderes = Pesticide_Mariem.objects.filter(category__icontains=form['category'].value(),

                                                  )
        context = {
            "form": form,
            "title": title,
            "orderes": orderes,
            'header': "Pesticide Hawara",
        }
    return render(request, 'pesticide.html', context)

class pestice_hwara3434(LoginRequiredMixin,CreateView):
    model = Pesticide_Mariem
    form_class = PesticideMRForm
    template_name = 'add_engrais.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('display4444')
    

class modifpestice3434(LoginRequiredMixin, UpdateView):
    model = Pesticide_Mariem
    form_class = PesticideMRForm
    template_name = 'modifier-engrais.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('display4444')

class deletionpestice3434(LoginRequiredMixin, DeleteView):
    model = Pesticide_Mariem
  
    def get_success_url(self):
        return reverse('display4444')







def add_consomme(request, cls):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pesticide')
    else:
        form = cls()
    return render(request, 'add_engrais.html', {'form': form})


def edit_pesti(request, pk, model, cls):
    if not request.user.is_authenticated:
        return redirect('home')
    subject = get_object_or_404(model, pk=pk)
    if request.method == "POST":
        form = cls(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('pesticide')
    else:
        form = cls(instance=subject)

        return render(request, 'modifier-item.html', {'form': form})


class AddArticle(LoginRequiredMixin,CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'ajouter-article.html'
    success_url = "/my-admin/my-articles"

    def form_valid(self, form):

        form.instance.user = self.request.user
        return super().form_valid(form)
#################################################################
###################################################################
#######################################################################


def caisse4(request):
    if not request.user.is_authenticated:
        return redirect('home')
    items = caisse_Mariem.objects.all()
    title = 'Gestion de la caisse'
    context = {
        'items': items,
        'title': title,
        'header': "Hawara"
    }
    return render(request, 'caisse.html', context)




def export_caisse4(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=caisse_Mariem.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('caisse_Mariem')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['libelle', 'recette', 'cumul_recette',
               'depense', 'cumul_depense', 'solde']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = caisse_Mariem.objects.all().values_list(
        'libelle', 'recette', 'cumul_recette', 'depense', 'cumul_depense', 'solde')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response





def export_3434(request):         
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Meriem' + \
        str(datetime.datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Meriem')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['user','Date', 'Zone', 'Verger', 'NBR_caisses_Entrée', 'Bon_caisserie', 'Véhicule_entré', 'NBR_caisses_Sortie', 'Bon_livraison', 'Véhicule_sorti',
               'Varieté', 'Poids', 'Observation']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Mouvement_3434.objects.all().values_list(
        'user','Date', 'Zone', 'Verger', 'NBR_caisses_Entrée', 'Bon_caisserie', 'Véhicule_entré', 'NBR_caisses_Sortie', 'Bon_livraison', 'Véhicule_sorti',
               'Varieté', 'Poids', 'Observation')


    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response




########################################################
##########################################################

###########################################################


def export_excel444(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Achat_Mariem.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Achat_Mariem')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['desg', 'Qté', 'pu', 'pt']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Achat_Mariem.objects.all().values_list(
        'desg', 'Qté', 'pu', 'pt')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response


def export_excel555(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Achat_plombier.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Achat_plombier')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['desg', 'Qté', 'pu', 'pt']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Achat_rgaigue.objects.all().values_list(
        'desg', 'Qté', 'pu', 'pt')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response


def edit_achat(request, pk, model, cls):
    if not request.user.is_authenticated:
        return redirect('home')
    subject = get_object_or_404(model, pk=pk)
    if request.method == "POST":
        form = cls(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=subject)

        return render(request, 'modifier-item.html', {'form': form})


# ____________________________###########################____________________

def display6(request):

    if not request.user.is_authenticated:
        return redirect('home')
   
    title = 'Liste des produits reçus'
    subjects = Achat_lglidi.objects.all()
    ziz = 0
    for subject in subjects:
                  maint_payable = (subject.Qté * subject.pu)
                  ziz += maint_payable
    context = {
         'ziz':ziz,
        'title': title,       
        'subjects': subjects,
        'header': "Lglidi",

    }
    return render(request, 'index.html', context)


def display7(request):

    if not request.user.is_authenticated:
        return redirect('home')
    
    title = 'Liste des produits reçus'
    subjects = Achat_benmbark.objects.all()
    ziz = 0
    for subject in subjects:
                  maint_payable = (subject.Qté * subject.pu)
                  ziz += maint_payable
    context = {
         'ziz':ziz,
        'title': title,
   
        'subjects': subjects,
        'header': "Benmbark",

    }
    return render(request, 'index.html', context)


def display8(request):

    if not request.user.is_authenticated:
        return redirect('home')
   
    title = 'Liste des produits reçus'
    subjects = Achat_raisin.objects.all()
    ziz = 0
    for subject in subjects:
                  maint_payable = (subject.Qté * subject.pu)
                  ziz += maint_payable
    context = {
         'ziz':ziz,
        'title': title,
     
        'subjects': subjects,
        'header': "Raisin",

    }
    return render(request, 'index.html', context)


def display9(request):

    if not request.user.is_authenticated:
        return redirect('home')
   
    title = 'Liste des produits reçus'
    subjects = Achat_bananier1.objects.all()
    ziz = 0
    for subject in subjects:
                  maint_payable = (subject.Qté * subject.pu)
                  ziz += maint_payable
    context = {
         'ziz':ziz,
        'title': title,
    
        'subjects': subjects,
        'header': "Bananier1",

    }
    return render(request, 'index.html', context)


def displayban2(request):

    if not request.user.is_authenticated:
        return redirect('home')
   
    title = 'Liste des produits reçus'
    subjects = Achat_bananier2.objects.all()
    ziz = 0
    for subject in subjects:
                  maint_payable = (subject.Qté * subject.pu)
                  ziz += maint_payable
    context = {
        'title': title,
        'ziz':ziz,
        'subjects': subjects,
        'header': "Bananier2",

    }
    return render(request, 'index.html', context)


def displayzbi(request):

    if not request.user.is_authenticated:
        return redirect('home')
  
    title = 'Liste des produits reçus'
    subjects = Achat_zbirate.objects.all()
    ziz = 0
    for subject in subjects:
                  maint_payable = (subject.Qté * subject.pu)
                  ziz += maint_payable
    context = {
        'title': title,
        'ziz':ziz,
        'subjects': subjects,
        'header': "Zbirate",

    }
    return render(request, 'index.html', context)


def displaymar(request):

    if not request.user.is_authenticated:
        return redirect('home')
   
    title = 'Liste des produits reçus'
    subjects = Achat_Maryem2.objects.all()
    ziz = 0
    for subject in subjects:
                  maint_payable = (subject.Qté * subject.pu)
                  ziz += maint_payable
    context = {
        'title': title,
        'ziz':ziz,
        'subjects': subjects,
        'header': "Maryem2",

    }
    return render(request, 'index.html', context)

def displaymurcott(request):
          
    if not request.user.is_authenticated:
        return redirect('home')
   
    title = 'Liste des produits reçus'
    subjects = Achat_murcott.objects.all().order_by('id')
    ziz = 0
    for subject in subjects:
                  maint_payable = (subject.Qté * subject.pu)
                  ziz += maint_payable
    context = {
        'title': title,
        'ziz':ziz,
        'subjects': subjects,
        'header': "Murcott",

    }
    return render(request, 'index.html', context)


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




def export_achatgli(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Achat_lglidi' + \
        str(datetime.datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Achat_lglidi')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['desg', 'Qté', 'pu', 'pt']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Achat_lglidi.objects.all().values_list(
        'desg', 'Qté', 'pu', 'pt')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response




def export_achatbenm(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Achat_benmbark' + \
        str(datetime.datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Achat_benmbark')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['desg', 'Qté', 'pu', 'pt']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Achat_benmbark.objects.all().values_list(
        'desg', 'Qté', 'pu', 'pt')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response




def export_achatzbi(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Achat_zbirate' + \
        str(datetime.datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Achat_zbirate')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['desg', 'Qté', 'pu', 'pt']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Achat_zbirate.objects.all().values_list(
        'desg', 'Qté', 'pu', 'pt')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response





def export_achatmer(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Achat_maryem2' + \
        str(datetime.datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Achat_maryem2')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['desg', 'Qté', 'pu', 'pt']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Achat_Maryem2.objects.all().values_list(
        'desg', 'Qté', 'pu', 'pt')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response




def export_achatban1(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Achat_bananier1' + \
        str(datetime.datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Achat_bananier1')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['desg', 'Qté', 'pu', 'pt']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Achat_bananier1.objects.all().values_list(
        'desg', 'Qté', 'pu', 'pt')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response




def export_achatban2(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Achat_bananier2' + \
        str(datetime.datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Achat_bananier2')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['desg', 'Qté', 'pu', 'pt']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Achat_bananier2.objects.all().values_list(
        'desg', 'Qté', 'pu', 'pt')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response





def export_achatrais(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Achat_raisin' + \
        str(datetime.datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Achat_raisin')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['desg', 'Qté', 'pu', 'pt']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Achat_raisin.objects.all().values_list(
        'desg', 'Qté', 'pu', 'pt')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response
###################################################################
# caisse##########################""















#########################################display###################








def Mabrouka(request):

    return render(request, 'mabrouka.html')


def Domaines(request):
    title = 'Mouvement des caisses '
    titlo='Mouvement des caisses mabrouka pour touts les domaines Hailali'
    titla = 'Situation globale '
    titre='Tonnage global'
    stocko='Stock caisses vides en fonction des zones'
    entrant = Mouvement_caisse.objects.all().aggregate(Sum('NBR_caisses_Entrée'))
    sortant = Mouvement_caisse.objects.all().aggregate(Sum('NBR_caisses_Sortie'))
    restant = Mouvement_caisse.objects.all().aggregate(
    Restes_dans_tous_les_vergers =Sum('NBR_caisses_Entrée')-Sum('NBR_caisses_Sortie'))
    bilan = Mouvement_caisse.objects.values('Zone').annotate(Caisses_vides_en_stock=Sum('NBR_caisses_Entrée')-Sum('NBR_caisses_Sortie'))
    resultat = Mouvement_caisse.objects.values('Varieté').annotate(Tonnage=Sum('Poids'))
    pesant = Mouvement_caisse.objects.all().aggregate(Sum('Poids'))
    return render(request, 'domaines.html', { 'title':title,'stocko':stocko, 'titla': titla,'titlo': titlo,'titre':titre, 'entrant': entrant,
                                             'restant': restant, 'sortant': sortant ,'bilan': bilan, 'pesant': pesant,'resultat':resultat})


def mbrouka436(request):
    if not request.user.is_authenticated:
        return redirect('home')

    title = 'Mouvement des caisses '
    
    
    movs = Mouvement_436.objects.all().order_by('Bon_livraison')
    entré = Mouvement_436.objects.all().aggregate(Sum('NBR_caisses_Entrée'))
    sortie = Mouvement_436.objects.all().aggregate(Sum('NBR_caisses_Sortie'))
    reste = Mouvement_436.objects.all().aggregate(
    Reste_en_stock=Sum('NBR_caisses_Entrée')-Sum('NBR_caisses_Sortie'))
    poids = Mouvement_436.objects.all().aggregate(Sum('Poids'))
    result = Mouvement_436.objects.values('Varieté').annotate(Tonnage=Sum('Poids'))
    context = {
        "title": title,
        'result':result,
        'movs': movs,
        'header': "Domaine Ouled Berhil 436",
        'entré': entré,
        'sortie': sortie,
        'reste': reste,
        'poids': poids,
    }

    return render(request, 'mabrouka.html', context)


def mbrouka4660(request):
    if not request.user.is_authenticated:
        return redirect('home')
    title = 'Mouvement des caisses '
    list_movs = Mouvement_caisse.objects.all()
    movs = Mouvement_4660.objects.all().order_by('Bon_livraison')
    entré = Mouvement_4660.objects.all().aggregate(Sum('NBR_caisses_Entrée'))
    sortie = Mouvement_4660.objects.all().aggregate(Sum('NBR_caisses_Sortie'))
    reste = Mouvement_4660.objects.all().aggregate(
    Reste_en_stock=Sum('NBR_caisses_Entrée')-Sum('NBR_caisses_Sortie'))
    result = Mouvement_4660.objects.values('Varieté').annotate(Tonnage=Sum('Poids'))
    poids = Mouvement_4660.objects.all().aggregate(Sum('Poids'))

    context = {
        "title": title,
        'list_movs': list_movs,
        'movs': movs,
        'header': "Domaine Ouled Drisse 4660",
         'result':result,
        'entré': entré,
        'sortie': sortie,
        'reste': reste,
        'poids': poids,
    }

    return render(request, 'mabrouka.html', context)


def mbrouka1286(request):
    if not request.user.is_authenticated:
        return redirect('home')
    title = 'Mouvement des caisses '

    movs = Mouvement_1286.objects.all().order_by('Bon_livraison')
    entré = Mouvement_1286.objects.all().aggregate(Sum('NBR_caisses_Entrée'))
    sortie = Mouvement_1286.objects.all().aggregate(Sum('NBR_caisses_Sortie'))
    reste = Mouvement_1286.objects.all().aggregate(
    Reste_en_stock=Sum('NBR_caisses_Entrée')-Sum('NBR_caisses_Sortie'))
    poids = Mouvement_1286.objects.all().aggregate(Sum('Poids'))
    result = Mouvement_1286.objects.values('Varieté').annotate(Tonnage=Sum('Poids'))
    context = {
        "title": title,
        'result':result,
        'movs': movs,
        'header': "Domaine Aoulouz 1286",
        'entré': entré,
        'sortie': sortie,
        'reste': reste,
        'poids': poids,
    }

    return render(request, 'mabrouka.html', context)


def mbrouka774(request):
    if not request.user.is_authenticated:
        return redirect('home')
    
   
    title = 'Mouvement des caisses '
    
    movs = Mouvement_774.objects.all().order_by('Bon_livraison')
    entré = Mouvement_774.objects.all().aggregate(Sum('NBR_caisses_Entrée'))
    result = Mouvement_774.objects.values('Varieté').annotate(Tonnage=Sum('Poids'))
    sortie = Mouvement_774.objects.all().aggregate(Sum('NBR_caisses_Sortie'))
    reste = Mouvement_774.objects.all().aggregate(
    Reste_en_stock=Sum('NBR_caisses_Entrée')-Sum('NBR_caisses_Sortie'))
    poids = Mouvement_774.objects.all().aggregate(Sum('Poids'))
    context = {
        "title": title,
        'movs': movs,
        'header': "Domaine Aoulouz 774",
        'entré': entré,
        'sortie': sortie,
        'reste': reste,
        'poids': poids,
        'result':result,
    }
    


    return render(request, 'mabrouka.html', context)


def mbrouka3434(request):
      if not request.user.is_authenticated:
          return redirect('home')

      title = 'Mouvement des caisses '
      
      movs = Mouvement_3434.objects.all().order_by('Bon_livraison')
      paginator = Paginator(movs,15)
      page = request.GET.get('page')
      try:
               items = paginator.page(page)
      except PageNotAnInteger:
               items = paginator.page(1)
      except EmptyPage:
               items = paginator.page(paginator.num_pages)


      index = items.number - 1
      max_index = len(paginator.page_range)
      start_index = index -5 if index >= 5 else 0
      end_index = index + 5 if index <= max_index - 5 else max_index
      page_range= paginator.page_range[start_index:end_index]
      entré = Mouvement_3434.objects.all().aggregate(Sum('NBR_caisses_Entrée'))
      sortie = Mouvement_3434.objects.all().aggregate(Sum('NBR_caisses_Sortie'))
      reste = Mouvement_3434.objects.all().aggregate(
      Reste_en_stock=Sum('NBR_caisses_Entrée')-Sum('NBR_caisses_Sortie'))
      poids = Mouvement_3434.objects.all().aggregate(Sum('Poids'))
      result = Mouvement_3434.objects.values('Varieté').annotate(Tonnage=Sum('Poids'))
      
      context = {
        "title": title,
       'page_range':page_range,
       'items': items,
        'movs': movs,
        'header': "Domaine Mariem 3434",
        'entré': entré,
        'sortie': sortie,
        'reste': reste,
        'poids': poids,
        'result':result,
    }
   
      return render(request, 'mabrouka.html', context)


def mbrouka2453(request):
    if not request.user.is_authenticated:
        return redirect('home')
    title = 'Mouvement des caisses '

    movs = Mouvement_2453.objects.all().order_by('Bon_livraison')
    entré = Mouvement_2453.objects.all().aggregate(Sum('NBR_caisses_Entrée'))

    sortie = Mouvement_2453.objects.all().aggregate(Sum('NBR_caisses_Sortie'))
    reste = Mouvement_2453.objects.all().aggregate(
    Reste_en_stock=Sum('NBR_caisses_Entrée')-Sum('NBR_caisses_Sortie'))
    poids = Mouvement_2453.objects.all().aggregate(Sum('Poids'))
    result = Mouvement_2453.objects.values('Varieté').annotate(Tonnage=Sum('Poids'))
    context = {
        "title": title,
        'result':result,
        'movs': movs,
        'header': "Domaine Zbirate 2453",
        'entré': entré,
        'sortie': sortie,
        'reste': reste,
        'poids': poids,
    }

    return render(request, 'mabrouka.html', context)


def mbrouka2463(request):
    if not request.user.is_authenticated:
        return redirect('home')
    title = 'Mouvement des caisses '

    movs = Mouvement_2463.objects.all().order_by('Bon_livraison')
    entré = Mouvement_2463.objects.all().aggregate(Sum('NBR_caisses_Entrée'))
    result = Mouvement_2463.objects.values('Varieté').annotate(Tonnage=Sum('Poids'))
    sortie = Mouvement_2463.objects.all().aggregate(Sum('NBR_caisses_Sortie'))
    reste = Mouvement_2463.objects.all().aggregate(
    Reste_en_stock=Sum('NBR_caisses_Entrée')-Sum('NBR_caisses_Sortie'))
    poids = Mouvement_2463.objects.all().aggregate(Sum('Poids'))
    context = {
        "title": title,
        'result':result,
        'movs': movs,
        'header': "Domaine Aoulouz 2463",
        'entré': entré,
        'sortie': sortie,
        'reste': reste,
        'poids': poids,
    }

    return render(request, 'mabrouka.html', context)


def mbrouka1574(request):
    if not request.user.is_authenticated:
        return redirect('home')
    title = 'Mouvement des caisses '

    movs = Mouvement_1574.objects.all().order_by('Bon_livraison')
    entré = Mouvement_1574.objects.all().aggregate(Sum('NBR_caisses_Entrée'))
    result = Mouvement_1574.objects.values('Varieté').annotate(Tonnage=Sum('Poids'))
    sortie = Mouvement_1574.objects.all().aggregate(Sum('NBR_caisses_Sortie'))
    reste = Mouvement_1574.objects.all().aggregate(
    Reste_en_stock=Sum('NBR_caisses_Entrée')-Sum('NBR_caisses_Sortie'))
    poids = Mouvement_1574.objects.all().aggregate(Sum('Poids'))
    context = {
        "title": title,
        'result':result,
        'movs': movs,
        'header': "Domaine Aoulouz 1574",
        'entré': entré,
        'sortie': sortie,
        'reste': reste,
        'poids': poids,
    }

    return render(request, 'mabrouka.html', context)


def mbrouka2200(request):
    if not request.user.is_authenticated:
        return redirect('home')
    title = 'Mouvement des caisses '

    movs = Mouvement_2200.objects.all().order_by('Bon_livraison')
    entré = Mouvement_2200.objects.all().aggregate(Sum('NBR_caisses_Entrée'))
    result = Mouvement_2200.objects.values('Varieté').annotate(Tonnage=Sum('Poids'))
    sortie = Mouvement_2200.objects.all().aggregate(Sum('NBR_caisses_Sortie'))
    reste = Mouvement_2200.objects.all().aggregate(
    Reste_en_stock=Sum('NBR_caisses_Entrée')-Sum('NBR_caisses_Sortie'))
    poids = Mouvement_2200.objects.all().aggregate(Sum('Poids'))
    context = {
        "title": title,
        'result':result,
        'movs': movs,
        'header': "Domaine Plambier 2200",
        'entré': entré,
        'sortie': sortie,
        'reste': reste,
        'poids': poids,
    }

    return render(request, 'mabrouka.html', context)


def mbrouka2805(request):
    if not request.user.is_authenticated:
        return redirect('home')

    title = 'Mouvement des caisses '

    movs = Mouvement_2805.objects.all().order_by('Bon_livraison')
    entré = Mouvement_2805.objects.all().aggregate(Sum('NBR_caisses_Entrée'))
    result = Mouvement_2805.objects.values('Varieté').annotate(Tonnage=Sum('Poids'))
    sortie = Mouvement_2805.objects.all().aggregate(Sum('NBR_caisses_Sortie'))
    reste = Mouvement_2805.objects.all().aggregate(
    Reste_en_stock=Sum('NBR_caisses_Entrée')-Sum('NBR_caisses_Sortie'))
    poids = Mouvement_2805.objects.all().aggregate(Sum('Poids'))
    context = {
        "title": title,
        'result':result,
        'movs': movs,
        'header': "Domaine Zbirate 2805",
        'entré': entré,
        'sortie': sortie,
        'reste': reste,
        'poids': poids,
    }

    return render(request, 'mabrouka.html', context)


class modification436(LoginRequiredMixin, UpdateView):
    model = Mouvement_436
    form_class = MouvementForm436
    template_name = 'modifier-item.html'
    user=Mouvement_436.user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('mouvement-des-caisses-cuillette_436')


class modification4660(LoginRequiredMixin,UpdateView):
    model = Mouvement_4660
    form_class = MouvementForm4660
    template_name = 'modifier-item.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('mouvement-des-caisses-cuillette_4660')


class modification3434(LoginRequiredMixin,UpdateView):
    model = Mouvement_3434
    form_class = MouvementForm3434
    template_name = 'modifier-item.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('mouvement-des-caisses-cuillette_3434')


class modification2200(LoginRequiredMixin,UpdateView):
    model = Mouvement_2200
    form_class = MouvementForm2200
    template_name = 'modifier-item.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('mouvement-des-caisses-cuillette_2200')


class modification1286(LoginRequiredMixin,UpdateView):
    model = Mouvement_1286
    form_class = MouvementForm1286
    template_name = 'modifier-item.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('mouvement-des-caisses-cuillette_1286')


class modification2453(LoginRequiredMixin,UpdateView):
    model = Mouvement_2453
    form_class = MouvementForm2453
    template_name = 'modifier-item.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('mouvement-des-caisses-cuillette_2453')


class modification2805(LoginRequiredMixin,UpdateView):
    model = Mouvement_2805
    form_class = MouvementForm2805
    template_name = 'modifier-item.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('mouvement-des-caisses-cuillette_2805')


class modification774(LoginRequiredMixin,UpdateView):
    model = Mouvement_774
    form_class = MouvementForm774
    template_name = 'modifier-item.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('mouvement-des-caisses-cuillette_774')

class modification2463(LoginRequiredMixin,UpdateView):
    model = Mouvement_2463
    form_class = MouvementForm2463
    template_name = 'modifier-item.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('mouvement-des-caisses-cuillette_2463')

class modification1574(LoginRequiredMixin,UpdateView):
    model = Mouvement_1574
    form_class = MouvementForm1574
    template_name = 'modifier-item.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
                  return reverse('mouvement-des-caisses-cuillette_1574')

class deletion436(LoginRequiredMixin, DeleteView):
    model = Mouvement_436
    

    
    def get_success_url(self):
        return reverse('mouvement-des-caisses-cuillette_436')

    
class deletion4660(LoginRequiredMixin,DeleteView):
    model = Mouvement_4660

    def get_success_url(self):
        return reverse('mouvement-des-caisses-cuillette_4660')


class deletion3434(LoginRequiredMixin,DeleteView):
    model = Mouvement_3434

    def get_success_url(self):
        return reverse('mouvement-des-caisses-cuillette_3434')


class deletion2200(LoginRequiredMixin,DeleteView):
    model = Mouvement_2200

    def get_success_url(self):
        return reverse('mouvement-des-caisses-cuillette_2200')


class deletion1286(LoginRequiredMixin,DeleteView):
    model = Mouvement_1286

    def get_success_url(self):
        return reverse('mouvement-des-caisses-cuillette_1286')


class deletion2453(LoginRequiredMixin,DeleteView):
    model = Mouvement_2453

    def get_success_url(self):
        return reverse('mouvement-des-caisses-cuillette_2453')


class deletion2805(LoginRequiredMixin,DeleteView):
    model = Mouvement_2805

    def get_success_url(self):
        return reverse('mouvement-des-caisses-cuillette_2805')


class deletion774(LoginRequiredMixin, DeleteView):
    model = Mouvement_774

    def get_success_url(self):
        return reverse('mouvement-des-caisses-cuillette_774')


class deletion2463(LoginRequiredMixin,DeleteView):
    model = Mouvement_2463

    def get_success_url(self):
        return reverse('mouvement-des-caisses-cuillette_2463')


class deletion1574(LoginRequiredMixin,DeleteView):
    model = Mouvement_1574

    def get_success_url(self):
        return reverse('mouvement-des-caisses-cuillette_1574')


class mouvement436(LoginRequiredMixin, CreateView):
    model = Mouvement_436
    
    form_class = MouvementForm436
    template_name = 'ajouter-mouvement.html'

    def get_success_url(self):
        return reverse('mouvement-des-caisses-cuillette_436')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
   

  

class mouvement4660(LoginRequiredMixin,CreateView):
    model = Mouvement_4660
    form_class = MouvementForm4660
    template_name = 'ajouter-mouvement.html'
   
    def get_success_url(self):
        return reverse('mouvement-des-caisses-cuillette_4660')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class mouvement3434(LoginRequiredMixin,CreateView):
    
       model = Mouvement_3434
       form_class = MouvementForm3434
       template_name = 'ajouter-mouvement.html'

       def get_success_url(self):
           return reverse('mouvement-des-caisses-cuillette_3434')

       def form_valid(self, form):
           form.instance.user = self.request.user
           return super().form_valid(form)
    

class mouvement2200(LoginRequiredMixin,CreateView):
    model = Mouvement_2200
    form_class = MouvementForm2200
    template_name = 'ajouter-mouvement.html'

    def get_success_url(self):
        return reverse('mouvement-des-caisses-cuillette_2200')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class mouvement1286(LoginRequiredMixin,CreateView):
    model = Mouvement_1286
    form_class = MouvementForm1286
    template_name = 'ajouter-mouvement.html'

    def get_success_url(self):
        return reverse('mouvement-des-caisses-cuillette_1286')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class mouvement2453(LoginRequiredMixin,CreateView):
    model = Mouvement_2453
    form_class = MouvementForm2453
    template_name = 'ajouter-mouvement.html'

    def get_success_url(self):
        return reverse('mouvement-des-caisses-cuillette_2453')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class mouvement2805(LoginRequiredMixin,CreateView):
    model = Mouvement_2805
    form_class = MouvementForm2805
    template_name = 'ajouter-mouvement.html'

    def get_success_url(self):
        return reverse('mouvement-des-caisses-cuillette_2805')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class mouvement774(LoginRequiredMixin,CreateView):
    model = Mouvement_774
    form_class = MouvementForm774
    template_name = 'ajouter-mouvement.html'

    def get_success_url(self):
        return reverse('mouvement-des-caisses-cuillette_774')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class mouvement2463(LoginRequiredMixin,CreateView):
    model = Mouvement_2463
    form_class = MouvementForm2463
    template_name = 'ajouter-mouvement.html'

    def get_success_url(self):
        return reverse('mouvement-des-caisses-cuillette_2463')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class mouvement1574(LoginRequiredMixin,CreateView):
    model = Mouvement_1574
    form_class = MouvementForm1574
    template_name = 'ajouter-mouvement.html'

    def get_success_url(self):
        return reverse('mouvement-des-caisses-cuillette_1574')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def export_4660(request):
          
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Ouled_drisse' + \
        str(datetime.datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Ouled_drisse')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['user','Date', 'Zone', 'Verger', 'NBR_caisses_Entrée', 'Bon_caisserie', 'Véhicule_entré', 'NBR_caisses_Sortie', 'Bon_livraison', 'Véhicule_sorti',
               'Varieté', 'Poids', 'Observation']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Mouvement_4660.objects.all().values_list(
        'user','Date', 'Zone', 'Verger', 'NBR_caisses_Entrée', 'Bon_caisserie', 'Véhicule_entré', 'NBR_caisses_Sortie', 'Bon_livraison', 'Véhicule_sorti',
               'Varieté', 'Poids', 'Observation')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response

def export_2453(request):
          
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=zbirate2453' + \
        str(datetime.datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('birate2453')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['user','Date', 'Zone', 'Verger', 'NBR_caisses_Entrée', 'Bon_caisserie', 'Véhicule_entré', 'NBR_caisses_Sortie', 'Bon_livraison', 'Véhicule_sorti',
               'Varieté', 'Poids', 'Observation']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Mouvement_2453.objects.all().values_list(
        'user','Date', 'Zone', 'Verger', 'NBR_caisses_Entrée', 'Bon_caisserie', 'Véhicule_entré', 'NBR_caisses_Sortie', 'Bon_livraison', 'Véhicule_sorti',
               'Varieté', 'Poids', 'Observation')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response



def export_2200(request):
          
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=plambier' + \
        str(datetime.datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('plambier')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['user','Date', 'Zone', 'Verger', 'NBR_caisses_Entrée', 'Bon_caisserie', 'Véhicule_entré', 'NBR_caisses_Sortie', 'Bon_livraison', 'Véhicule_sorti',
               'Varieté', 'Poids', 'Observation']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Mouvement_2200.objects.all().values_list(
        'user','Date', 'Zone', 'Verger', 'NBR_caisses_Entrée', 'Bon_caisserie', 'Véhicule_entré', 'NBR_caisses_Sortie', 'Bon_livraison', 'Véhicule_sorti',
               'Varieté', 'Poids', 'Observation')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response
