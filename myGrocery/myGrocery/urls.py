"""myGrocery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/', include('apps.category.urls')),
    path('see_category/', include('apps.category.urls')),
    path('', include('apps.dashboard.urls')),
    path('product/', include('apps.product.urls')),
    path('manage_product/', include('apps.product.urls')),
    path('setting/', include('apps.setting.urls')),
    path('transaction/', include('apps.transaction.urls')),
    path('manage_transaction/', include('apps.transaction.urls')),
    path('user/', include('apps.user.urls')),
    path('login/', include('apps.login.urls')),
    path('logout/', include('apps.login.urls')),
    path('registration/', include('apps.login.urls')),
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)