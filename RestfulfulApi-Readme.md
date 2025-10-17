# API TEST COMMANDS 

### Prerequisites
Make sure your server is running:

```bash
python manage.py runserver
```

## 1. Test Subscribers
### List all subscribers
```
curl http://127.0.0.1:8000/api/subscribers/
```
### Create subscriber (sends welcome email)
```
curl -X POST http://127.0.0.1:8000/api/subscribers/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com"
  }'
```

### Get specific subscriber

```
curl http://127.0.0.1:8000/api/subscribers/1/
```

### Update subscriber

```
curl -X PUT http://127.0.0.1:8000/api/subscribers/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Updated",
    "email": "john.updated@example.com",
    "is_active": true
  }'
```
### Delete subscriber

```
curl -X DELETE http://127.0.0.1:8000/api/subscribers/1/
```
### Search subscribers

```
curl "http://127.0.0.1:8000/api/subscribers/?search=john"
```

## 2. Test Categories

### List all categories

```
curl http://127.0.0.1:8000/api/categories/
```
### Create category
```
curl -X POST http://127.0.0.1:8000/api/categories/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Italian",
    "slug": "italian",
    "description": "Authentic Italian cuisine"
  }'
```
### Get category by slug

```
curl http://127.0.0.1:8000/api/categories/italian/
```
### Get recipes in category
```
curl http://127.0.0.1:8000/api/categories/italian/recipes/
```

## 3. Test Recipes

### List all recipes
```
curl http://127.0.0.1:8000/api/recipes/
```


### Get featured recipes

```
curl http://127.0.0.1:8000/api/recipes/featured/
```


### Create recipe

```
curl -X POST http://127.0.0.1:8000/api/recipes/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Pasta Carbonara",
    "slug": "pasta-carbonara",
    "description": "Classic Italian pasta",
    "ingredients": "400g spaghetti\n200g pancetta\n4 egg yolks\n100g Pecorino\nBlack pepper",
    "instructions": "1. Cook pasta\n2. Fry pancetta\n3. Mix eggs and cheese\n4. Combine\n5. Season",
    "prep_time": 10,
    "cook_time": 15,
    "servings": 4,
    "difficulty": "medium",
    "category": 1,
    "is_featured": true
  }'
```
### Get recipe by slug

```
curl http://127.0.0.1:8000/api/recipes/pasta-carbonara/
```
### Update recipe
```
curl -X PATCH http://127.0.0.1:8000/api/recipes/pasta-carbonara/ \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Updated description",
    "is_featured": false
  }'
```
### Search recipes
```
# Search by title/description/ingredients
curl "http://127.0.0.1:8000/api/recipes/?search=pasta"

# Filter by category
curl "http://127.0.0.1:8000/api/recipes/?category=1"

# Filter by difficulty
curl "http://127.0.0.1:8000/api/recipes/?difficulty=easy"

# Filter featured recipes
curl "http://127.0.0.1:8000/api/recipes/?is_featured=true"

# Sort by newest
curl "http://127.0.0.1:8000/api/recipes/?ordering=-created_at"

# Sort by title
curl "http://127.0.0.1:8000/api/recipes/?ordering=title"

# Combine filters
curl "http://127.0.0.1:8000/api/recipes/?category=1&difficulty=easy&ordering=-created_at"
```
### Pagination
```
# Get first page (10 items)
curl "http://127.0.0.1:8000/api/recipes/"

# Get second page
curl "http://127.0.0.1:8000/api/recipes/?page=2"

# Custom page size
curl "http://127.0.0.1:8000/api/recipes/?page_size=20"
```

## 4. Test Reviews

### List all reviews
```
curl http://127.0.0.1:8000/api/reviews/
```
### Create review
```
curl -X POST http://127.0.0.1:8000/api/reviews/ \
  -H "Content-Type: application/json" \
  -d '{
    "recipe": 1,
    "reviewer_name": "Alice Brown",
    "reviewer_email": "alice@example.com",
    "rating": 5,
    "comment": "Absolutely delicious! Best carbonara ever."
  }'
```

