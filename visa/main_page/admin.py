from django.contrib import admin

from .models import Article, Service


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')
    search_fields = ('title',)
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'amount_of_days')
    search_fields = ('title',)
    list_filter = ('price', 'amount_of_days')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Service, ServiceAdmin)
