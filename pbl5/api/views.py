from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse
from .models import hr
import random
import datetime

@csrf_exempt
def show_chart(request):
    return render(request, 'show.html', {})

def get_chart(request):
    value = random.randint(0, 100)
    hr_temp = hr.objects.all()
    id = 0
    if hr_temp.count() != 0:
        id = hr.objects.latest('id').id + 1
        if hr_temp.count() >= 30:
            hr_temp.delete()

    hr_object = hr.objects.create(
        id = id,
        value = value,
        date_posting = datetime.datetime.now()  
    )
    hr_object.save()
    return JsonResponse({'value': value})

def delete_record(request, id):
    hr_object = hr.objects.get(id = id)
    hr_object.delete()
    return redirect('show_chart')

def get_data(request):
    hr_temp = hr.objects.all()
    post_list = serializers.serialize('json', hr_temp)
    return HttpResponse(post_list, content_type="text/json-comment-filtered")

def get_data_detail(request,id):
    hr_temp = hr.objects.filter(id=id)
    post_list = serializers.serialize('json', hr_temp)
    return HttpResponse(post_list, content_type="text/json-comment-filtered")

