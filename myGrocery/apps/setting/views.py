from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def index(request):
    from apps.setting.models import Setting
    data_grocery = Setting.objects.all()
    send_data_base = {"data_grocery": data_grocery}
    if request.method == 'POST':
        name_of_grocery = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        est_date = request.POST.get('est_date')
        website = request.POST.get('website')
        facebook = request.POST.get('facebook')

        save_in_db = Setting(name_of_grocery=name_of_grocery, address=address, email=email, est_date=est_date,
                             website=website, facebook=facebook, user=request.user)
        save_in_db.save()
        return redirect('/')
    return render(request, 'basics/setting/index.html', send_data_base)
