from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('challenges/', views.challengeList, name='challenge-list'),
    path('myChallenges/', views.hosterMyChallenges, name='my-challenges'),
    path('challenge-detail/<int:id>/', views.challengeDetail, name='challenge-detail'),
    path('challenge-submissions/<int:id>/', views.viewChallengeSubmission, name='view-submissions'),
    path('review-submissions/<int:id>/', views.reviewSubmission, name='review-submissions'),
    path('challenge-update/<int:id>/', views.challengeUpdate, name='challenge-update'),
    path('challenge-delete/<int:id>/', views.challengeDetail, name='challenge-delete'),
    path('create-challenge/', views.CreateChallenge, name='create-challenge'),
    path('submitchallenge/<int:id>', views.challengeSubmission, name='challenge-submission'),

]
