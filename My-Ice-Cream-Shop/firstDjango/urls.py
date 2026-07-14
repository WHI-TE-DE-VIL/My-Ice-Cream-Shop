from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    # Admin interface route
    path('admin/', admin.site.urls),

    # Core structural base routes
    path('', views.home, name='home_page'),
    path('profile/', views.my_profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),

    # Authentication routes
    path('sign_in/', views.signin, name='sign_in'),
    path('sign_up/', views.signup, name='sign_up'),

    # Store front & informational content routes
    path('menu/', views.menu, name='menu'),
    path('find_store/', views.findstore, name='find_store'),
    path('scoop/', views.scoop, name='scoop_detail'),
    path('ourstory/', views.ourstory, name='our_story'),
    path('locations/', views.locations, name='locations'),
    path('flavours/', views.flavours, name='flavours'),
    path('contact_us/', views.contactus, name='contact_us'),
]
