from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from core.models import Category, Item, Slide


class Command(BaseCommand):
    help = "Seed demo categories, items, and slides for local development."

    def handle(self, *args, **options):
        categories = [
            {
                "title": "Shoes",
                "description": "Performance and lifestyle shoes.",
                "image": "banner-02.webp",
            },
            {
                "title": "T-Shirts",
                "description": "Daily wear tees and active tops.",
                "image": "banner-03.webp",
            },
            {
                "title": "Hoodies",
                "description": "Warm and comfortable hoodies.",
                "image": "banner-07.webp",
            },
            {
                "title": "Accessories",
                "description": "Add-ons and training accessories.",
                "image": "banner-08.webp",
            },
        ]

        category_map = {}
        for data in categories:
            slug = slugify(data["title"])
            category, _ = Category.objects.get_or_create(
                slug=slug,
                defaults={
                    "title": data["title"],
                    "description": data["description"],
                    "image": data["image"],
                    "is_active": True,
                },
            )
            category_map[data["title"]] = category

        items = [
            {
                "title": "Runner Pro",
                "category": "Shoes",
                "label": "N",
                "price": Decimal("120.00"),
                "discount_price": Decimal("99.00"),
                "stock_no": "RUN001",
                "description_short": "Lightweight running shoe",
                "description_long": "Breathable upper and cushioned midsole for daily training.",
                "image": "item-10.webp",
            },
            {
                "title": "Street Classic Tee",
                "category": "T-Shirts",
                "label": "S",
                "price": Decimal("35.00"),
                "discount_price": Decimal("25.00"),
                "stock_no": "TEE001",
                "description_short": "Cotton crew-neck tee",
                "description_long": "Soft fabric and relaxed fit for everyday comfort.",
                "image": "item-11.webp",
            },
            {
                "title": "Core Hoodie",
                "category": "Hoodies",
                "label": "P",
                "price": Decimal("80.00"),
                "discount_price": Decimal("69.00"),
                "stock_no": "HOD001",
                "description_short": "Fleece-lined hoodie",
                "description_long": "Warm fleece interior with minimal street-ready design.",
                "image": "item-12.webp",
            },
            {
                "title": "Gym Bottle",
                "category": "Accessories",
                "label": "N",
                "price": Decimal("18.00"),
                "discount_price": None,
                "stock_no": "ACC001",
                "description_short": "Reusable training bottle",
                "description_long": "Leak-resistant bottle for gym and outdoor use.",
                "image": "gallery-09.webp",
            },
        ]

        for data in items:
            slug = slugify(data["title"])
            Item.objects.get_or_create(
                slug=slug,
                defaults={
                    "title": data["title"],
                    "price": data["price"],
                    "discount_price": data["discount_price"],
                    "category": category_map[data["category"]],
                    "label": data["label"],
                    "stock_no": data["stock_no"],
                    "description_short": data["description_short"],
                    "description_long": data["description_long"],
                    "image": data["image"],
                    "is_active": True,
                },
            )

        slides = [
            {
                "caption1": "Spring Collection",
                "caption2": "Fresh New Arrivals",
                "link": "/shop/",
                "image": "1920x678-1.jpg",
            },
            {
                "caption1": "Run Faster",
                "caption2": "Performance Essentials",
                "link": "/shop/",
                "image": "light-bulbs--1920x570.jpg",
            },
        ]

        for data in slides:
            Slide.objects.get_or_create(
                caption1=data["caption1"],
                caption2=data["caption2"],
                defaults={
                    "link": data["link"],
                    "image": data["image"],
                    "is_active": True,
                },
            )

        self.stdout.write(self.style.SUCCESS("Demo data seeded successfully."))
