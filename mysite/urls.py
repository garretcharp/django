from django.urls import path, include

urlpatterns = [
    path('', include('mysite.content.index.urls')),
]
