from django.shortcuts import redirect, render

from .forms import RegisterForm

def home(request):
    return render(request, 'blog/base.html')


def posts(request):
    return render(request, 'blog/posts.html')

def login_view(request):
    return render(request, 'blog/login.html')

# def register(request):
#     return render(request, 'blog/register.html')
def logout_view(request):
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})