### Get reviews for specific recipe
```
curl http://127.0.0.1:8000/api/recipes/pasta-carbonara/reviews/
```
### Filter reviews by rating
```
curl "http://127.0.0.1:8000/api/reviews/?rating=5"
```

## 5. Test Contact Messages

### Submit contact message
```
curl -X POST http://127.0.0.1:8000/api/contact/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Smith",
    "email": "jane@example.com",
    "subject": "Question about recipes",
    "message": "Do you have gluten-free options available?"
  }'
```
### List all messages
```
curl http://127.0.0.1:8000/api/contact/
```
### Mark message as read
```
curl -X PATCH http://127.0.0.1:8000/api/contact/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "is_read": true
  }'
```
## 6. Test Statistics

### Get API stats
```
curl http://127.0.0.1:8000/api/stats/
```
### Using Postman
- Import this JSON collection:
```
{
  "info": {
    "name": "Restaurant API",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Subscribers",
      "item": [
        {
          "name": "List Subscribers",
          "request": {
            "method": "GET",
            "url": "http://127.0.0.1:8000/api/subscribers/"
          }
        },
        {
          "name": "Create Subscriber",
          "request": {
            "method": "POST",
            "header": [{"key": "Content-Type", "value": "application/json"}],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"name\": \"Test User\",\n  \"email\": \"test@example.com\"\n}"
            },
            "url": "http://127.0.0.1:
```

# Restaurant Web REST API Documentation 

- (documentation - extra data to use when needed) 
- useful for testing or integration
- Helpful for debugging (you know what endpoint expects what data)
- Professional use

  
## Base URL: http://127.0.0.1:8000/api/
## Authentication
- Currently, no authentication required. All endpoints are publicly accessible.

## Endpoints Overview:

### Subscribers

- GET /api/subscribers/ - List all subscribers
- POST /api/subscribers/ - Create new subscriber
- GET /api/subscribers/{id}/ - Get subscriber details
- PUT /api/subscribers/{id}/ - Update subscriber
- DELETE /api/subscribers/{id}/ - Delete subscriber

### Categories

- GET /api/categories/ - List all categories
- POST /api/categories/ - Create new category
- GET /api/categories/{slug}/ - Get category details
- PUT /api/categories/{slug}/ - Update category
- DELETE /api/categories/{slug}/ - Delete category
- GET /api/categories/{slug}/recipes/ - Get all recipes in category

### Recipes

- GET /api/recipes/ - List all recipes (paginated, filterable)
- POST /api/recipes/ - Create new recipe
- GET /api/recipes/featured/ - Get featured recipes
- GET /api/recipes/{slug}/ - Get recipe details
- PUT /api/recipes/{slug}/ - Update recipe
- DELETE /api/recipes/{slug}/ - Delete recipe
- GET /api/recipes/{slug}/reviews/ - Get all reviews for recipe

### Reviews

- GET /api/reviews/ - List all reviews
- POST /api/reviews/ - Create new review
- GET /api/reviews/{id}/ - Get review details
- PUT /api/reviews/{id}/ - Update review
- DELETE /api/reviews/{id}/ - Delete review

### Contact Messages

- GET /api/contact/ - List all contact messages
- POST /api/contact/ - Submit contact message
- GET /api/contact/{id}/ - Get message details
- PUT /api/contact/{id}/ - Update message (mark as read)
- DELETE /api/contact/{id}/ - Delete message

### Statistics

- GET /api/stats/ - Get API statistics

## Detailed Endpoint Documentation

### 1. Subscribers
  
#### List Subscribers
```
GET /api/subscribers/
```

#### Query Parameters:
- search - Search by name or email
- ordering - Order by fields (e.g., -subscribed_at)
- page - Page number
- page_size - Results per page
(response): 
```
{
  "count": 50,
  "next": "http://127.0.0.1:8000/api/subscribers/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "subscribed_at": "2025-10-15T10:30:00Z",
      "is_active": true
    }
  ]
}
```

