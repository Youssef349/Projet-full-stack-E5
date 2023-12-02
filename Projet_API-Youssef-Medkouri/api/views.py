from django.db.models import Q
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from .models import Order, Reservation, Menu, MenuItem
from .serializers import (
    OrderCreateSerializer,
    OrderSerializer,
    ReservationSerializer,
    ReservationCreateSerializer,
    MenuSerializer,
    MenuCreateSerializer,
    MenuItemSerializer,
    MenuItemCreateSerializer,
)
from .permissions import IsOwnerOrReadOnly


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.filter().order_by("id")
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(
                Q(created_by=self.request.user)
                | Q(restaurant__created_by=self.request.user)
            )
        )

    def get_serializer_class(self):
        if self.action == "create":
            return OrderCreateSerializer
        else:
            return OrderSerializer

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        return Response(OrderSerializer(instance).data)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.filter().order_by("id")
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(
                Q(created_by=self.request.user)
                | Q(restaurant__created_by=self.request.user)
            )
        )

    def get_serializer_class(self):
        if self.action == "create":
            return ReservationCreateSerializer
        else:
            return ReservationSerializer

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        return Response(ReservationSerializer(instance).data)


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.filter().order_by("pk")
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action == "create":
            return MenuCreateSerializer
        else:
            return MenuSerializer

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        return Response(MenuSerializer(instance).data)


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.filter().order_by("pk")
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action == "create":
            return MenuItemCreateSerializer
        else:
            return MenuItem

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        return Response(MenuItemSerializer(instance).data)
