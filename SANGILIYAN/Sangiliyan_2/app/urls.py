from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostList.as_view(), name="home"),
    
    # --- LA ROUTE POUR LA CHRONOLOGIE ---
    path('timeline/', views.timeline, name="timeline"),
    
    # --- LA NOUVELLE ROUTE POUR LES ARCHIVES ---
    path('archives/', views.archives, name="archives"),
    
    # Toujours mettre le slug en DERNIER
    path('<slug:slug>/', views.DetailView.as_view(), name="post_detail"),
]

# Gestion des fichiers média (images des articles)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)