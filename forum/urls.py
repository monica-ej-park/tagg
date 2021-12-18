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
    path('delete/<int:data_id>/', views.delete, name="delete"), 
    path('modify/<int:data_id>/', views.modify, name="modify"), 
    path('write/', views.write, name="write"), 
    path('rank/', views.get_tag_rank, name='tag_rank'),
    path('like/<int:data_id>/<str:value>/', views.like, name='like'),
    path('reply/<int:data_id>/', views.reply, name='reply'),
    path('reply2/<int:data_id>/<int:reply_id>/', views.save_modified_reply, name='save_modified_reply'),
    path('modify_reply/<int:data_id>/<int:reply_id>/', views.modify_reply, name='modify_reply'),
    path('delete_reply/<int:data_id>/<int:reply_id>/', views.delete_reply, name='delete_reply'),
    
]
