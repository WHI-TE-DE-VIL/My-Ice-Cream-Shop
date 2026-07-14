from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home_page'), # Keeps your clean homepage domain path
    
    path('sign_in/', views.signin, name='sign_in'),
    path('sign_up/', views.signup, name='sign_up'),
    path('menu/', views.menu, name='menu'),
    path('find_store/', views.findstore, name='find_store'),
    path('scoop/', views.scoop, name='scoop_detail'),
    path('ourstory/', views.ourstory, name='our_story'),
    path('locations/', views.locations, name='locations'),
    path('flavours/', views.flavours, name='flavours'),
    path('contact_us/', views.contactus, name='contact_us'),

    path('profile/', views.my_profile, name='profile'), # This will now safely handle the view execution
    path('logout/', views.logout_view, name='logout'),
]
