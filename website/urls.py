from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('works', WorksView.as_view(),name="works"),
    path('works/<int:pk>', WorkDetailView.as_view(), name="work_detail"),
    path('crafts', CraftsView.as_view(), name="crafts"),
    path('crafts/<int:pk>', CraftDetailView.as_view(), name='craft_detail'),
    path('contact', ContactView.as_view(), name='contact'),
]