- Create Subscriber
```
POST /api/subscribers/
Content-Type: application/json

{
  "name": "Jane Smith",
  "email": "jane@example.com"
}
```
Success Response (201):
```
{
  "id": 2,
  "name": "Jane Smith",
  "email": "jane@example.com",
  "subscribed_at": "2025-10-17T14:22:00Z",
  "is_active": true
}
```
Error Response (400):
```
{
  "email": ["This email is already subscribed."]
}
```
 
### 2. Categories

#### List Categories
```
GET /api/categories/
```
Response:
```
[
  {
    "id": 1,
    "name": "Italian",
    "description": "Italian cuisine",
    "slug": "italian",
    "recipe_count": 15,
    "created_at": "2025-10-01T12:00:00Z"
  }
]
```
#### Get Recipes by Category
```
GET /api/categories/italian/recipes/
```
- Response: Paginated list of recipes in that category

### 3. Recipes

#### List Recipes

```
GET /api/recipes/
```

#### Query Parameters:

- search - Search in title, description, ingredients
- category - Filter by category ID
- difficulty - Filter by difficulty (easy, medium, hard)
- is_featured - Filter featured recipes (true/false)
- ordering - Order by fields (e.g., -created_at, title)
- page - Page number
- page_size - Results per page

- Examples:
```
# Search for pasta recipes
GET /api/recipes/?search=pasta

# Get easy recipes
GET /api/recipes/?difficulty=easy

# Get Italian recipes
GET /api/recipes/?category=1

# Sort by newest first
GET /api/recipes/?ordering=-created_at
```
- Response:
```
{
  "count": 25,
  "next": "http://127.0.0.1:8000/api/recipes/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Pasta Carbonara",
      "slug": "pasta-carbonara",
      "description": "Classic Italian pasta dish",
      "category_name": "Italian",
      "author_name": "chef",
      "difficulty": "medium",
      "total_time": 25,
      "servings": 4,
      "image_url": null,
      "is_featured": true,
      "average_rating": 4.5,
      "review_count": 8,
      "created_at": "2025-10-15T09:00:00Z"
    }
  ]
}
```

#### Get Recipe Details
```
GET /api/recipes/pasta-carbonara/
```
- Response:
```
{
  "id": 1,
  "title": "Pasta Carbonara",
  "slug": "pasta-carbonara",
  "description": "Classic Italian pasta dish with eggs and pancetta",
  "ingredients": "400g spaghetti\n200g pancetta\n4 egg yolks\n100g Pecorino Romano\nBlack pepper",
  "ingredients_list": [
    "400g spaghetti",
    "200g pancetta",
    "4 egg yolks",
    "100g Pecorino Romano",
    "Black pepper"
  ],
  "instructions": "1. Cook pasta in salted water\n2. Fry pancetta until crispy\n3. Mix egg yolks with grated cheese\n4. Combine pasta with pancetta\n5. Add egg mixture off heat\n6. Season with black pepper",
  "instructions_list": [
    "1. Cook pasta in salted water",
    "2. Fry pancetta until crispy",
    "3. Mix egg yolks with grated cheese",
    "4. Combine pasta with pancetta",
    "5. Add egg mixture off heat",
    "6. Season with black pepper"
  ],
  "prep_time": 10,
  "cook_time": 15,
  "total_time": 25,
  "servings": 4,
  "difficulty": "medium",
  "category": 1,
  "category_name": "Italian",
  "author": 1,
  "author_name": "chef",
  "image_url": null,
  "is_featured": true,
  "reviews": [
    {
      "id": 1,
      "recipe": 1,
      "recipe_title": "Pasta Carbonara",
      "reviewer_name": "Mary Johnson",
      "reviewer_email": "mary@example.com",
      "rating": 5,
      "comment": "Absolutely delicious!",
      "created_at": "2025-10-16T18:30:00Z",
      "is_approved": true
    }
  ],
  "average_rating": 4.5,
  "created_at": "2025-10-15T09:00:00Z",
  "updated_at": "2025-10-15T09:00:00Z"
}
```
#### Create Recipe
```
POST /api/recipes/
Content-Type: application/json

{
  "title": "Chocolate Cake",
  "slug": "chocolate-cake",
  "description": "Rich and moist chocolate cake",
  "ingredients": "2 cups flour\n1.5 cups sugar\n3/4 cup cocoa powder\n2 eggs\n1 cup milk",
  "instructions": "1. Preheat oven to 350°F\n2. Mix dry ingredients\n3. Add wet ingredients\n4. Bake for 30 minutes",
  "prep_time": 20,
  "cook_time": 30,
  "servings": 8,
  "difficulty": "easy",
  "category": 3,
  "image_url": "https://example.com/cake.jpg",
  "is_featured": false
}
```

