import os
from django.conf import settings
from django.http import HttpResponse, Http404
from mimetypes import guess_type  # Usado para identificar o tipo do arquivo

def download_image(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    
    if os.path.exists(file_path):
        # Determina o tipo de conteúdo com base na extensão do arquivo (JPG, PNG, etc.)
        content_type, _ = guess_type(file_path)
        if content_type is None:
            content_type = 'application/octet-stream'  # Tipo padrão se o MIME não for identificado

        # Prepara a resposta para download
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type=content_type)
            response['Content-Disposition'] = f'attachment; filename="{filename}"'

            # Exclui o arquivo após o download ser iniciado
            os.remove(file_path)
            return response
    else:
        raise Http404("Arquivo não encontrado")
