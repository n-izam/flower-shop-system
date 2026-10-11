from django.core.management.base import BaseCommand
from shops.models import Shop


class Command(BaseCommand):
    help = "Seeds initial UAE shop locations into database"

    def handle(self, *args, **kwargs):
        shops_data = [
            {
                "name": "Shop 1 - Downtown Dubai Branch",
                "address": "Downtown Dubai, Near Burj Khalifa Area, Dubai, UAE",
                "latitude": 25.197197,
                "longitude": 55.274376,
                "geofence_radius": 200,  # 200 meters
                "is_active": True,
            },
            {
                "name": "Shop 2 - Dubai Marina Branch",
                "address": "Dubai Marina Promenade, Dubai, UAE",
                "latitude": 25.077250,
                "longitude": 55.133240,
                "geofence_radius": 250,  # 250 meters
                "is_active": True,
            },
        ]

        for data in shops_data:
            shop, created = Shop.objects.get_or_create(
                name=data["name"],
                defaults=data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created shop: '{shop.name}'"))
            else:
                self.stdout.write(self.style.WARNING(f"Shop '{shop.name}' already exists."))