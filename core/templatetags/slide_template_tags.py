from django import template
from django.templatetags.static import static
from django.utils.safestring import mark_safe

from core.image_utils import media_url_or_fallback
from core.models import Slide

register = template.Library()


@register.simple_tag
def slides():
    items = Slide.objects.filter(is_active=True).order_by('pk')
    items_div = ""
    default_slides = [
        ("images/pngtree-outdoor-hiking-shoes-banner-pictures-image_877424.jpg", "New Outdoor Collection", "High performance, all terrain"),
        ("images/34mpIkbEsTI9M.jpg", "Built For Everyday", "Comfort and style combined"),
    ]
    if not items:
        for image_path, caption1, caption2 in default_slides:
            image_url = static(image_path)
            items_div += """<div class="item-slick1 item2-slick1" style="background-image: url({});"><div class="wrap-content-slide1 sizefull flex-col-c-m p-l-15 p-r-15 p-t-150 p-b-170"><span class="caption1-slide1 m-text1 t-center animated visible-false m-b-15" data-appear="rollIn">{}</span><h2 class="caption2-slide1 xl-text1 t-center animated visible-false m-b-37" data-appear="lightSpeedIn">{}</h2><div class="wrap-btn-slide1 w-size1 animated visible-false" data-appear="slideInUp"><a href="/shop/" class="flex-c-m size2 bo-rad-23 s-text2 bgwhite hov1 trans-0-4">Shop Now</a></div></div></div>""".format(image_url, caption1, caption2)
        return mark_safe(items_div)

    for i in items:
        fallback = default_slides[(i.pk or 0) % 2][0]
        image_url = media_url_or_fallback(i.image, fallback)
        items_div += """<div class="item-slick1 item2-slick1" style="background-image: url({});"><div class="wrap-content-slide1 sizefull flex-col-c-m p-l-15 p-r-15 p-t-150 p-b-170"><span class="caption1-slide1 m-text1 t-center animated visible-false m-b-15" data-appear="rollIn">{}</span><h2 class="caption2-slide1 xl-text1 t-center animated visible-false m-b-37" data-appear="lightSpeedIn">{}</h2><div class="wrap-btn-slide1 w-size1 animated visible-false" data-appear="slideInUp"><a href="{}" class="flex-c-m size2 bo-rad-23 s-text2 bgwhite hov1 trans-0-4">Shop Now</a></div></div></div>""".format(image_url, i.caption1 or "", i.caption2 or "", i.link or "/shop/")
    return mark_safe(items_div)