### 4. Reviews

#### Create Review
```
POST /api/reviews/
Content-Type: application/json

{
  "recipe": 1,
  "reviewer_name": "Alice Brown",
  "reviewer_email": "alice@example.com",
  "rating": 5,
  "comment": "Best recipe ever! Made it for my family and everyone loved it."
}
```
- Success Response (201):
```
{
  "id": 5,
  "recipe": 1,
  "recipe_title": "Pasta Carbonara",
  "reviewer_name": "Alice Brown",
  "reviewer_email": "alice@example.com",
  "rating": 5,
  "comment": "Best recipe ever! Made it for my family and everyone loved it.",
  "created_at": "2025-10-17T16:45:00Z",
  "is_approved": false
}
```
- Note: Reviews need admin approval (is_approved=True) before appearing publicly.

### 5. Contact Messages

#### Submit Contact Message
```
POST /api/contact/
Content-Type: application/json

{
  "name": "Robert Lee",
  "email": "robert@example.com",
  "subject": "Question about recipes",
  "message": "Do you have any vegetarian options?"
}
```

### 6. Statistics

#### Get API Statistics
```
GET /api/stats/
```
- Response:
```
{
  "total_subscribers": 150,
  "total_recipes": 45,
  "total_categories": 8,
  "total_reviews": 230,
  "featured_recipes": 6,
  "pending_reviews": 12,
  "unread_messages": 3
}
```
#### Error Responses
- 400 Bad Request
```
{
  "field_name": ["Error message"]
}
```
404 Not Found

```
{
  "error": "Recipe not found"
}
```
500 Internal Server Error
```
{
  "error": "Internal server error"
}
```
#### Rate Limiting
- Anonymous users: 100 requests/hour
- Authenticated users: 1000 requests/hour

#### Pagination
All list endpoints support pagination:

- Default page size: 10
- Max page size: 100
- Use ?page_size=20 to change page size
- Use ?page=2 to get second page

#### Testing with cURL
```
# List recipes
curl http://127.0.0.1:8000/api/recipes/

# Create subscriber
curl -X POST http://127.0.0.1:8000/api/subscribers/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Test User", "email": "test@example.com"}'

# Get specific recipe
curl http://127.0.0.1:8000/api/recipes/pasta-carbonara/

# Search recipes
curl "http://127.0.0.1:8000/api/recipes/?search=chocolate"

# Filter by category
curl "http://127.0.0.1:8000/api/recipes/?category=1"
```
#### Testing with Python requests
```
import requests

# List recipes
response = requests.get('http://127.0.0.1:8000/api/recipes/')
recipes = response.json()

# Create subscriber
data = {
    'name': 'Python User',
    'email': 'python@example.com'
}
response = requests.post('http://127.0.0.1:8000/api/subscribers/', json=data)
subscriber = response.json()

# Submit review
review_data = {
    'recipe': 1,
    'reviewer_name': 'John',
    'reviewer_email': 'john@example.com',
    'rating': 5,
    'comment': 'Excellent!'
}
response = requests.post('http://127.0.0.1:8000/api/reviews/', json=review_data)
```

# Complete REST API Installation Guide

## Step 1: Install Dependencies
```
pip install djangorestframework django-filter django-cors-headers
```
### Or use the requirements.txt:
```
pip install -r requirements.txt
```
## Step 2: Update Settings

