from django.urls import include, path
from .views import ( CustomAuthToken, LogoutView, StudentOnlyView, StudentSignupView, TmOnlyView, TmSignupView)
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'shedule', views.SheduleViewSet, basename='shedule')
router.register(r'session', views.SessionViewSet, basename='session')


urlpatterns=[
    path('shedule/',include(router.urls)),

    path('signup/tm/', TmSignupView.as_view()),
    path('signup/student/', StudentSignupView.as_view()),
    path('login/', CustomAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('tm/dashboard/', TmOnlyView.as_view(), name='tmdashboard'),
    path('student/dashboard/', StudentOnlyView.as_view(), name='studentdashboard'),
]