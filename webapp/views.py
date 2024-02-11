from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView, UpdateView, \
    DeleteView
from django.views import View
from django.urls import reverse_lazy
from webapp.forms import PostForm, CommentForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Post, User

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    data = {
        'posts': posts,
        'title': "So'nggi yangiliklar",
    }
    return render(request, 'webapp/index.html', data)

def about(request):
    data = {
        'title': 'About us'
    }
    return render(request, 'webapp/about.html', data)


# def create_post(request):
#     error = ''
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user_id = request.user
#             post.save()
#
#             return redirect('home')
#         else:
#             error = "Maqolani to'liq to'ldiring"
#     else:
#         form = PostForm()
#
#     data = {
#         'form': form,
#         'error': error
#     }
#
#     return render(request, 'webapp/create.html', data)

class CreatePostView(LoginRequiredMixin, View):
    login_url = '/login/'  # Specify the URL to redirect to if the user is not logged in

    def get(self, request):
        error = ''
        form = PostForm()
        data = {'form': form, 'error': error}
        return render(request, 'webapp/create.html', data)

    def post(self, request):
        error = ''
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user
            post.save()
            return redirect('home')
        else:
            error = "Maqolani to'liq to'ldiring"

        data = {'form': form, 'error': error}
        return render(request, 'webapp/create.html', data)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in')
            return redirect('home')
        else:
            messages.success(request, 'There was an error, please try again later.')
            return redirect('login')

    else:
        return render(request, 'webapp/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out.'))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # LOGIN
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have registered successfully')
            return redirect('home')
        else:
            messages.success(request, 'There was a problem, please try again later.')
            return redirect('register')
    else:
        return render(request, 'webapp/register.html', {'form': form})

class PostDetailView(DetailView):
    model = Post
    template_name = 'webapp/news_detail.html'
    context_object_name = 'post'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'webapp/create.html'
    form_class = PostForm

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'webapp/post_delete.html'

def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
    return redirect('news-detail', pk=pk)

from django.shortcuts import redirect

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'webapp/profile.html'
    context_object_name = 'profile_view'
    login_url = '/login/'  # Set the login URL where anonymous users will be redirected

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('pk')
        return get_object_or_404(User, pk=user_id)

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        profile_view = self.get_object()
        context['profile_view'] = profile_view
        if self.request.user == profile_view:
            context['form'] = ProfileForm(instance=profile_view)
        return context
    def post(self, request, *args, **kwargs):
        profile_view = self.get_object()
        form = ProfileForm(request.POST, request.FILES, instance=profile_view)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return self.render_to_response(self.get_context_data(form=form))
