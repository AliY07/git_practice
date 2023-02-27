from django.urls import path
from accounts import views
from .views import SignUpView
from .import views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("first_page/",views.first_page,name="first_page"),
    path("products/",views.products,name="products"),
    path("deals/",views.deals,name="deals"),
    path("stores/",views.stores,name="stores"),
    path("contact/", views.contact, name="contact"),
]
