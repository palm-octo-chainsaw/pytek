from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    ProductDetailView,
    home
)

app_name='pytek'

urlpatterns = [
    path('', home, name='index'),
    path('details/<slug>/', ProductDetailView.as_view(), name='details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
