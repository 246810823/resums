from django.urls import path
from . import views



urlpatterns = [
            path('',views.createprofile, name='create'),
            path('listdetails/', views.listdetails, name='details'),
            path('updatedetails/<int:p_id>/', views.updatedetails, name='update'),
            path('deletedetails/<int:p_id>/', views.deletedetails, name='delete')



]