from django.core.exceptions import ValidationError
from PIL import Image

def validate_image_file_type(value):
    valid_formats = ("JPEG", "PNG")
    try:
        img = Image.open(value)
        img_format = img.format.upper()
        if img_format not in valid_formats:
            raise ValidationError("Please upload a JPG or PNG image.")
    except Exception:
        raise ValidationError("Invalid image file.")
    finally:
        value.seek(0)

def validate_image_file_size(value):
    max_size = 10 * 1024 * 1024  # 10 MB
    if value.size > max_size:
        raise ValidationError("Image must be under 10 MB.")
