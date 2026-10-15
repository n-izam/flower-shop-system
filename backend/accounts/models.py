from django.contrib.auth.models import AbstractUser
from django.db import models
from shops.models import Shop


class User(AbstractUser):
    class Role(models.TextChoices):
        OWNER = 'OWNER', 'Shop Owner'
        MANAGER = 'MANAGER', 'Shop Manager'
        WORKER = 'WORKER', 'Florist / Staff Worker'
        DELIVERY = 'DELIVERY', 'Delivery Personnel'
        ACCOUNTANT = 'ACCOUNTANT', 'Accountant (Read-Only)'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.WORKER,
        help_text="Role determining user permissions and data access levels"
    )
    shop = models.ForeignKey(
        Shop,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='staff_members',
        help_text="Assigned primary shop branch. Owners can leave this null to access all shops."
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Contact number for WhatsApp notifications or staff communication"
    )

    class Meta:
        ordering = ['username']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        shop_name = self.shop.name if self.shop else "All Shops (Owner/Global)"
        return f"{self.username} ({self.get_role_display()}) - {shop_name}"

    @property
    def is_owner(self):
        return self.role == self.Role.OWNER

    @property
    def is_manager(self):
        return self.role == self.Role.MANAGER

    @property
    def is_worker(self):
        return self.role == self.Role.WORKER
    
    @property
    def is_delivery(self):
        return self.role == self.Role.DELIVERY

    @property
    def is_accountant(self):
        return self.role == self.Role.ACCOUNTANT