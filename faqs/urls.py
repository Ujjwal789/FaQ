from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='home'),
    path('list/', views.faq_list, name='faq-list'),
    path('page/', views.faq_page, name='faq-page'),
    path('submit/', views.submit_faq, name='faq-submit'),
    path('faqs/success/', views.faq_success, name='faq-success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)