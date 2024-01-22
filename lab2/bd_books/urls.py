from django.urls import path
from . import views
from .views import books_home, CartUser

urlpatterns = [
   path('', books_home.as_view(), name='books_home'),
   path('book/<int:book_id>/', views.show_book, name='book_page'),
   path('cart', CartUser.as_view(), name='cart'),
]
