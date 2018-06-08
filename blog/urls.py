"""
^ — beginning of text;
$ — ending of text;
\d — number;
+ — last element should be repeated at least once
() — get part of template
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # ^$ - start and end of string - empty URL
    # redirect to 'post_list' view method with name 'post_list'
    url(r'^$', views.post_list, name='post_list'),

    # ^post/ - starts with post/
    # (?P<pk>\d+) - takes everything and transfer to variable pk. can be only numbers
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),

    #regex: start with 'post/edit/',then primary key that should be at least one number, / and end($ - end)
    #in views - post_edit method with name 'post_edit'
    url(r'^post/edit/(?P<pk>\d+)/$', views.post_edit, name='post_edit')
]