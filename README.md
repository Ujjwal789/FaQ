Multilingual FAQ Management System

Overview

This project is a Django-based FAQ management system with multi-language support, rich text editing, and optimized performance using caching. The system allows users to store, manage, and retrieve FAQs dynamically in multiple languages.

Features

Django Models with WYSIWYG Support: Uses django-ckeditor for rich text formatting.

Multilingual Support: FAQs are stored with translations, and users can fetch FAQs in their preferred language.

REST API: Fully functional API supporting language selection via ?lang= query parameter.

Caching with Redis: Speeds up retrieval using Django cache framework.

Automated Translations: Uses Google Translate API to auto-translate FAQs during creation.

Admin Panel: User-friendly admin interface for managing FAQs.

Unit Testing: Comprehensive test coverage using pytest.

Docker Support: Provides Dockerfile and docker-compose.yml for easy deployment.

Installation

Prerequisites

Ensure you have the following installed:

Python 3.8+

Django

Redis

Docker (optional)

Steps

1 Clone the repository
git clone https://github.com/Ujjwal789/FaQ


2 Create a virtual environment
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

3 Install dependencies
pip install -r requirements.txt

4 Run Migrations
python manage.py migrate

5 Run The Server
python manage.py migrate

Contributing

We welcome contributions! Follow these steps:

1 Fork the repository.

2 Create a feature branch: git checkout -b feature-name.

3 Commit your changes: git commit -m "feat: Describe your feature".

4 Push to your branch and create a pull request.
