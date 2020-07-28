from django.shortcuts import render
from .forms import ImageForm,Image_DimensionsForm
from .models import Image_M
from PIL import Image
from skimage import io
from skimage.transform import rescale, resize, downscale_local_mean

def home(request):
    images = Image_M.objects.all()
    image_list = []
    for image in images:
        image_list.append(image)
    if len(image_list) > 0:
        return render(request, "home.html", {'image_list': image_list,'var':len(image_list)})
    else:
        return render(request, "home.html", {'image_list': image_list,'var':0})


def image_upload_view(request):
    """Process images uploaded by users"""
    print("qwertyi")
    if request.method == 'POST':
        form0 = Image_DimensionsForm()
        form1 = ImageForm(request.POST, request.FILES)
        if request.POST.get('image') == '' and request.POST.get('image_url') == '':
            return render(request, 'Error.html')
        else:
            if form1.is_valid():
                global ReadedImage 
                ReadedImage = form1.instance
                form1.save()
                # Get the current instance object to display in the template
                img_obj = form1.instance
                return render(request, 'uploaded_image.html', {'form': form0, 'img_obj': img_obj})
            

    else:
        form = ImageForm()
    return render(request, 'image_upload.html', {'form': form})

def image_update_view(request):
    """Process images uploaded by users"""
    print("qwertyi")
    if request.method == 'POST':
        form2 = Image_DimensionsForm(request.POST, request.FILES)
        #im = request.POST.get('adf')
        im = ReadedImage
        if form2.is_valid():
            dimns = form2.instance
            width = dimns.width
            height = dimns.height
            ReadedImage.width = width
            ReadedImage.height = height
            ReadedImage.save()
            #image = Image.objects.create(title='ad',height=height,width=width,image=im)
            # Get the current instance object to display in the template
            return render(request, 'updated_image.html', {'form': form2, 'width': width,'height': height, 'image_obj': im})
    else:
        form = ImageForm()
    return render(request, 'image_upload.html', {'form': form})

def image_view(request,image_title):
    images = Image_M.objects.all()
    for image in images:
        if image.title == image_title:
            return render(request, "image_view.html", {'img_obj': image})





