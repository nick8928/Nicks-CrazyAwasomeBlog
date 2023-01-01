from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
from .models import Post, Category
from .forms import PostForm,UpdateForm



# Create your views here.
# def home(request):
#     return render(request,'home.html')

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    cats = Category.objects.all()
    # ordering = ['-id']
    ordering = ['-post_date']

# def get_context_data(self, *args, **kwargs):
#     cat_menu = Category.objects.all()
#     context = super(HomeView,self).get_context_data(*args,**kwargs)
#     context["cat_menu"] = cat_menu
#     return context


def CategoryView(request,cats):
    category_posts = Post.objects.filter(category= cats.replace('-',' '))
    return render(request,'categories.html',{'cats':cats.title().replace('-',' '),'category_posts':category_posts})



class Articles_detail_View(DetailView):
    model = Post
    template_name = 'articles_detail.html'


class AddPostView(CreateView):
    model = Post

    form_class = PostForm

    template_name = 'add_post.html'
    # fields = "__all__"

class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = "__all__"


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'
    # fields = ['title','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')