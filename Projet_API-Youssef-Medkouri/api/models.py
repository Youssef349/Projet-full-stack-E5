from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True


class Restaurant(BaseModel):
    name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.name


class Menu(BaseModel):
    restaurant = models.OneToOneField(
        Restaurant,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self) -> str:
        return f"{self.restaurant}'s Menu"


class MenuItem(BaseModel):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    price = models.FloatField()

    def __str__(self) -> str:
        return f"{self.title} from {self.menu}"


class Order(BaseModel):
    class OrderStatus(models.IntegerChoices):
        DRAFT = 0
        SUBMITTED = 1
        CONFIRMED = 2
        PROCESSING = 3
        COMPLETED = 4

    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="orders"
    )
    menu_items = models.ManyToManyField(MenuItem)
    status = models.IntegerField(
        choices=OrderStatus.choices, default=OrderStatus.DRAFT
    )


class Reservation(BaseModel):
    class ReservationStatus(models.IntegerChoices):
        DRAFT = 0
        SUBMITTED = 1
        CONFIRMED = 2
        PROCESSING = 3
        COMPLETED = 4

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    status = models.IntegerField(
        choices=ReservationStatus.choices, default=ReservationStatus.DRAFT
    )
    reserved_at = models.DateTimeField()
