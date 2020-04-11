from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from books.views import *

#To call a view you need to map it to a URL, this is where you put your URLConfigs
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:title>', views.bookDetails, name='bookDetails'),
    #C.R. Urls
    path('topseller/', views.book_top_seller, name= 'book_top_seller' ),
    path('genre/<str:gname>/', views.book_genre, name= 'book_genre'),
    path('rating/<int:filter>/', views.book_rating, name= 'book_rating' ),
    path('ordering/<int:filter>/', views.book_order, name= 'book_order' ),
    #C.S. Urls
    path('add_to_cart/<item_id>', views.add_to_cart, name='add_to_cart'),
    path('order_summary/', views.order_details, name='order_summary'),
    path('item/delete/<item_id>', views.delete_from_cart, name='delete_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('add-quantity-from-cart/<item_id>', views.add_quantity_from_cart, name='add_quantity_from_cart'),
    path('reduce-quantity-from-cart/<item_id>', views.reduce_quantity_from_cart, name='reduce_quantity_from_cart'),
    path('save-item/<item_id>', views.save_item, name='save_item'),
    path('add-back-item/<item_id>', views.add_back_item, name='add_back_item'),
    path('booklist/',views.index, name='booklist'),
    path('author-list/<author>' , views.author_book_list, name='author_book_list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

