from django.conf import settings
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_view, name='contact'),
]

# Add Debug Toolbar URLs if DEBUG is True
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]