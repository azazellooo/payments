from django.contrib import admin

from .models import Card, Purchase, STATUS_CHOICES


def activate_cards(modeladmin, request, queryset):
    for card in queryset:
        card.status = STATUS_CHOICES[0][0]
        card.save()


def inactivate_cards(modeladmin, request, queryset):
    for card in queryset:
        card.status = STATUS_CHOICES[1][0]
        card.save()


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner_name', 'number', 'issue_date',  'expiration_date', 'status']
    list_filter = ['issue_date', 'status']
    search_fields = ['owner_name', 'number', 'issue_date', 'status']
    fields = ['owner_name', 'status']
    readonly_fields = ['expiration_date', 'id', 'issue_date', 'number']
    list_editable = ['status']
    actions = [activate_cards, inactivate_cards]

    activate_cards.short_description = 'Activate selected cards'
    inactivate_cards.short_description = 'Inactivate selected cards'


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['good', 'price', 'cc_number', 'date']
    list_filter = ['cc_number']
    search_fields = ['cc_number__number']

# Register your models here.
