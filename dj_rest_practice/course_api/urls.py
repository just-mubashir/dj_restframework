from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from app.views import courseListView , courseDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include,('app.urls')),
    path('api/courses', courseListView),
    path('api/courses/<int:pk>', courseDetailView)
    
]
