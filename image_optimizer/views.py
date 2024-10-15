import os
from django.conf import settings
from django.shortcuts import render
from .forms import ImageUploadForm
from .optimizer import image_optimizer

def index(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['image']
            quality = form.cleaned_data['quality']
            scale = form.cleaned_data['scale']

            # Caminhos para a imagem original e otimizada
            input_file = os.path.join(settings.MEDIA_ROOT, image.name)
            output_file_name = f"optimized_{image.name}"
            output_file = os.path.join(settings.MEDIA_ROOT, output_file_name)

            # Certifique-se de que o diretório de mídia existe
            if not os.path.exists(settings.MEDIA_ROOT):
                os.makedirs(settings.MEDIA_ROOT)

            # Salva o arquivo de imagem original no disco
            with open(input_file, 'wb+') as f:
                for chunk in image.chunks():
                    f.write(chunk)

            # Otimiza a imagem
            image_optimizer(input_file, output_file, quality=quality, scale=scale, verbose=False)

            # Remove o arquivo original (não otimizado)
            os.remove(input_file)

            # Renderiza o template com o link de download
            optimized_image_url = f"/download/{output_file_name}"
            return render(request, 'image_optimizer/result.html', {
                'optimized_image': optimized_image_url,
                'optimized_image_name': output_file_name
            })
    else:
        form = ImageUploadForm()

    return render(request, 'image_optimizer/index.html', {'form': form})
