from django.urls import path
from django.contrib.auth import views
from Account.views import PostList, PostCreate, PostUpdate, PostDelete, Profile, Login

app_name = 'account'
urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
  # path(
  #     "password_change/", views.PasswordChangeView.as_view(), name="password_change"
  # ),
  # path(
  #     "password_change/done/",
  #     views.PasswordChangeDoneView.as_view(),
  #     name="password_change_done",
  # ),
  # path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
  # path(
  #     "password_reset/done/",
  #     views.PasswordResetDoneView.as_view(),
  #     name="password_reset_done",
  # ),
  # path(
  #     "reset/<uidb64>/<token>/",
  #     views.PasswordResetConfirmView.as_view(),
  #     name="password_reset_confirm",
  # ),
  # path(
  #     "reset/done/",
  #     views.PasswordResetCompleteView.as_view(),
  #     name="password_reset_complete",
  # ),
]

urlpatterns += [
    path('', PostList.as_view(), name='home'),
    path('Post/Create', PostCreate.as_view(), name='post-create'),
    path('Post/Update/<int:pk>', PostUpdate.as_view(), name='post-update'),
    path('Post/Delete/<int:pk>', PostDelete.as_view(), name='post-delete'),
    path('Profile/', Profile.as_view(), name='profile'),
]
