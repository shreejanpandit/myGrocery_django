from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.category.models import Category
from apps.product.models import Product
from apps.product.forms import UpdateProduct


@login_required(login_url='/login/')
def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        id_cat = request.POST.get('category')
        category_id = Category.objects.get(id=id_cat)
        total_scale = request.POST.get('total_scale')
        unit_price = request.POST.get('unit_price')
        buy_price = request.POST.get('buy_price')
        msrp = request.POST.get('msrp')
        product_code = request.POST.get('product_code')
        quantity_in_scale = request.POST.get('quantity_in_scale')
        description = request.POST.get('description')
        save_in_db = Product(name=name, categoryID=category_id, totalScale=total_scale, unitPrice=unit_price,
                             buyPrice=
                             buy_price, msrp=msrp, totalPrice=float(total_scale) * float(unit_price),
                             productCode=product_code,
                             quantityInScale=quantity_in_scale,
                             quantityInStock=quantity_in_scale, description=description)
        save_in_db.save()
        # return render(request, 'basics/product/manage_product.html')
        return redirect('/product/show_manage')
    return redirect('/product/show')


@login_required(login_url='/login/')
def manage(request):
    return redirect('/product/show_manage')


def see_category(request):
    data = Category.objects.all()
    from apps.setting.models import Setting
    data_grocery = Setting.objects.all()
    category = {"data": data,"data_grocery": data_grocery}
    return render(request, 'basics/product/add_product.html', category)


def see_product(request):
    product_data = Product.objects.all()
    from apps.setting.models import Setting
    data_grocery = Setting.objects.all()
    product = {"product_data": product_data,"data_grocery": data_grocery}
    return render(request, 'basics/product/manage_product.html', product)


def delete(request, pk):
    data = Product.objects.get(id=pk)
    data.delete()
    return redirect('/product/show_manage')


def update(request, pk):
    item = Product.objects.get(id=pk)
    updateForm = UpdateProduct(instance=item)
    if request.method == 'POST':
        update_data = UpdateProduct(request.POST, instance=item)
        if update_data.is_valid():
            update_data.save()
            # messages.success(request, 'Data has been updated.')
            return redirect('/product/show_manage')
    return render(request, 'basics/product/edit.html', {
        'form': updateForm,
        'item': item
    })
