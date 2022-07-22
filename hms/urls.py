
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
    path("delete_room/<int:id>", views.delete_room_view, name="deleteRoom"),
    path("update_room/<int:id>", views.update_room_view, name="updateRoom"),
    path("add_room/", views.add_room_view, name="addRoom"),
    path("available_rooms/", views.available_rooms_view, name="availableRooms"),
    path("dirty_rooms/", views.dirty_rooms_view, name="dirtyRooms"),
    path("manage_reservation/", views.manage_reservation_view, name="manageReserve"),
    path("cancel_reservation/<int:id>", views.cancel_reservation_view, name="cancel"),
    path("process_select/", views.handle_ajax_request, name="processSelect"),
    path("add_reservation/", views.add_reservation_view, name="addReservation"),
    path("manage_checkin/", views.manage_checkin_view, name="manageCheckin"),
    path("checkout/<int:id>", views.checkout_view, name="checkout"),
    path("checkin/<int:id>", views.checkin_view, name="checkin"),
    path("add_checkin/", views.add_checkin_view, name="addCheckin"),
    path("view_checkin/", views.view_checkin_view, name="viewCheckin"),
]