from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Article, Service, Client


#class ArticleAdmin(admin.ModelAdmin):
#    list_display = ('title', 'created_date')
#    search_fields = ('title',)
#    list_filter = ('created_date',)
#    date_hierarchy = 'created_date'
#
#
#class ServiceAdmin(admin.ModelAdmin):
#    list_display = ('title', 'price', 'amount_of_days')
#    search_fields = ('title',)
#    list_filter = ('price', 'amount_of_days')
#
#
#class ClientAdmin(admin.ModelAdmin):
#    list_display = ('name', 'phone', 'email')
#    search_fields = ('name',)
#    list_filter = ('name',)
#
#
admin.site.register(Article, TranslatableAdmin)
admin.site.register(Service, TranslatableAdmin)
admin.site.register(Client, TranslatableAdmin)
