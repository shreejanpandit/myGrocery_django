from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.category.models import Category
from apps.product.models import Product
from apps.transaction.models import Transaction


@login_required(login_url='/login/')
def create(request):
    if request.method == 'POST':
        id_cat = request.POST.get('category')
        category_id = Category.objects.get(id=id_cat)
        id_prod = request.POST.get('product')
        print(id_prod)
        product_id = Product.objects.get(id=id_prod)
        quantity = request.POST.get('quantity')
        total_price = 0

        save_in_db = Transaction(category=category_id, product=product_id, quantity=quantity, totalPrice=total_price)
        save_in_db.save()
        return redirect('/transaction/show_prod_cat/')
    return redirect('/transaction/show_prod_cat')


@login_required(login_url='/login/')
def manage(request):
    from apps.setting.models import Setting
    data_grocery = Setting.objects.all()
    trans_data = Transaction.objects.all()
    send_data = {"trans_data": trans_data,"data_grocery": data_grocery}
    return render(request, 'basics/transaction/manage_transaction.html', send_data)


def see_product_category(request):
    from apps.setting.models import Setting
    data_grocery = Setting.objects.all()
    product_data = Product.objects.all()
    category_data = Category.objects.all()
    transaction_data = Transaction.objects.all()
    send_data = {"product_data": product_data, "category_data": category_data, "transaction_data": transaction_data,
                 "data_grocery": data_grocery}
    return render(request, 'basics/transaction/add_transaction.html', send_data)


def delete(request, pk):
    data = Transaction.objects.get(id=pk)
    data.delete()
    return redirect('/manage_transaction/')
