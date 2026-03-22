from django.shortcuts import render
from django.views import generic
from .models import Post
from django.db.models import Q  # Import indispensable pour la recherche

class PostList(generic.ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query),
                status=1
            ).order_by('-created_on')
        
        return Post.objects.filter(status=1).order_by('-created_on')

class DetailView(generic.DetailView):
    model = Post
    template_name = 'post_details.html'

# --- FONCTION POUR LA CHRONOLOGIE ---
def timeline(request):
    return render(request, 'timeline.html')

# --- FONCTION MODIFIÉE POUR L'IA ---
def archives(request):
    # On pointe maintenant vers le nouveau fichier AI.html
    return render(request, 'AI.html')