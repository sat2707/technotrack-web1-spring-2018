from django.conf.urls import url
from reports.views import all_categories

urlpatterns = [
    url(r'^$', all_categories, name='main')
]
