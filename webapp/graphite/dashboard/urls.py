from django.conf.urls.defaults import *

urlpatterns = patterns('graphite.dashboard.views',
  ('^save/(?P<name>[^/]+)', 'save'),
  ('^load/(?P<name>[^/]+)', 'load'),
  ('^delete/(?P<name>[^/]+)', 'delete'),
  ('^create-temporary/?', 'create_temporary'),
  ('^email', 'email'),
  ('^find/', 'find'),
  ('^save_template/(?P<name>[^/]+)', 'save_template'),
  ('^load_template/(?P<name>[^/]+)/(?P<host_id>[^/]+)', 'load_template'),
  ('^delete_template/(?P<name>[^/]+)', 'delete_template'),
  ('^find_template/', 'find_template'),
  ('^list_hosts/', 'list_hosts'),
  ('^help/', 'help'),
  ('^(?P<name>[^/]+)/(?P<host_id>[^/]+)', 'template'),
  ('^(?P<name>[^/]+)', 'dashboard'),
  ('', 'dashboard'),
)
