from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stdapp.urls')),  # Ensure 'myapp' is replaced with the name of your app
]
