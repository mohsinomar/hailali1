from django.shortcuts import render, redirect

from django.urls import reverse
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from paie.models import Article
from paie.forms import ArticleForm, ArticleSearchForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
import datetime
import xlwt



@login_required

def user_article(request):
          if not request.user.is_authenticated:
                        return redirect('home')
          title = 'Liste des rapports'
          compte=Article.objects.count()             
          has_perm= False
          if request.user.has_perm("project.delete_article"):
                    has_perm= True
          
          list_articles= Article.objects.all()
          paginator = Paginator(list_articles,15)
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
          form = ArticleSearchForm(request.POST or None)
          if request.method == 'POST':          
                  items= Article.objects.filter(titre__icontains=form['titre'].value(),
                                                        date__icontains=form['date'].value()
                                                        )

          context ={
              'title':title,
              'form':form,
              'list_articles':list_articles,
              "has_perm":has_perm,
              'items': items,
              'page_range': page_range,
              'compte':compte
              }

          return render(request,'my-articles.html',context)
#####################################################################
def bilan(request, id_article):
          article = Article.objects.get(id=id_article)         
          return render(request,'bilan.html', {"article": article})






class AddArticle(LoginRequiredMixin,CreateView):
          model=Article
          form_class=ArticleForm
          template_name='ajouter-article.html'
          success_url="/my-admin/my-articles" 


          def form_valid(self,form):

                    form.instance.user=self.request.user
                    return super().form_valid(form)

class UpdateArticle(LoginRequiredMixin,UpdateView):
          model = Article
          form_class= ArticleForm
          template_name ='app_admin/article_form.html'
          success_url ="/my-admin/my-articles"
          
class DeleteArticle(DeleteView):
          model = Article          
          success_url ="/my-admin/my-articles"

          def dispatch(self, request, *args, **kwargs):
                    if not request.user.has_perm('paie.delete_article'):
                              raise PermissionDenied

                    return super().dispatch(request, *args, **kwargs)
          


def export_Article(request):
          
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Ouled_berhil' + \
        str(datetime.datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Ouled_berhil')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['user','date','titre', 'description']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Article.objects.all().values_list(
        'user','date','titre', 'description')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response          


        

          
        



