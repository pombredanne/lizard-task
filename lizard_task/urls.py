# (c) Nelen & Schuurmans.  GPL licensed, see LICENSE.txt.
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin

from lizard_ui.urls import debugmode_urlpatterns

from lizard_task.views import TasksView
from lizard_task.views import TaskDetailView

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    url(r'^$',
        TasksView.as_view(),
        name='lizard_task_home'),
    url(r'^(?P<task_id>\d+)/$',
        TaskDetailView.as_view(),
        name='lizard_task_detail'),
    )
urlpatterns += debugmode_urlpatterns()
