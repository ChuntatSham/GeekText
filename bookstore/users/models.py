from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.core.exceptions import ValidationError 
from django.utils.translation import gettext_lazy as _


MONTH_CHOICES = (
    ('01', 'January'),
    ('02', 'February'),
    ('03', 'March'),
    ('04', 'April'),
    ('05', 'May'),
    ('06', 'June'),
    ('07', 'July'),
    ('08', 'August'),
    ('09', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
)


YEAR_CHOICES = (
    ('2020', '2020'),
    ('2021', '2021'),
    ('2022', '2022'),
    ('2023', '2023'),
    ('2024', '2024'),
    ('2025', '2025'),
    ('2026', '2026'),
    ('2027', '2027'),
    ('2028', '2028'),
    ('2029', '2029'),
    ('2030', '2030'),
    ('2031', '2031'),
    ('2032', '2032'),
    ('2033', '2033'),
    ('2034', '2034'),
)


def validate_zip(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s is not a 5 digit zipcode '),
            params={'value':value},
        )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, default='')
    street_address = models.CharField(max_length=100, default='')
    apartment_address = models.CharField(max_length=100, null=True, blank=True, default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=50, default='')
    zip = models.IntegerField(validators=[validate_zip], default=0)
    country = CountryField(multiple=False, default='US')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Address(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=Profile)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=50)
    zip = models.IntegerField(validators=[validate_zip])
    country = CountryField(multiple=False, default='US')
    default = models.BooleanField(default=False)

    def get_absolute_url(self):
        return f"/users/address-management/%i/" % self.id
    
    class Meta:
        verbose_name_plural = 'Addresses'


class CreditCard(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=Profile)
    card_number = models.CharField(max_length=16)
    expiration_month = models.CharField(max_length=2, choices=MONTH_CHOICES, default='05')
    expiration_year = models.CharField(max_length=4, choices=YEAR_CHOICES, default='01')
    security_code = models.IntegerField()
    cardholder_name = models.CharField(max_length=100)
    default = models.BooleanField(default=False)

    def get_absolute_url(self):
        return f"/users/card-management/%i/" % self.id
    
    class Meta:
        verbose_name_plural = 'CCards'


