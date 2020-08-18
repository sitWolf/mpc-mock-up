from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = "demomodules"

urlpatterns = [
    path("1", views.ModuleOneView.as_view(), name="one"),
    path("2", views.ModuleTwoView.as_view(), name="two"),
    path("3", views.ModuleThreeView.as_view(), name="three"),
    path("4", views.ModuleFourView.as_view(), name="four"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


