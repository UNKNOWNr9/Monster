from django.urls import path
from django.contrib.auth import views
from Account.views import PostList, PostCreate, PostUpdate, PostDelete, Profile


app_name = 'account'

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('Post/Create', PostCreate.as_view(), name='post-create'),
    path('Post/Update/<int:pk>', PostUpdate.as_view(), name='post-update'),
    path('Post/Delete/<int:pk>', PostDelete.as_view(), name='post-delete'),
    path('Profile/', Profile.as_view(), name='profile'),
]
