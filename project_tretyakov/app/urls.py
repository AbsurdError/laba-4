from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.urls import path

urlpatterns = [
    path('', index),
    path('add/', add, name='add'),
    path('edit/', edit, name='edit'),
    path('delete/', delete, name='delete'),
    path('delete/<int:id>/', delete_choose, name='dishes_delete_choose'),
    path('edit/<int:id>/', edit_choose, name='dishes_edit_choose'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)