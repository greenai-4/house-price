"""
URL configuration for housing_prediction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from prediction.views import house,calc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', house), #根路徑指向house
    # path('', include('prediction.urls')),  # 包含应用的 URL 路由
    path('house', house),
    path('test', calc),
    
]

