"""firststudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blogapp.views
import polls.views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.index, name='index'),
    path('blogMain/', blogapp.views.blogMain, name='blogMain'),
    path('blogMain/createBlog/', blogapp.views.createBlog, name='createBlog'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blogMain/detail/<int:blog_id>/', blogapp.views.detail, name='detail'),

    path('oauth/', blogapp.views.oauth, name='oauth'),
    path('signup/', blogapp.views.signup, name='signup'),
    path('signin/', blogapp.views.signin, name='signin'),

    path('polls/', polls.views.IndexView.as_view(), name='polls'),

    path('polls/<int:pk>/', polls.views.DetailsView.as_view(), name='pdetail'),
    path('polls/<int:pk>/results/', polls.views.ResultView.as_view(), name='results'),
    path('polls/<int:pk>/vote/', polls.views.vote, name='vote'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

