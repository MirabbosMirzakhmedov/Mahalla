from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, UpdateView, \
    DeleteView
from django.shortcuts import redirect
from django.shortcuts import render
from webapp.forms import PostForm, CommentForm, ProfileForm, PostNeighborsForm, \
    NeighborCommentForm
from .forms import SignUpForm
from .models import Post, User, Comment, Business, PostNeighbors


def index(request):
    posts = Post.objects.all().order_by('-created_at')
    comments = Comment.objects.all().order_by('-created_at')

    latest_news = posts.first()
    other_posts = posts[1:]
    last_five = comments[:5]

    data = {
        'last_five': last_five,
        'posts': posts,
        'latest_news': latest_news,
        'other_posts': other_posts,
        'title': "So'nggi yangiliklar",
    }
    return render(request, 'webapp/index.html', data)


def about(request):
    data = {
        'title': 'About us'
    }
    return render(request, 'webapp/about.html', data)


class CreatePostView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        error = ''
        form = PostForm()
        data = {'form': form, 'error': error}
        return render(request, 'webapp/create.html', data)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.success(request, 'Bu yerda sizga ruxsat berilmagan.')
            return redirect('home')

        return super().dispatch(request, *args, **kwargs)

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

class CreateNeighborPostView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        error = ''
        form = PostNeighborsForm()
        data = {'form': form, 'error': error}
        return render(request, 'webapp/create.html', data)

    def post(self, request):
        error = ''
        form = PostNeighborsForm(request.POST, request.FILES)

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
            messages.success(request, 'Siz veb-saytga kirdingiz')
            return redirect('home')
        else:
            messages.success(request,
                             'Xatolik yuz berdi, keyinroq qayta urinib ko‘ring.')
            return redirect('login')

    else:
        return render(request, 'webapp/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, ('Siz tizimdan chiqdingiz.'))
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
            messages.success(request, 'Siz roʻyxatdan oʻtdingiz, iltimos tizimga kiring')
            return redirect('login')
        else:
            if form.errors['username'] == ['A user with that username already exists.']:
                messages.error(request, 'Bu foydalanuvchi nomi mavjud. Iltimos, boshqa nom tanlang.')
            else:
                messages.error(request, 'Muammo yuz berdi, keyinroq qayta urinib ko‘ring.')
            return redirect('register')
    else:
        return render(request, 'webapp/register.html', {'form': form})


class PostDetailView(DetailView):
    model = Post
    template_name = 'webapp/news_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = (Comment.objects.all().order_by('-created_at'))[:5]
        return context

class NeighborPostDetailView(DetailView):
    model = PostNeighbors
    template_name = 'webapp/neighbor_news_detail.html'
    context_object_name = 'neighbor_post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = (Comment.objects.all().order_by('-created_at'))[:5]
        return context

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Post
    template_name = 'webapp/create.html'
    form_class = PostForm

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.request.user.pk != self.object.user_id_id:
            messages.success(request, 'Bu yerda sizga ruxsat berilmagan.')
            return redirect('home')

        return super().dispatch(request, *args, **kwargs)

class NeighborPostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = PostNeighbors
    template_name = 'webapp/create.html'
    form_class = PostForm

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.request.user.pk != self.object.user_id_id:
            messages.success(request, 'Bu yerda sizga ruxsat berilmagan.')
            return redirect('home')

        return super().dispatch(request, *args, **kwargs)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Post
    success_url = reverse_lazy('home')
    template_name = 'webapp/post_delete.html'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.request.user.pk != self.object.user_id_id:
            messages.success(request, 'Bu yerda sizga ruxsat berilmagan.')
            return redirect('home')

        return super().dispatch(request, *args, **kwargs)

class NeighborPostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = PostNeighbors
    success_url = reverse_lazy('home')
    template_name = 'webapp/post_delete.html'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.request.user.pk != self.object.user_id_id:
            messages.success(request, 'Bu yerda sizga ruxsat berilmagan.')
            return redirect('home')

        return super().dispatch(request, *args, **kwargs)


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

def neighbors_add_comment(request, pk):
    post = get_object_or_404(PostNeighbors, pk=pk)

    if request.method == 'POST':
        form = NeighborCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
    return redirect('neighbor-news-detail', pk=pk)





class ProfileDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = User
    template_name = 'webapp/profile.html'
    context_object_name = 'profile_view'

    def get_object(self, queryset=None):
        user_id = self.kwargs.get('pk')
        return get_object_or_404(User, pk=user_id)

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        profile_view = self.get_object()
        comments = Comment.objects.filter(user=profile_view)
        context['profile_view'] = profile_view
        context['comments'] = comments
        if self.request.user == profile_view:
            context['form'] = ProfileForm(instance=profile_view)
        return context

    def post(self, request, *args, **kwargs):
        profile_view = self.get_object()
        form = ProfileForm(request.POST, request.FILES, instance=profile_view)
        if form.is_valid():
            form.save()
        return self.get(request, *args, **kwargs)

def business(request):
    categories = Business.CATEGORIES
    categories_with_businesses = []

    for category_key, _ in categories:
        businesses = Business.objects.filter(category=category_key)
        categories_with_businesses.append((category_key, businesses))

    data = {
        'categories_with_businesses': categories_with_businesses,
        'categories': categories,
        'title': "Atrofimizda",
    }

    return render(request, 'webapp/business.html', data)




def neighbors(request):
    neighbors = PostNeighbors.objects.all().order_by('-created_at')

    data = {
        'title': "Qo'shnilardan yangilik",
        'neighbors': neighbors
    }
    return render(request, 'webapp/neighbors.html', data)

