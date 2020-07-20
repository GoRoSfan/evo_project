from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import View

from .forms import TempFileForm
from .models import TempFile
from .tasks import delete_temp_file


# Create your views here.


class TempFileView(View):

    def get(self, request):
        pk = request.GET.get('file_id', -1)

        temp_file = get_object_or_404(TempFile, pk=pk)

        is_file_alive = timezone.now() - temp_file.upload_time < temp_file.life_time
        if is_file_alive:
            temp_file_url = temp_file.file.url
            return JsonResponse({'file': temp_file_url}, status=200)
        return JsonResponse({'data': ''}, status=404)

    def post(self, request):

        form = TempFileForm(request.POST, request.FILES)

        if form.is_valid():
            temp_file = form.save()

            delete_temp_file(temp_file.id, schedule=temp_file.life_time.seconds)

            response_data = {'file_id': temp_file.id}

            return JsonResponse(response_data)
        return JsonResponse({'data': ''}, status=404)


class ListTempFileView(View):

    def get(self, request):
        queryset = TempFile.objects.filter(upload_time__gt=timezone.now() - F('life_time'))

        response_queryset = list(queryset.values())
        for i in range(len(response_queryset)):
            response_queryset[i]['end_time'] = queryset[i].upload_time + queryset[i].life_time
        return JsonResponse({'data': response_queryset}, status=200)
