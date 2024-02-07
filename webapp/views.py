from django.shortcuts import render, redirect
from webapp.forms import PostForm


def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request,'webapp/index.html', data)


from .models import Post

def create_post(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user
            post.save()

            return redirect('home')
        else:
            error = "Maqolani to'liq to'ldiring"
    else:
        form = PostForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'webapp/about.html', data)
