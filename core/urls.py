from django.urls import path
from .views import ClienteList, ClienteCreate, ClienteUpdate, ClienteDetail, ClienteDelete
from django.conf.urls.static import static
from django.conf import settings

app_name = 'core' 

urlpatterns = [
    path('', ClienteList.as_view(), name='list'), 
    path('create/', ClienteCreate.as_view(), name='create'),
    path('update/<int:pk>', ClienteUpdate.as_view(), name='update'),
    path('detail/<int:pk>', ClienteDetail.as_view(), name='detail'),
    path('delete/<int:pk>', ClienteDelete.as_view(), name='delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    