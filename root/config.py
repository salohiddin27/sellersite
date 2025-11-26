import os

from decouple import config, Csv
from icecream import ic

# Check if .env file exists
env_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.env'))
if not os.path.exists(env_file_path):
    ic(f"File not found: {env_file_path}")
    ic('.env fayli topilmadi!')
    ic('.env.example faylidan nusxa ko\'chirib shablonni o\'zizga moslang.')
    exit(1)

SECRET_KEY = config('SECRET_KEY', default='djangorestframework')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', default='http://127.0.0.1', cast=Csv())
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='http://127.0.0.1', cast=Csv())