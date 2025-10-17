# SKIP TO -> SIMPLE START STEPS (if you know what you're doing without getting lost) 

# Simple Overview & Setup Guide

- 📋 What Each File Does (Simple Explanation)

## 1. models.py - The Database Structure
-What it is: Defines what data you store (like creating Excel tables) Contains:

- Subscriber table (name, email, date joined)
- Recipe table (title, ingredients, instructions, cook time)
- Category table (Italian, American, Desserts)
- Review table (ratings and comments on recipes)
- Contact Message table (messages from website visitors)

`Think of it as: Your database blueprint`

## 2. serializers.py - Data Translator
What it is: Converts database data to JSON (and vice versa)
Why needed: Apps communicate in JSON format
Example:

Database: `Recipe object (id=1)`
JSON: `{"id": 1, "title": "Pasta", "cook_time": 15}`

#### Think of it as: A translator between database and internet

## 3. api_views.py - The Logic Center
What it is: Handles all API requests (GET, POST, PUT, DELETE)
Contains:

- Functions to list recipes
- Functions to create/update/delete data
- Search and filter logic
- Email sending logic

#### Think of it as: The brain that processes requests

## 4. api_urls.py - The Address Book
What it is: Maps URLs to functions
Example:

- `/api/recipes/` → shows all recipes
- `/api/subscribers/` → shows all subscribers

#### Think of it as: GPS directions for your API

## 5. admin.py - Admin Dashboard Setup
What it is: Makes Django admin panel better
Features:

- Search bars
- Filters
- Bulk actions (approve 10 reviews at once)

#### Think of it as: Your control panel customization

## 6. settings.py Updates - Configuration File

- What it is: Tells Django to use REST Framework

Contains:
- Install REST Framework
- Add CORS (lets other websites use your API)
- Pagination settings

#### Think of it as: Your app's settings menu

## 7. restaurant_web/urls.py - Main Routing

- What it is: Connects /api/ to your API URLs
- Simple change: Just adds one line to include API routes
#### Think of it as: Main entrance that directs traffic

## 8. requirements.txt - Shopping List

- What it is: List of packages to install

Contains:
- Django
- Django REST Framework
- Django Filter
- CORS Headers

#### Think of it as: Your grocery list for Python packages

## 9. INSTALLATION_GUIDE.md - Step-by-Step Setup

- What it is: Detailed instructions to install everything

Contains:
- Commands to run
- How to test
- Troubleshooting tips

#### Think of it as: An instruction manual

## 10. API_DOCUMENTATION.md - User Manual
- What it is: Explains every API endpoint

Contains:
- What each URL does
- Example requests and responses
- Query parameters

#### Think of it as: The API dictionary

## 11. API_TEST_COMMANDS.md - Testing Cheat Sheet
- What it is: Copy-paste commands to test your API

Contains:
- cURL commands
- Python examples
- Browser URLs

#### Think of it as: Practice exercises with answers

## 12. README_API.md - Project Overview
- What it is: Complete project documentation

Contains:
- What the project does
- How to use it
- All features listed

#### Think of it as: The book cover and table of contents

# 🎯 SIMPLE START STEPS (Follow This Order!)

## STEP 1: Install Dependencies ⏱️ 2 minutes
```
pip install djangorestframework django-filter django-cors-headers
```
- What this does: Downloads the tools you need

## STEP 2: Copy Files ⏱️ 5 minutes

In your `recipes/` folder, create/replace these files:

- Copy `models.py` content → Replace your `recipes/models.py`
- Copy `serializers.py` content → Create NEW file `recipes/serializers.py`
- Copy `api_views.py` content → Create NEW file `recipes/api_views.py`
- Copy `api_urls.py` content → Create NEW file `recipes/api_urls.py`
- Copy `admin.py` content → Replace your `recipes/admin.py`

#### In your -  restaurant_web/ - folder:

Copy the settings updates → Add to your `restaurant_web/settings.py`
Copy the URL config → Update your `restaurant_web/urls.py`

## STEP 3: Update Settings ⏱️ 3 minutes

Open `restaurant_web/settings.py` and add:

```
INSTALLED_APPS = [
    # ... your existing apps ...
    'rest_framework',      # ADD THIS
    'django_filters',      # ADD THIS
    'corsheaders',        # ADD THIS
    'recipes',
]
```
- Scroll to bottom and paste the REST_FRAMEWORK settings from artifact #6. `settings.py`



