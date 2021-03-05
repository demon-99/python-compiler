from django.conf.urls import url
from codestar import views

urlpatterns = [
	url('',views.greetings),
    url('home/run',views.runcode),
]
