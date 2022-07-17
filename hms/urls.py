
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("staff_mgt/", views.manage_staff_view, name="staffMgt"),
    path("update_staff/<int:id>", views.update_staff_view, name="updateStaff"),
    path("delete_staff/<int:id>", views.delete_staff_view, name="deleteStaff"),
    path("add_staff/", views.add_staff_view, name="addStaff"),
    path("access_mgt/", views.access_mgt_view, name="accessMgt"),
    path("grant_access/<int:id>", views.grant_access_view, name="grant"),
    path("revoke_access/<int:id>", views.revoke_access_view, name="revoke"),
    path("room_mgt/", views.manage_room_view, name="roomMgt"),
]