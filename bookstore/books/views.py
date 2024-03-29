from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
# C.S. imports
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import F
from datetime import date
import random
import string
import datetime
from .models import Book, Genre, Author, Order, OrderItem
from users.models import Profile
from django import forms
from django.http import HttpResponseRedirect

# S.T. views for home page and book details pages


def nonUser(request):
    allBook = Book.objects.all()
    return render(request, 'BookDetails/index.html', {'Booklist': allBook})


def author_book_list(request, author):
    try:
        athing = Author.objects.get(id=author)
    except Author.DoesNotExist:
        athing = None
    Books = Book.objects.filter(author=athing)
    # C.R. added this to all methods to allow pagination
    paginate_by = request.GET.get('paginate_by', 10)
    paginator = Paginator(Books, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # C.R. added this to get a list of genre objects
    genre_list = Genre.objects.all()

    # sorted_list = cache.get('sorted_list')
    # if not sorted_list:

    sorted_list = [books.id for books in Books]
    request.session['export_querset'] = sorted_list

    context = {
        'Book': Books,
        'page_obj': page_obj,
        'genre_list': genre_list,
    }
    # C.S. edits to index
    if not request.user.is_authenticated:
        return render(request, 'BookDetails/index.html', context)
    else:
        filtered_orders = Order.objects.filter(owner=request.user.profile)
        current_order_products = []
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [
                product.product for product in user_order_items]

        context = {
            'Book': Books,
            'page_obj': page_obj,
            'genre_list': genre_list,
            'current_order_products': current_order_products
        }
        return render(request, "BookDetails/index.html", context)

# C.S. added this


def index(request):
    Books = Book.objects.all()
    paginate_by = request.GET.get('paginate_by', 10)
    paginator = Paginator(Books, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    genre_list = Genre.objects.all()

    sorted_list = [books.id for books in Books]
    request.session['export_querset'] = sorted_list

    context = {
        'Book': Books,
        'page_obj': page_obj,
        'genre_list': genre_list,
    }
    # C.S. edits to index
    if not request.user.is_authenticated:
        return render(request, 'BookDetails/index.html', context)
    else:
        filtered_orders = Order.objects.filter(owner=request.user.profile)
        current_order_products = []
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [
                product.product for product in user_order_items]

        context = {
            'Book': Books,
            'page_obj': page_obj,
            'genre_list': genre_list,
            'current_order_products': current_order_products,
        }
        return render(request, "BookDetails/index.html", context)

# C.R. added pagination, browsing and sorting functions

# C.R. method to browse by genre


def book_genre(request, gname):
    Books = Book.objects.filter(genre__name=gname)
    paginate_by = request.GET.get('paginate_by', 10)
    paginator = Paginator(Books, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    genre_list = Genre.objects.all()

    sorted_list = [books.id for books in Books]
    request.session['export_querset'] = sorted_list

    context = {
        'Book': Books,
        'page_obj': page_obj,
        'genre_list': genre_list,
    }
    # C.S. edits to index
    if not request.user.is_authenticated:
        return render(request, 'BookDetails/index.html', context)
    else:
        filtered_orders = Order.objects.filter(owner=request.user.profile)
        current_order_products = []
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [
                product.product for product in user_order_items]

        context = {
            'Book': Books,
            'page_obj': page_obj,
            'genre_list': genre_list,
            'current_order_products': current_order_products
        }
        return render(request, "BookDetails/index.html", context)

# C.R. method to browse by best seller


def book_top_seller(request):
    Books = Book.objects.filter(top_seller=True)
    paginate_by = request.GET.get('paginate_by', 10)
    paginator = Paginator(Books, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    genre_list = Genre.objects.all()

    sorted_list = [books.id for books in Books]
    request.session['export_querset'] = sorted_list

    context = {
        'Book': Books,
        'page_obj': page_obj,
        'genre_list': genre_list,
    }
    # C.S. edits to index
    if not request.user.is_authenticated:
        return render(request, 'BookDetails/index.html', context)
    else:
        filtered_orders = Order.objects.filter(owner=request.user.profile)
        current_order_products = []
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [
                product.product for product in user_order_items]

        context = {
            'Book': Books,
            'page_obj': page_obj,
            'current_order_products': current_order_products,
            'genre_list': genre_list,
        }
        return render(request, "BookDetails/index.html", context)

# C.R. method to browse by ratings


def book_rating(request, filter):
    if filter == 1:
        Books = Book.objects.filter(rating__gte=1)
    elif filter == 2:
        Books = Book.objects.filter(rating__gte=2)
    elif filter == 3:
        Books = Book.objects.filter(rating__gte=3)
    elif filter == 4:
        Books = Book.objects.filter(rating__gte=4)
    elif filter == 5:
        Books = Book.objects.filter(rating=5)
    else:
        Books = Book.objects.all()

    paginate_by = request.GET.get('paginate_by', 10)
    paginator = Paginator(Books, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    genre_list = Genre.objects.all()

    sorted_list = [books.id for books in Books]
    request.session['export_querset'] = sorted_list
    
    context = {
        'Book': Books,
        'page_obj': page_obj,
        'genre_list': genre_list,
    }
    # C.S. edits to index
    if not request.user.is_authenticated:
        return render(request, 'BookDetails/index.html', context)
    else:
        filtered_orders = Order.objects.filter(owner=request.user.profile)
        current_order_products = []
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [
                product.product for product in user_order_items]

        context = {
            'Book': Books,
            'page_obj': page_obj,
            'genre_list': genre_list,
            'current_order_products': current_order_products
        }
        return render(request, "BookDetails/index.html", context)

# C.R. method to order books


def book_order(request, filter=None):
    sorted_list = [Book.objects.get(id=id) for id in request.session['export_querset']]

    if filter == 1:
        Books = Book.objects.filter(book_name__in=sorted_list).order_by('book_name')
    elif filter == 2:
        Books = Book.objects.filter(book_name__in=sorted_list).order_by('-book_name')
    elif filter == 3:
        Books = Book.objects.filter(book_name__in=sorted_list).order_by('author')
    elif filter == 4:
        Books = Book.objects.filter(book_name__in=sorted_list).order_by('-author')
    elif filter == 5:
        Books = Book.objects.filter(book_name__in=sorted_list).order_by('price')
    elif filter == 6:
        Books = Book.objects.filter(book_name__in=sorted_list).order_by('-price')
    elif filter == 7:
        Books = Book.objects.filter(book_name__in=sorted_list).order_by('published_date')
    elif filter == 8:
        Books = Book.objects.filter(book_name__in=sorted_list).order_by('-published_date')
    elif filter == 9:
        Books = Book.objects.filter(book_name__in=sorted_list).order_by('rating')
    else:
        Books = Book.objects.filter(book_name__in=sorted_list).order_by('-rating')


    paginate_by = request.GET.get('paginate_by', 10)
    paginator = Paginator(Books, paginate_by)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    genre_list = Genre.objects.all()

    

    context = {
        'Book': Books,
        'page_obj': page_obj,
        'genre_list': genre_list,
        'sorted_list': sorted_list,
    }
    # C.S. edits to index
    if not request.user.is_authenticated:
        return render(request, 'BookDetails/index.html', context)
    else:
        filtered_orders = Order.objects.filter(owner=request.user.profile)
        current_order_products = []
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [
                product.product for product in user_order_items]

        context = {
            'Book': Books,
            'page_obj': page_obj,
            'genre_list': genre_list,
            'current_order_products': current_order_products,
            'sorted_list': sorted_list,
        }
        return render(request, 'BookDetails/index.html', context)


@login_required()
def save_item(request, item_id):
    item_to_add = OrderItem.objects.filter(pk=item_id).update(is_saved=True)
    messages.info(request, "This book saved for later.")
    return redirect(reverse('order_summary'))


@login_required()
def add_back_item(request, item_id):
    item_to_add = OrderItem.objects.filter(pk=item_id).update(is_saved=False)
    messages.info(request, "This book added back to cart.")
    return redirect(reverse('order_summary'))


def bookDetails(request, title):
    book = get_object_or_404(Book, book_name=title)
    genre_list = Genre.objects.all()
    # C.S. edits to index
    if not request.user.is_authenticated:
        context = {
            'Book': book,
            'genre_list': genre_list,
        }
        return render(request, 'BookDetails/bookDetails.html', context)
    else:
        filtered_orders = Order.objects.filter(owner=request.user.profile)
        current_order_products = []
        if filtered_orders.exists():
            user_order = filtered_orders[0]
            user_order_items = user_order.items.all()
            current_order_products = [
                product.product for product in user_order_items]

        context = {
            'Book': book,
            'current_order_products': current_order_products,
            'genre_list': genre_list,
        }
        return render(request, "BookDetails/bookDetails.html", context)

# C.S. views for Shopping Cart feature


def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')[
        2:] + str(datetime.datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str


def get_user_pending_order(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.filter(owner=user_profile)
    if order.exists():
        return order[0]
    return 0


@login_required()
def add_to_cart(request, **kwargs):
    user_profile = get_object_or_404(Profile, user=request.user)
    product = Book.objects.filter(id=kwargs.get('item_id', "")).first()
    order_item, status = OrderItem.objects.get_or_create(product=product)
    user_order, status = Order.objects.get_or_create(owner=user_profile)
    user_order.items.add(order_item)
    if status:
        user_order.ref_code = generate_order_id()
        user_order.save()

    messages.info(request, "item added to cart")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def add_quantity_from_cart(request, item_id):
    item_to_add = OrderItem.objects.filter(
        pk=item_id).update(quantity=F('quantity') + 1)
    messages.info(request, "This books quantity added.")
    return redirect(reverse('order_summary'))


@login_required()
def reduce_quantity_from_cart(request, item_id):
    item_to_reduce = OrderItem.objects.filter(pk=item_id)
    if item_to_reduce[0].quantity < 2:
        item_to_reduce[0].delete()
        messages.info(
            request, "Book has been removed since quantity less than 1")
    else:
        item_to_reduce.update(quantity=F('quantity') - 1)
        messages.info(request, "This books quantity reduced.")
    return redirect(reverse('order_summary'))


@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Book has been removed")
    return redirect(reverse('order_summary'))


@login_required()
def order_details(request, **kwargs):
    genre_list = Genre.objects.all()
    existing_order = get_user_pending_order(request)

    context = {
        'order': existing_order,
        'genre_list': genre_list,
    }
    return render(request, 'BookDetails/order_summary.html', context)


@login_required()
def checkout(request):
    OrderItem.objects.filter(is_saved=False).delete()
    messages.info(request, "Thank you, order processed.")
    return redirect(reverse('order_summary'))
