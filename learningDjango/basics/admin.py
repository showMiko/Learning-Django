from django.contrib import admin
from .models import Item, Review, Tag, ItemDetail

# Register your models here.

class ItemReviewInline(admin.TabularInline):
    model = Review
    extra = 3

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'in_stock', 'date_added')
    list_filter = ('type', 'in_stock', 'date_added')
    search_fields = ('name', 'description')
    inlines = [ItemReviewInline]

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    filter_horizontal = ('items',)

class ItemDetailsAdmin(admin.ModelAdmin):
    list_display = ('item', 'manufacturer', 'warranty_period')
    search_fields = ('item__name', 'manufacturer')



admin.site.register(Item, ItemAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(ItemDetail, ItemDetailsAdmin)


