import os
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Directory where files will be uploaded
UPLOAD_DIR = '/home/sam/WebUploads'

def upload_file(request):
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)  # Ensure the directory exists

    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        fs = FileSystemStorage(location=UPLOAD_DIR)
        fs.save(file.name, file)

    # List files and folders in UPLOAD_DIR
    file_list = os.listdir(UPLOAD_DIR)

    return render(request, 'upload.html', {'file_list': file_list, 'upload_dir': UPLOAD_DIR})
