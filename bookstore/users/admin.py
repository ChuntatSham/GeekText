from django.contrib import admin
from .models import Profile, Address, CreditCard

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'profile',
        'street_address',
        'apartment_address',
        'city',
        'state',
        'zip',
        'country',
        'default'
    ]

class CreditCardAdmin(admin.ModelAdmin):
    list_display = [
        'card_number',
        'expiration_month',
        'expiration_year',
        'security_code',
        'cardholder_name',
        'default'
    ]

admin.site.register(Profile)
admin.site.register(Address, AddressAdmin)
admin.site.register(CreditCard, CreditCardAdmin)