from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserSignupForm, UserUpdateForm, ProfileUpdateForm, AddressForm, CreditCardForm
from .models import Address, CreditCard
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from books.models import Genre

def SignUpView(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You can login now')
            return redirect('login')
    else:
        form = UserSignupForm()
    return render(request, 'users/signup.html', {'form': form})


@login_required
def ProfileView(request):
    genre_list = Genre.objects.all()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        # a_form = AddressForm(request.POST, instance=request.user.address)
        if u_form.is_valid() and p_form.is_valid():# and a_form.is_valid():
            u_form.save()
            p_form.save()
            # a_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        # a_form = AddressForm(instance=request.user.address)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'genre_list': genre_list,
        # 'a_form': a_form
    }

    return render(request, 'users/profile.html', context)


################# ADDRESS ######################

@login_required
def AddressView(request):
    genre_list = Genre.objects.all()
    if request.method == 'POST':
        a_form = AddressForm(request.POST)#, instance=request.user.addresses)
        if a_form.is_valid():
            address = a_form.save(commit=False)
            address.profile = request.user.profile
            address.save()
            messages.success(request, f'Address saved successfully!')
            return redirect('address_management')
        else:
            return render(request, 'users/add_address.html', { 'a_form':a_form })
    else:
        a_form = AddressForm(None)#instance=request.user.addresses)
        return render(request, 'users/add_address.html', {'a_form':a_form})


def AddressListView(request):
    queryset = Address.objects.all()
    return render(request, 'users/address_management.html', { 'object_list': queryset })
    

def AddressUpdateView(request, id=id):
    obj = get_object_or_404(Address, id=id)
    # obj = Address.objects.get(id=id)
    form = AddressForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, f'Address updated successfully!')
        return redirect('address_management')
    context = { 'form': form }
    return render(request, 'users/address_update.html', context)


def AddressDeleteView(request, id=id):
    obj = get_object_or_404(Address, id=id)
    # obj = Address.objects.get(id=id)
    # form = AddressForm(request.POST or None, instance=obj)
    if request.method == "POST":
        obj.delete()
        messages.success(request, f'Address deleted successfully!')
        return redirect('address_management')
    context = { 'object': obj }
    return render(request, 'users/address_delete.html', context)


################# CREDIT CARD ######################

@login_required
def CCardView(request):
    if request.method == 'POST':
        cc_form = CreditCardForm(request.POST)#, instance=request.user.addresses)
        if cc_form.is_valid():
            card = cc_form.save(commit=False)
            card.profile = request.user.profile
            card.save()
            messages.success(request, f'Credit card saved successfully!')
            return redirect('card_management')
        else:
            return render(request, 'users/add_card.html', { 'cc_form':cc_form })
    else:
        cc_form = CreditCardForm(None)#instance=request.user.addresses)
        return render(request, 'users/add_card.html', {'cc_form':cc_form})


def CCardListView(request):
    queryset = CreditCard.objects.all() 
    return render(request, 'users/card_management.html', { 'object_list': queryset })
    

def CCardUpdateView(request, id=id):
    obj = get_object_or_404(CreditCard, id=id)
    form = CreditCardForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, f'Credit card updated successfully!')
        return redirect('card_management')
    context = { 'form': form }
    return render(request, 'users/card_update.html', context)


def CCardDeleteView(request, id=id):
    obj = get_object_or_404(CreditCard, id=id)
    if request.method == "POST":
        obj.delete()
        messages.success(request, f'Credit card deleted successfully!')
        return redirect('card_management')
    context = { 'object': obj }
    return render(request, 'users/card_delete.html', context)