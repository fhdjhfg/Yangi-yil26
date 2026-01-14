from django.urls import path
from.views import CategoryListApiView

urlpatterns=[
    path("categories/list",CategoryListApiView.as_view()),
    path("caregories/list/<int:pk>/", CategoryListApiView.as_view())
]