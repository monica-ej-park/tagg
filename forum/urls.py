from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.get_list, name="list"),
    path('list/view/', views.get_most_view_list, name='most_view_list'), 
    path('list/like/', views.get_most_like_list, name='most_like_list'), 
    path('list/me/', views.get_list_by_me, name='list_by_me'), 
    path('list/tag/<str:tag>/', views.get_list_by_tag, name='list_by_tag'),
    path('search/', views.search, name='search'),
    path('thread/<int:data_id>/', views.view_detail, name='thread'),
    path('modify/<int:data_id>/', views.modify, name="modify"), 
    path('write/', views.write, name="write"), 
    path('rank/', views.get_tag_rank, name='tag_rank'),
    path('like/<int:data_id>/<str:value>/', views.like, name='like'),
    path('reply/<int:data_id>', views.reply, name='reply'),
    
]
