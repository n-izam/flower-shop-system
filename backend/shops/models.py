from django.db import models


class Shop(models.Model):
    name = models.CharField(
        max_length=150, 
        unique=True, 
        help_text="Name of the shop branch"
    )
    address = models.TextField(
        blank=True, 
        help_text="Physical address or area location"
    )
    latitude = models.DecimalField(
        max_digits=9, 
        decimal_places=6, 
        help_text="GPS Latitude coordinate"
    )
    longitude = models.DecimalField(
        max_digits=9, 
        decimal_places=6, 
        help_text="GPS Longitude coordinate"
    )
    geofence_radius = models.PositiveIntegerField(
        default=200, 
        help_text="Geofence radius in meters for worker attendance check-in"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'

    def __str__(self):
        return self.name