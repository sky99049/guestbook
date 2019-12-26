from django.urls import path
from django.views.generic import RedirectView
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', MessageList.as_view(), name='msg_lis'),
    path('<int:pk>/', MessageDetail.as_view(), name='msg_view'),
    path('create/', MessageCreate.as_view(), name='msg_create'),
    path('message/<int:pk>/delete/', MessageDelete.as_view()),
]
