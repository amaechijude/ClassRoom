from django.shortcuts import render, redirect
from decouple import config
from django.contrib.auth.decorators import login_required
from .forms import * #RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    return redirect('/login')

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email_or_username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "Loggend in")
                return redirect('/')
            else:
                messages.info(request, "rrror")
                return redirect('/login')
    form = LoginForm()
    return render(request, 'login.html', {"form": form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #message
            return redirect('/login')
        #error message
        return redirect('/register')
    form = RegisterForm()
    return render(request, 'register.html', {"form": form})
    
            
@login_required(login_url='/login')
def dashboard(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            author = request.user
            title = form.cleaned_data['title']
            img = request.FILES['img']
            tags = form.cleaned_data['tags']
            
            new_post = PostModel.objects.create(author=author, title=title,img=img,tags=tags)
            new_post.save()
          
            return redirect('dashboard')
        
    form = PostForm()
    posts = PostModel.objects.all()
    
    name = f"{request.user.first_name} {request.user.last_name}"
    context = {
        'form': form,
        'posts': posts,
        'name': name,
        }
    return render(request, 'dashboard.html', context)


@login_required(login_url='/login')
def meeting(request):
    name = f"{request.user.first_name} {request.user.last_name}"
    context = {
        "name": name,
        "APP_ID": config('APP_ID'),
        "SERVER_SECRET": config('SERVER_SECRET'),
        }
    return render(request, 'meeting.html', context)


@login_required(login_url='/login')
def joinroom(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect(f"/meeting?roomID={roomID}")
    return render(request, 'joinroom.html')


@login_required(login_url='/login')
def allpost(request):
    if request.method == 'POST':
        author = request.user
        title = request.POST['title']
        
        try:
            img = request.FILES['img']
        except:
            img = None
        
        new_post = PostModel.objects.create(author=author, title=title,img=img)#,tags=tags)
        new_post.save()
        
        return redirect('dashboard')

@login_required(login_url='login_user')
def postview(request, pk):
    post = PostModel.objects.get(pid=pk)
    comments = CommentModel.objects.filter(post=post)
    kp = pk    
    context = {
        'p': post,
        'comments': comments,
        'form': CommentForm(),
        'kp': kp,
    }
    return render(request, 'details.html', context)



@login_required(login_url='login_user')
def comment(request):
    if request.method == 'POST':
        author = request.user
        kp = request.POST['kp']
        post = PostModel.objects.get(pid=int(kp))
        title = request.POST['title']
        try:
            img = request.FILES['img']
        except:
            img = None
        new_comment = CommentModel.objects.create(author=author, title=title,post=post,img=img)
        new_comment.save()
        return redirect(f'/post/{int(kp)}')
