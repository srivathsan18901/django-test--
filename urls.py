from django.urls import path
from .views import GoogleCalendarInitView, GoogleCalendarRedirectView

urlpatterns = [
    path('rest/v1/calendar/init/', GoogleCalendarInitView.as_view()),
    path('rest/v1/calendar/redirect/', GoogleCalendarRedirectView.as_view()),
]
