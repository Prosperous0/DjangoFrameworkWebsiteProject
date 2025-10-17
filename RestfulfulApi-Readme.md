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


  
