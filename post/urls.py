from django.urls import path
from .views import UserApiView , PostListApiView, PostDetailApiView
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('users/', UserApiView.as_view()),
    path('posts/', PostListApiView.as_view()),
    path('token-auth/', views.obtain_auth_token),
    path('posts/<int:pk>/', PostDetailApiView.as_view(), name='post-detail'),  # DELETE by ID
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)