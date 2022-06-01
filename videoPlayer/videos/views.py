from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Video

def index(request):
    return render(request, 'videos/index.html')

class CriarVideo(CreateView):
    model = Video
    fields = ['titulo', 'descricao', 'arquivos_de_video', 'thumbnail']
    template_name = 'videos/criar_video.html'
    
    # def get_success_url(self):
    #     return reverse('video-detail', kwargs={'pk': self.object.pk})