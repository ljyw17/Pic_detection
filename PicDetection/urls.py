from django.conf.urls import url
from django.contrib import admin
import img_db.views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
urlpatterns = [
    url(r'^index/static/(?P<path>.*)$', serve, {'document_root':'F:\PicUpload\img_db\static'}),
    url(r'^admin/', admin.site.urls),
    # url(r'^upload', img_db.views.uploadImg),
    url(r'^localdetect', img_db.views.localDetect),
    url(r'^home', img_db.views.homeIndex),
    url(r'^crawldetect', img_db.views.crawlDetect),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)