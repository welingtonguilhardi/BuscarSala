
from django import template



register = template.Library()

@register.filter
def extrair_id_do_video(link):
    try:
        # Verifica se é um link do YouTube
        if 'youtube.com' in link:
            # Extrai o ID do vídeo após "v=" na URL
            video_id = link.split('v=')[1]

            # Se houver outros parâmetros na URL, remove-os
            video_id = video_id.split('&')[0]

            return video_id
        elif 'youtu.be' in link:
            # Se o link for do formato youtu.be, extrai diretamente o restante da URL
            video_id = link.split('youtu.be/')[1]

            # Se houver outros parâmetros na URL, remove-os
            video_id = video_id.split('?')[0]

            return video_id
        else:
            return None  # Não é um link do YouTube
    except IndexError:
        return None  # Não foi possível extrair o ID do vídeo