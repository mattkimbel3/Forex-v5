from django.contrib import admin
from .models import Account, Trade, ForexPair, OptionTrade, CryptoPair, Profile

# Register your models here.
admin.site.register(Account)
admin.site.register(CryptoPair)
admin.site.register(Trade)
admin.site.register(Profile)
admin.site.register(ForexPair)
admin.site.register(OptionTrade)