Copy the content from `settings_updates.py` artifact and merge it with your existing `restaurant_web/settings.py`:

- Add `'rest_framework'`, `'django_filters'`, and `'corsheaders'` to `INSTALLED_APPS`
- Add CORS middleware
- Add the `REST_FRAMEWORK` configuration block

## Step 3: Replace/Update Files

Replace or create these files in your `recipes/` app:

- models.py - Enhanced models with Recipe, Category, Review, ContactMessage
- serializers.py - Complete API serializers (NEW FILE)
- api_views.py - All REST API views (NEW FILE)
- api_urls.py - API URL routing (NEW FILE)
- admin.py - Enhanced admin interface

## Step 4: Update Main URLs
Update `restaurant_web/urls.py` to include the API routes:
```
path('api/', include('recipes.api_urls')),
```

## Step 5: Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```
## Step 6: Create Test Data

```
python manage.py shell
```
### Then in the shell:
```
from recipes.models import Category, Recipe
from django.contrib.auth.models import User

# Create categories
Category.objects.create(name="Italian", slug="italian", description="Italian cuisine")
Category.objects.create(name="American", slug="american", description="American classics")
Category.objects.create(name="Desserts", slug="desserts", description="Sweet treats")

# Create a test user
user = User.objects.create_user('chef', 'chef@example.com', 'password123')

# Create a sample recipe
italian = Category.objects.get(slug="italian")
Recipe.objects.create(
    title="Pasta Carbonara",
    slug="pasta-carbonara",
    description="Classic Italian pasta dish",
    ingredients="400g spaghetti\n200g pancetta\n4 egg yolks\n100g Pecorino Romano\nBlack pepper",
    instructions="1. Cook pasta\n2. Fry pancetta\n3. Mix eggs and cheese\n4. Combine everything\n5. Season",
    prep_time=10,
    cook_time=15,
    servings=4,
    difficulty="medium",
    category=italian,
    author=user,
    is_featured=True
)

exit()
```
## Step 7: Start Server

```
python manage.py runserver
```
## Step 8: Test API Endpoints
### View API Root
```
http://127.0.0.1:8000/api/
```
### Test Endpoints
- Get all recipes:
```
curl http://127.0.0.1:8000/api/recipes/
```
- Get featured recipes:

```
curl http://127.0.0.1:8000/api/recipes/featured/
```
- Get single recipe:

```
curl http://127.0.0.1:8000/api/recipes/pasta-carbonara/
```
Create subscriber:
```
curl -X POST http://127.0.0.1:8000/api/subscribers/ \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```

Search recipes:
```
curl "http://127.0.0.1:8000/api/recipes/?search=pasta"
```


Filter by category:
```
curl "http://127.0.0.1:8000/api/recipes/?category=1"
```

Get API statistics:
```
curl http://127.0.0.1:8000/api/stats/
```

### Browsable API

#### Visit these URLs in your browser:
- http://127.0.0.1:8000/api/recipes/
- http://127.0.0.1:8000/api/categories/
- http://127.0.0.1:8000/api/subscribers/
- http://127.0.0.1:8000/api/reviews/
- http://127.0.0.1:8000/api/contact/
(You'll see a nice browsable interface where you can test all endpoints!)

#### Common Issues

- Issue: ModuleNotFoundError: No module named 'rest_framework'
| Solution: Run `pip install djangorestframework`
- Issue: ModuleNotFoundError: No module named 'django_filters'
| Solution: Run `pip install django-filter`
- Issue: CSRF verification failed
| Solution: Add CSRF token to your requests or update CSRF_TRUSTED_ORIGINS in settings.py
- Issue: Email not sending
| Solution:
1. Check your Gmail app password
2. Enable 2FA on your Gmail account
3. use console backend for testing: `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`

### Next Steps

- Test all endpoints using Postman or curl
- Add authentication (JWT tokens) if needed
- Create frontend integration
- Deploy to production
