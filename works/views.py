from django.shortcuts import get_object_or_404, redirect , render
from django.views.generic import TemplateView , ListView , View , DeleteView
from account.models import User
from .models import Comments, Work , Categories

class WorkView(ListView):
    model = Work
    template_name = "works/works_v2.html"
    context_object_name = 'works'
    def get_context_data(self ,*args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['user'] = User.objects.all()
        context['categories'] = Categories.objects.all()
        return context

class WorkDetailView(DeleteView):
    model = Work
    template_name = "works/single-post.html"
    context_object_name = 'works'
    def get_context_data(self ,*args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['user'] = User.objects.all()
        return context
    def post(self,request,slug):
        works = Work.objects.get(slug=slug)
        parent_id = request.POST.get('parent_id')
        message = request.POST.get('message')
        Comments.objects.create(message=message, parent_id=parent_id , works=works , user=request.user)
        return redirect('blog:detail' , slug)
        
class Category_details(View):
    queryset = None
    template_name = 'works/category_work_detail.html'
    def get(self, request , pk):
        queryset = get_object_or_404(Categories , id=pk)
        objects = queryset.works.all()
        categories = Categories.objects.all()
        user = User.objects.all()
        return render (request , self.template_name , {'id':pk , 'works':objects , 'categories':categories , 'user':user })