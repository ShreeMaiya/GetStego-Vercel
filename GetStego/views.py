from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from algorithms.encode import encode_lsb_audio, decode_lsb_audio
from algorithms.encode_video import encode_lsb_video, decode_lsb_video
from algorithms.encode_img import encode_lsb_image, decode_lsb_image
from django.http import HttpResponse
import os
import tempfile

def my_view(request):
    return render(request, 'index.html')

def handle_uploaded_file(file):
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(file.read())
    temp_file.close()
    return temp_file.name

def encode_audio_view(request):
    if request.method == 'POST':
        try:
            audio_file = request.FILES['audio_file']
            message = request.POST['message']
            audio_file_path = handle_uploaded_file(audio_file)
            zip_file_path = encode_lsb_audio(audio_file_path, message)
            os.remove(audio_file_path)  # Delete the temporary file
            response = HttpResponse(content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(zip_file_path)}"'
            with open(zip_file_path, 'rb') as file:
                response.write(file.read())
            return response
        except Exception as e:
            return render(request, 'error.html')
    return render(request, 'encode.html')

def decode_audio_view(request):
    if request.method == 'POST':
        try:
            encoded_audio_file = request.FILES['encoded_audio_file']
            key = request.POST['key']
            encoded_audio_file_path = handle_uploaded_file(encoded_audio_file)
            message = decode_lsb_audio(encoded_audio_file_path, key)
            os.remove(encoded_audio_file_path)  # Delete the temporary file
            return render(request, 'decode.html', {'message': message})
        except Exception as e:
            return render(request, 'error.html')
    return render(request, 'decode.html')

def encode_audio_remake_view(request):
    if request.method == 'POST':
        try:
            audio_file = request.FILES['audio_file']
            message = request.POST['message']
            audio_file_path = handle_uploaded_file(audio_file)
            zip_file_path = encode_lsb_audio(audio_file_path, message)
            os.remove(audio_file_path)  # Delete the temporary file
            response = HttpResponse(content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(zip_file_path)}"'
            with open(zip_file_path, 'rb') as file:
                response.write(file.read())
            return response
        except Exception as e:
            return render(request, 'error.html')
    return render(request, 'encode_remake.html')

def decode_audio_remake_view(request):
    if request.method == 'POST':
        try:
            encoded_audio_file = request.FILES['encoded_audio_file']
            key = request.POST['key']
            encoded_audio_file_path = handle_uploaded_file(encoded_audio_file)
            message = decode_lsb_audio(encoded_audio_file_path, key)
            os.remove(encoded_audio_file_path)  # Delete the temporary file
            return render(request, 'decode_remake.html', {'message': message})
        except Exception as e:
            return render(request, 'error.html')
    return render(request, 'decode_remake.html')

def encode_video_view(request):
    if request.method == 'POST':
        try:
            video_file = request.FILES['video_file']
            message = request.POST['message']
            video_file_path = handle_uploaded_file(video_file)
            zip_file_path = encode_lsb_video(video_file_path, message)
            os.remove(video_file_path)  # Delete the temporary file
            response = HttpResponse(content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(zip_file_path)}"'
            with open(zip_file_path, 'rb') as file:
                response.write(file.read())
            return response
        except Exception as e:
            return render(request, 'error.html')
    return render(request, 'encode_video.html')

def decode_video_view(request):
    if request.method == 'POST':
        try:
            encoded_video_file = request.FILES['encoded_video_file']
            key = request.POST['key']
            encoded_video_file_path = handle_uploaded_file(encoded_video_file)
            message = decode_lsb_video(encoded_video_file_path, key)
            os.remove(encoded_video_file_path)  # Delete the temporary file
            return render(request, 'decode.html', {'message': message})
        except Exception as e:
            return render(request, 'error.html')
    return render(request, 'decode_video.html')

def encode_video_remake_view(request):
    if request.method == 'POST':
        try:
            video_file = request.FILES['video_file']
            message = request.POST['message']
            video_file_path = handle_uploaded_file(video_file)
            zip_file_path = encode_lsb_video(video_file_path, message)
            os.remove(video_file_path)  # Delete the temporary file
            response = HttpResponse(content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(zip_file_path)}"'
            with open(zip_file_path, 'rb') as file:
                response.write(file.read())
            return response
        except Exception as e:
            return render(request, 'error.html')
    return render(request, 'encode_video_remake.html')

def decode_video_remake_view(request):
    if request.method == 'POST':
        try:
            encoded_video_file = request.FILES['encoded_video_file']
            key = request.POST['key']
            encoded_video_file_path = handle_uploaded_file(encoded_video_file)
            message = decode_lsb_video(encoded_video_file_path, key)
            os.remove(encoded_video_file_path)  # Delete the temporary file
            return render(request, 'decode_video_remake.html', {'message': message})
        except Exception as e:
            return render(request, 'error.html')
    return render(request, 'decode_video_remake.html')

def encode_image_view(request):
    if request.method == 'POST':
        try:
            image_file = request.FILES['image_file']
            message = request.POST['message']
            image_file_path = handle_uploaded_file(image_file)
            zip_file_path = encode_lsb_image(image_file_path, message)
            os.remove(image_file_path)  # Delete the temporary file
            response = HttpResponse(content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(zip_file_path)}"'
            with open(zip_file_path, 'rb') as file:
                response.write(file.read())
            return response
        except Exception as e:
            return render(request, 'error.html')
    return render(request, 'encode_image.html')

def decode_image_view(request):
    if request.method == 'POST':
        try:
            encoded_image_file = request.FILES['encoded_image_file']
            key = request.POST['key']
            encoded_image_file_path = handle_uploaded_file(encoded_image_file)
            message = decode_lsb_image(encoded_image_file_path, key)
            os.remove(encoded_image_file_path)  # Delete the temporary file
            return render(request, 'decode.html', {'message': message})
        except Exception as e:
            return render(request, 'error.html')
    return render(request, 'decode.html')

def encode_image_remake_view(request):
    if request.method == 'POST':
        try:
            image_file = request.FILES['image_file']
            message = request.POST['message']
            image_file_path = handle_uploaded_file(image_file)
            zip_file_path = encode_lsb_image(image_file_path, message)
            os.remove(image_file_path)  # Delete the temporary file
            response = HttpResponse(content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(zip_file_path)}"'
            with open(zip_file_path, 'rb') as file:
                response.write(file.read())
            return response
        except Exception as e:
            return render(request, 'error.html')
    return render(request, 'encode_image_remake.html')

def decode_image_remake_view(request):
    if request.method == 'POST':
        try:
            encoded_image_file = request.FILES['encoded_image_file']
            key = request.POST['key']
            encoded_image_file_path = handle_uploaded_file(encoded_image_file)
            message = decode_lsb_image(encoded_image_file_path, key)
            os.remove(encoded_image_file_path)  # Delete the temporary file
            return render(request, 'decode_image_remake.html', {'message': message})
        except Exception as e:
            return render(request, 'error.html')
    return render(request, 'decode_image_remake.html')