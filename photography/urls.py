from unicodedata import name
from django.urls import path
from .views import AboutPageView, ContactPageView, HomePageView, PhotoListView, PhotoDetailView

app_name = 'photography'

urlpatterns = [
    # Home Page.
    path('', HomePageView.as_view(), name='home'),
    # Collection of images page.
    path('photo/collection/', PhotoListView.as_view(), name='list'),
    # Detail view of each photo.
    path('photo/detail/', PhotoDetailView.as_view(), name= 'detail'),
    # About me page.
    path('About/', AboutPageView.as_view(), name='about'),
    # Contact page.
    path('Contact/', ContactPageView.as_view(), name='contact'),
]