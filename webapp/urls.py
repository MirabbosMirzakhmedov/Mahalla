from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.CreatePostView.as_view(), name='create'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('<int:pk>', views.PostDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/neighbor-post-update', views.NeighborPostUpdateView.as_view(), name='neighbor-post-update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('<int:pk>/neighbor-post-delete', views.NeighborPostDeleteView.as_view(), name='neighbor-post-delete'),
    path('<int:pk>/comment', views.add_comment, name='add-comment'),
    path('<int:pk>/neighbor-comment', views.neighbors_add_comment, name='neighbors-add-comment'),
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile'),
    path('about/', views.about, name='about'),
    path('business/', views.business, name='business'),
    path('notify-neighbors/', views.CreateNeighborPostView.as_view(), name='notify-neighbors'),
    path('post-neighbors/', views.neighbors, name='neighbors'),
    path('post-neighbors/<int:pk>', views.NeighborPostDetailView.as_view(), name='neighbor-news-detail'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<int:pk>', views.ImageDetailView.as_view(), name='image_detail_view'),
    path('image/', views.CreateImageView.as_view(), name='add_image')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)