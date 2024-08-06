from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image

def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery:image_list')
    else:
        form = ImageForm()
    return render(request, 'gallery/image_upload.html', {'form': form})

def image_list_view(request):
    images = Image.objects.all()
    return render(request, 'gallery/image_list.html', {'images': images})
