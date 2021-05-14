from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from apps.user.forms import UpdateUser
from json import dumps


@login_required(login_url='/login/')
def index(request):
    current_user = request.user

    return redirect('/user/update')
    # return render(request, 'basics/user/index.html')


def update(request):
    from apps.setting.models import Setting
    data_grocery = Setting.objects.all()
    current_user = request.user
    item = User.objects.get(id=current_user.id)
    # send_data = {"user_data": item}
    updateForm = UpdateUser(instance=item)
    if request.method == 'POST':
        update_data = UpdateUser(request.POST, instance=item)
        if update_data.is_valid():
            update_data.save()
            # messages.success(request, 'Data has been updated.')
            return redirect('/user/update/')
    return render(request, 'basics/user/index.html',
                  {
                      'form': updateForm,
                      'item': item,
                      "data_grocery": data_grocery
                  })
