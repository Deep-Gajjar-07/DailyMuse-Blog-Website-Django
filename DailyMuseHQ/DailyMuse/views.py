from django.shortcuts import render
from .models import Blog
from .forms import BlogForm, UserRegistrationForm
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

def blogs(request):
    blogs = Blog.objects.all().order_by('-id')
    return render(request,'blog_list.html',{'blogs':blogs})

@login_required
def create_blog(request):
    form_class = BlogForm
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('homepage')
    else:
        form = BlogForm()
    return render(request,'blog_form.html',{'form':form})

@login_required
def my_blogs(request):
    my_blogs = Blog.objects.filter(user=request.user).order_by('-id')
    return render(request,'my_blogs.html',{'my_blogs':my_blogs})

@login_required
def edit_blog(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id,user = request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST,instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect('homepage')
    else:
        form = BlogForm(instance=blog)
    return render(request,'blog_form.html',{'form':form})

@login_required
def delete_blog(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id,user=request.user)
    if request.method == "POST":
        blog.delete()
        return redirect('homepage')
    return render(request,'delete_confim_blog.html',{'blog':blog})

def register(request):
    form_class = UserRegistrationForm
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('homepage')
    else:
            form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})
