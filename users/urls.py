from django.conf.urls import url
from users.views import all_users, user

app_name = 'users'


urlpatterns = [
    url(r'^(\d+)/$', user, name='user'),
    url(r'^$', all_users, name='all_users')
]