from django.urls import path
from .views import RegisterView, LoginView, TrainingListView, UserTrainingListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('trainings/', TrainingListView.as_view(), name='training-list'),
    path('my-trainings/', UserTrainingListView.as_view(), name='my-trainings'),
]
