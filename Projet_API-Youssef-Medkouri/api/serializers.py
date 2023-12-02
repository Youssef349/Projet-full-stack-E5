from rest_framework import serializers

from .models import Order, Reservation, Menu, MenuItem


def all_same_menu(value):
    if len(set([item.menu.pk for item in value["menu_items"]])) != 1:
        raise serializers.ValidationError(
            "All menu items must be from the same restaurant."
        )
    if value["menu_items"][0].menu.restaurant != value["restaurant"]:
        raise serializers.ValidationError(
            "All menu items must be from the restaurant specified in the 'restaurant' field"
        )


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("menu_items", "restaurant")
        validators = [all_same_menu]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Order


class ReservationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("reserved_at", "restaurant")


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Reservation


class MenuCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ("restaurant",)


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Menu


class MenuItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("menu", "title", "description", "price")
        model = MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = MenuItem
