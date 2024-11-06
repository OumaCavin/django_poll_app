# To access view.py  in a browser, we need to map it to a URL - and for this we need to define a URL configuration,
# to configure the global URLconf in the mysite project to include the URLconf defined in polls.urls.

# poll_app/poll/urls.py¶

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('service/', views.service, name='service'),  # Service page
    path('blog/', views.blog, name='blog'),  # Blog page
    path('faq/', views.faq, name='faq'),  # Faq page
]


