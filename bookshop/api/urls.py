from .views import UserView, BookView, TransactionView
from django.urls import path

urlpatterns = [
    path('user/', UserView.as_view()),
    path('book/', BookView.as_view()),
    path('transaction/', TransactionView.as_view()),
    
]
