# # To access view.py  in a browser, we need to map it to a URL - and for this we need to define a URL configuration,
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # The root path within the polls app
]


# # Option 2:
# # to configure the global URLconf in the mysite project to include the URLconf defined in polls.urls.
# from django.contrib import admin
# from django.urls import include, path
#
# urlpatterns = [
#     path("polls/", include("polls.urls")),
#     path("admin/", admin.site.urls),
# ]

# # Fix Option 3:
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path("", views.index, name="index"),
# ]
