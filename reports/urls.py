from django.conf.urls import url
from reports.views import all_categories, category, report

app_name = 'reports'

urlpatterns = [
    url(r'^$', all_categories, name='all_categories'),
    url(r'^(\d+)/$', category, name='category'),
    url(r'^report/(\d+)/$', report, name='report')
]