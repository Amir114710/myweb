from django.shortcuts import redirect, render
from django.views.generic import TemplateView , ListView , DetailView
from account.models import Profile
from .models import Post, PostComments , PostLike


class BlogView(ListView):
    model = Post
    template_name = "blog/weblog.html"
    context_object_name = 'posts'
    def get_context_data(self ,*args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['user'] = Profile.objects.all()
        return context
    
class PostDetail(DetailView):
    model = Post
    template_name = "blog/detailpage.html"
    context_object_name = 'posts'
    def get_context_data(self ,*args , **kwargs):
        context = super().get_context_data(*args , **kwargs)
        context['user'] = Profile.objects.all()
        queryset = Post.objects.get(slug = self.object.slug)
        queryset.save()
        if self.request.user.is_authenticated == True:
            if self.request.user.likes.filter(posts__english_title = self.object.english_title , users_id = self.request.user.id).exists():
                context['is_liked'] = True
            else:
                context['is_liked'] = False
        else:
            pass
        return context
    def post(self,request,slug):
        posts = Post.objects.get(slug=slug)
        parent_id = request.POST.get('parent_id')
        message = request.POST.get('message')
        PostComments.objects.create(message=message, parent_id=parent_id , posts=posts , user=request.user)
        return redirect('blog:post_detail' , slug)    
    
def like(request , slug , pk):
    try:
        like = PostLike.objects.get(posts__slug = slug , users_id=request.user.id)
        like.delete()
    except:
        PostLike.objects.create(posts_id=pk , users_id = request.user.id)
    return redirect('blog:post_detail' , slug)
