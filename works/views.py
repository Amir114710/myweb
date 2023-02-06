from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect , render
from django.views.generic import TemplateView , ListView , View , DeleteView
from account.models import Profile, User
from .models import Comments, Like, Work , Categories

class WorkView(ListView):
    model = Work
    template_name = "works/works_v2.html"
    context_object_name = 'works'
    def get_context_data(self ,*args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['user'] = Profile.objects.all()
        context['categories'] = Categories.objects.all()
        return context

class WorkDetailView(DeleteView):
    model = Work
    template_name = "works/single-post.html"
    context_object_name = 'works'
    queryset = None
    def get_context_data(self ,*args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['user'] = Profile.objects.all()
        queryset = Work.objects.get(slug = self.object.slug)
        queryset.save()
        if self.request.user.is_authenticated == True:
            if self.request.user.likes2.filter(works__english_title = self.object.english_title , users_id = self.request.user.id).exists():
                context['is_liked'] = True
            else:
                context['is_liked'] = False
        else:
            pass
        return context
    
    def post(self,request,slug):
        works = Work.objects.get(slug=slug)
        parent_id = request.POST.get('parent_id')
        message = request.POST.get('message')
        Comments.objects.create(message=message, parent_id=parent_id , works=works , user=request.user)
        return redirect('work:work_detail' , slug)
        
class Category_details(View):
    queryset = None
    template_name = 'works/category_work_detail.html'
    def get(self, request , pk):
        queryset = get_object_or_404(Categories , id=pk)
        objects = queryset.works.all()
        categories = Categories.objects.all()
        user = Profile.objects.all()
        return render (request , self.template_name , {'id':pk , 'works':objects , 'categories':categories , 'user':user })

def like(request , slug , pk):
    try:
        like = Like.objects.get(works__slug = slug , users_id=request.user.id)
        like.delete()
    except:
        Like.objects.create(works_id=pk , users_id = request.user.id)
    return redirect('work:work_detail' , slug)