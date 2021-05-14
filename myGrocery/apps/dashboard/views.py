from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def index(request):
    from apps.setting.models import Setting
    data_grocery = Setting.objects.all()
    send_data_base = {"data_grocery": data_grocery}
    return render(request, 'basics/dashboard/index.html',send_data_base)
