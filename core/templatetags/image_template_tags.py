from django import template

from core.image_utils import media_url_or_fallback

register = template.Library()


@register.filter(name="safe_image")
def safe_image(image_field, fallback_static_path="images/61Fbt5Yyf2L._AC_UY1000_.jpg"):
    return media_url_or_fallback(image_field, fallback_static_path)
