import re
from os.path import basename

from django.templatetags.static import static


BAD_IMAGE_TOKENS = (
    "1920x678",
    "1920x570",
    "1920x239",
    "720x600",
    "600x720",
    "placeholder",
    "no-image",
)


def media_url_or_fallback(image_field, fallback_static_path):
    try:
        url = image_field.url
    except Exception:
        return static(fallback_static_path)

    image_name = basename(str(image_field)).lower()
    if not image_name:
        return static(fallback_static_path)
    if any(token in image_name for token in BAD_IMAGE_TOKENS):
        return static(fallback_static_path)
    if "via.placeholder.com" in url.lower():
        return static(fallback_static_path)
    if re.match(r"^\d{3,4}x\d{3,4}", image_name):
        return static(fallback_static_path)
    return url
