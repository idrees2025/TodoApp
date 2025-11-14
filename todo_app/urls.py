from django.urls import path
from todo_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.createtodo_view,name='create'),
    path('register/',views.Register_view.as_view(),name='register'),
    path('login/',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('profile/',views.myprofile_view.as_view(),name='profile'),
    path('foryou/',views.foryou_view.as_view(),name='foryou'),
    path('detail/<int:pk>/',views.detail_view.as_view(),name='detail'),
    path('edit/<int:required_id>/',views.edit_view,name='edit'),
    path('delete/<int:required_id>/',views.delete_view,name='delete')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
