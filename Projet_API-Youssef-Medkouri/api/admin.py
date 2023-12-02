from django.contrib import admin

from .models import Restaurant, Menu, MenuItem, Order, Reservation


class BaseAdmin(admin.ModelAdmin):
    pass


@admin.register(Restaurant)
class RestaurantAdmin(BaseAdmin):
    list_display = ["pk", "name", "created_at", "updated_at"]


@admin.register(Menu)
class MenuAdmin(BaseAdmin):
    list_display = ["pk", "restaurant", "created_at", "updated_at"]


@admin.register(MenuItem)
class MenuItemAdmin(BaseAdmin):
    list_display = ["pk", "title", "menu", "created_at", "updated_at"]


@admin.register(Order)
class OrderAdmin(BaseAdmin):
    list_display = ["pk", "created_by", "created_at", "updated_at"]


@admin.register(Reservation)
class ReservationAdmin(BaseAdmin):
    list_display = ["pk", "created_by", "created_at", "updated_at"]
