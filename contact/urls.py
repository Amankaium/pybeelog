from django.urls import path
from .views import FeedbackView, SubscribeView


urlpatterns = [
    path('', FeedbackView.as_view(), name='feedback_view'),
    path('c/', SubscribeView.as_view(), name='subscribe')
]



