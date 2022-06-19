from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('blog/', blog , name = 'blog'),
    path('resume/', resume , name = 'resume'),
    path('about/', about , name = 'about'),
    path('create-post/', CreatePost.as_view() , name = 'create-post'),
    path('update-resume/<int:id>/', update_resume, name ='update-resume'),
    path('update-about/<int:id>/', update_about, name ='update-about'),
    path('delete-post/<int:pk>/', DeltePost.as_view(), name ='delete-post'),
    path('update-post/<int:pk>/', UpdatePost.as_view(), name ='update-post'),
    path('reply/<int:id>/', reply_view , name = 'reply'),
    path('detail/<int:id>', post_detail_view, name = 'detail')
]