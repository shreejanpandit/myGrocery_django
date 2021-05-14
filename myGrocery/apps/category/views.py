from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.category.models import Category
from apps.category.forms import UpdateCategory


@login_required(login_url='/login/')  # redirect when user is not logged in
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        remarks = request.POST.get('description')
        save_in_db = Category(name=name, remarks=remarks)
        save_in_db.save()

        data = Category.objects.all()
        print(data)
        category = {"data": data}
        return render(request, 'basics/category/index.html', category)

    return redirect('/see_category/cat/')


def see_category(request):
    from apps.setting.models import Setting
    data_grocery = Setting.objects.all()
    data = Category.objects.all()
    category = {"data": data,"data_grocery": data_grocery}
    return render(request, 'basics/category/index.html', category)


def delete(request, pk):
    # return HttpResponse("I am deleting you")
    data = Category.objects.get(id=pk)
    data.delete()
    return redirect('/see_category/cat/')


def update(request, pk):
    item = Category.objects.get(id=pk)
    updateForm = UpdateCategory(instance=item)
    if request.method == 'POST':
        update_data = UpdateCategory(request.POST, instance=item)
        if update_data.is_valid():
            update_data.save()
            # messages.success(request, 'Data has been updated.')
            return redirect('/see_category/cat/')
    return render(request, 'basics/category/edit.html', {
        'form': updateForm,
        'item': item
    })
