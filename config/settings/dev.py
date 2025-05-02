from .base import *
import os

DEBUG = True
ALLOWED_HOSTS = ['*']

# If you're running the project on your local machine, replace 'IP_BASE' with '0.0.0.0'.
# If you want to scan the QR code from a different device (like mobile) with LAN connection between pc and mobile, replace 'IP_BASE' with your computer's local IP address (e.g., 192.168.x.x).
QR_BASE_URL = 'http://IP_BASE:8000'

# Enable template tags
@register.filter(name='b64encode')
def b64encode(value):
    return base64.b64encode(value).decode('utf-8')