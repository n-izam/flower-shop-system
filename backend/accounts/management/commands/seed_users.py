from django.core.management.base import BaseCommand
from accounts.models import User
from shops.models import Shop


class Command(BaseCommand):
    help = "Seeds initial test users across roles (Owner, Manager, Worker) for both shop locations"

    def handle(self, *args, **kwargs):
        downtown_shop = Shop.objects.filter(name__icontains="Downtown").first()
        marina_shop = Shop.objects.filter(name__icontains="Marina").first()

        if not downtown_shop or not marina_shop:
            self.stdout.write(
                self.style.ERROR("Shops are not seeded yet! Run 'python manage.py seed_shops' first.")
            )
            return

        users_data = [
            {
                "username": "owner_admin",
                "email": "owner@flowershop.ae",
                "first_name": "Tariq",
                "last_name": "Al-Mansoori",
                "role": User.Role.OWNER,
                "shop": None,  # Owners access both shops
                "is_staff": True,
                "is_superuser": True,
            },
            {
                "username": "downtown_mgr",
                "email": "manager.downtown@flowershop.ae",
                "first_name": "Sara",
                "last_name": "Khan",
                "role": User.Role.MANAGER,
                "shop": downtown_shop,
                "is_staff": True,
                "is_superuser": False,
            },
            {
                "username": "marina_mgr",
                "email": "manager.marina@flowershop.ae",
                "first_name": "Zaid",
                "last_name": "Ahmed",
                "role": User.Role.MANAGER,
                "shop": marina_shop,
                "is_staff": True,
                "is_superuser": False,
            },
            {
                "username": "downtown_worker",
                "email": "worker1.downtown@flowershop.ae",
                "first_name": "Bilal",
                "last_name": "Hassan",
                "role": User.Role.WORKER,
                "shop": downtown_shop,
                "is_staff": False,
                "is_superuser": False,
            },
            {
                "username": "marina_worker",
                "email": "worker1.marina@flowershop.ae",
                "first_name": "Youssef",
                "last_name": "Omar",
                "role": User.Role.WORKER,
                "shop": marina_shop,
                "is_staff": False,
                "is_superuser": False,
            },
        ]

        default_password = "Password123!"

        for data in users_data:
            username = data.pop("username")
            password = default_password
            
            user, created = User.objects.get_or_create(
                username=username,
                defaults=data
            )
            if created:
                user.set_password(password)
                user.save()
                self.stdout.write(
                    self.style.SUCCESS(f"Created user '{username}' [{user.get_role_display()}]")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"User '{username}' already exists.")
                )

        self.stdout.write(
            self.style.NOTICE(f"\n[NOTE] All seeded users were assigned default password: '{default_password}'")
        )