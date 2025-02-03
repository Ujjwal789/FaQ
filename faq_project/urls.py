from django.contrib import admin
from django.urls import path, include
from faqs.views import homepage, faq_page 
from django.conf import settings
from django.conf.urls.static import static
from faqs import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('faqs/', include('faqs.urls')),  # Includes the URLs from faqs app
    path('', homepage),  # Homepage path
    path('page/', faq_page, name='faq-page'),  # FAQ page path
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
