from django.shortcuts import render, redirect
from .forms import ArticleForm, UserForm, UserLoginForm
from .models import Article
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'main.html', {})

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'error_form.html')
    else:
        form = ArticleForm()

        data = {
            'form': form
        }

        return render(request, 'create_article.html', data)

def articles(request):
    articles = Article.objects.all()
    
    data = {
        'articles':articles
    }

    return render(request, 'articles.html', data)

def post(request, id):
    article = Article.objects.get(id=id)

    data = {
        'article':article
    }

    return render(request, 'post.html', data)

def reg(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
            except:
                return render(request, 'error_form.html')
    else:
        form = UserForm()
    return render(request, 'registration.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
    form = UserLoginForm()
    return render(request, 'login.html', {'form': form, 'check':User.is_authenticated()})

def exit_user(request):
    logout(request)
    return redirect('index')
