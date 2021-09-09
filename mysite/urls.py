from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView
from blog.sitemaps import PostSitemap
from blog.views import about_view, contact_view



sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
