from background_task import background
from django.shortcuts import get_object_or_404

from .models import TempFile


@background(schedule=10)
def delete_temp_file(file_id):
    temp_file = get_object_or_404(TempFile, pk=file_id)
    temp_file.delete()
