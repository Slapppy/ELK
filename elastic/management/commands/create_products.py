import random
import string
from django.core.management.base import BaseCommand
from elastic.models import Product


class Command(BaseCommand):
    help = "Creates 10,000 Product records"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating 10,000 Product records...")
        for _ in range(10000):
            name = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
            description = "".join(
                random.choices(string.ascii_letters + string.digits, k=50)
            )
            price = round(random.uniform(1, 1000), 2)
            Product.objects.create(name=name, description=description, price=price)
        self.stdout.write(
            self.style.SUCCESS("Successfully created 10,000 Product records")
        )
