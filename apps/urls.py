from django.urls import path
from .views import contact_view, main_page

urlpatterns = [
    path('', main_page, name='main_page'),
    path('contact/', contact_view, name='contact_view'),
]
